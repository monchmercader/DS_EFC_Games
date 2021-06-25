/*******************************************************************************

  Bare Conductive Pi Cap
  ----------------------

  datastream-osc.cpp - streams capacitive sense data from MPR121 to OSC endpoint

  Written for Raspberry Pi.

  Bare Conductive code written by Szymon Kaliski.

  This work is licensed under a MIT license https://opensource.org/licenses/MIT
  
  Copyright (c) 2016, Bare Conductive
  
  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files (the "Software"), to deal
  in the Software without restriction, including without limitation the rights
  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
  copies of the Software, and to permit persons to whom the Software is
  furnished to do so, subject to the following conditions:
  
  The above copyright notice and this permission notice shall be included in all
  copies or substantial portions of the Software.
  
  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
  SOFTWARE.

 *******************************************************************************/

#include <MPR121.h>
#include <signal.h>
#include <iostream>
#include <stdlib.h>

#include <lo/lo.h>

#define NUM_ELECTRODES 12

using namespace std;

// "volatile" means - I can be modified from elsewhere
bool volatile keepRunning = true;

// this allows us to exit the program via Ctrl+C while still exiting elegantly
void intHandler(int dummy) {
  keepRunning = false;
  exit(0);
}

int main(int argc, char* argv[]) {
  string host = "127.0.0.1";
  string port = "3000";

  // sift through the arguments and set stuff up / show help as appropriate
  for (int i = 0; i < argc; i++) {
    if ((string)argv[i] == "-h" || (string)argv[i] == "--host" ) {
      host = (string)argv[i+1];
    }
    else if ((string)argv[i] == "-p" || (string)argv[i] == "--port") {
      port = (string)argv[i+1];
    }
    else if ((string)argv[i] == "--help") {
      cout
        << "Streams Pi Cap data over OSC - MUST be run as root." << endl << endl
        << "Usage: datastream-osc [OPTION]" << endl << endl
        << "Options:" << endl
        << "  -h, --host   host address, defaults to 127.0.0.1" << endl
        << "  -p, --port   port on which to send, defaults to 3000" << endl
        << "      --help   displays this message" << endl;

      exit(0);
    }
  }

  // wait for Ctrl+C
  signal(SIGINT, intHandler);

  // create OSC address
  lo_address address = lo_address_new(host.c_str(), port.c_str());

  // default MPR121 address on the Pi Cap
  if (!MPR121.begin(0x5C)) {
    cout << "error setting up MPR121: ";

    switch (MPR121.getError()) {
      case NO_ERROR:
        cout << "no error" << endl;
        break;
      case ADDRESS_UNKNOWN:
        cout << "incorrect address" << endl;
        break;
      case READBACK_FAIL:
        cout << "readback failure" << endl;
        break;
      case OVERCURRENT_FLAG:
        cout << "overcurrent on REXT pin" << endl;
        break;
      case OUT_OF_RANGE:
        cout << "electrode out of range" << endl;
        break;
      case NOT_INITED:
        cout << "not initialised" << endl;
        break;
      default:
        cout << "unknown error" << endl;
        break;
    }

    exit(1);
  }

  // this is the touch threshold - setting it low makes it more like a proximity trigger
  // default value is 40 for touch
  int touchThreshold = 40;

  // this is the release threshold - must ALWAYS be smaller than the touch threshold
  // default value is 20 for touch
  int releaseThreshold = 20;

  MPR121.setTouchThreshold(touchThreshold);
  MPR121.setReleaseThreshold(releaseThreshold);

  // reuse iterating variable
  int i;

  while (keepRunning) {
    // bundle all OSC messages together
    lo_bundle bundle = lo_bundle_new(LO_TT_IMMEDIATE);

    if (MPR121.touchStatusChanged()) {
      MPR121.updateTouchData();
    }

    MPR121.updateBaselineData();
    MPR121.updateFilteredData();

    // touch values
    lo_message touch = lo_message_new();
    for (i = 0; i < NUM_ELECTRODES; i++) {
      lo_message_add(touch, "i", MPR121.getTouchData(i));
    }
    lo_bundle_add_message(bundle, "/touch", touch);

    // touch thresholds
    lo_message tths = lo_message_new();
    for (i = 0; i < NUM_ELECTRODES; i++) {
      lo_message_add(tths, "i", touchThreshold);
    }
    lo_bundle_add_message(bundle, "/tths", tths);

    // release thresholds
    lo_message rths = lo_message_new();
    for (i = 0; i < NUM_ELECTRODES; i++) {
      lo_message_add(rths, "i", releaseThreshold);
    }
    lo_bundle_add_message(bundle, "/rths", rths);

    // filtered values
    lo_message fdat = lo_message_new();
    for (i = 0; i < NUM_ELECTRODES; i++) {
      lo_message_add(fdat, "i", MPR121.getFilteredData(i));
    }
    lo_bundle_add_message(bundle, "/fdat", fdat);

    // baseline values
    lo_message bval = lo_message_new();
    for (i = 0; i < NUM_ELECTRODES; i++) {
      lo_message_add(bval, "i", MPR121.getBaselineData(i));
    }
    lo_bundle_add_message(bundle, "/bval", bval);

    // the trigger and threshold values refer to the difference between
    // the filtered data and the running baseline - see p13 of
    // http://www.freescale.com/files/sensors/doc/data_sheet/MPR121.pdf

    // value pairs
    lo_message diff = lo_message_new();
    for (i = 0; i < NUM_ELECTRODES; i++) {
      lo_message_add(diff, "i", MPR121.getBaselineData(i) - MPR121.getFilteredData(i));
    }
    lo_bundle_add_message(bundle, "/diff", diff);

    // finally, send the bundle and clean up
    lo_send_bundle(address, bundle);
    lo_bundle_free_recursive(bundle);

    // a little delay so that we don't just sit chewing CPU cycles
    // could implement this with proper interrupts for greater efficiency

    delay(10);
  }

  // make sure we return gracefully
  return(0);
}
