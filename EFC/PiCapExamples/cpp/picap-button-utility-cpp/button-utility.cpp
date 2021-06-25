/*******************************************************************************

  Bare Conductive Pi Cap
  ----------------------

  button-utility.cpp - utility for reacting to single-click, long-click and
  double-click events from the Pi Cap button

  Written for Raspberry Pi.

  Bare Conductive code written by Stefan Dzisiewski-Smith.

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

#include <stdio.h>
#include <wiringPi.h>
#include <signal.h>
#include <unistd.h>
#include <stdlib.h>
#include <string>
#include <iostream>

using namespace std;

#define BUTTON_PIN 7 // this is wiringPi pin 7, which just happens to be physical pin 7 too
#define DEBOUNCE_LOCKOUT_MS    10
#define DOUBLEPRESS_TIMEOUT_US 300000
#define LONGPRESS_TIMEOUT_US   750000

// enums and variables for state and timeout action
enum state_t {IDLE, PRESSED, RELEASED};
state_t volatile state = IDLE;

enum action_t {NONE, SINGLE_PRESS, LONG_PRESS};
action_t volatile action = NONE;

bool volatile isrEnabled = true;
bool volatile buttonFlag = false;

string singlePressCommand = "echo \"Hello World!\" &";
string doublePressCommand = "sync && reboot now &";
string longPressCommand = "sync && halt &";

void singlePress() {
  // single press event handler
  system(singlePressCommand.c_str());
}

void doublePress() {
  // double press event handler
  system(doublePressCommand.c_str());
}

void longPress() {
  // long press event handler
  system(longPressCommand.c_str());
}

// this allows us to exit the program via Ctrl+C while still exiting elegantly
void intHandler(int dummy) {
  exit(0);
}

void alarmHandler(int dummy) {
  // time-based part of state machine
  switch (action) {
    case NONE:
      break;
    case SINGLE_PRESS:
      singlePress(); // call the single press event handler
      action = NONE;
      state = IDLE;
      break;
    case LONG_PRESS:
      longPress(); // call the long press event handler
      action = NONE;
      state = IDLE;
      break;
    default:
      break;
  }
}

void buttonIsr(void) {
  // event based part of state machine
  if(isrEnabled) buttonFlag = true; // set the ISR flag, but only if our soft-gate is enabled
}

int main(int argc, char* argv[]) {
  // sift through the arguments and set stuff up / show help as appropriate
  for (int i = 0; i < argc; i++) {
    if ((string)argv[i] == "-s" || (string)argv[i] == "--single-press" ) {
      singlePressCommand = (string)argv[i+1] + " &";
    }
    else if ((string)argv[i] == "-d" || (string)argv[i] == "--double-press") {
      doublePressCommand = (string)argv[i+1] + " &";
    }
    else if ((string)argv[i] == "-l" || (string)argv[i] == "--long-press") {
      longPressCommand = (string)argv[i+1] + " &";
    }
    else if ((string)argv[i] == "-h" || (string)argv[i] == "--help") {
      cout
        << "Maps three different PiCap button events to system calls - MUST be run as root." << endl << endl
        << "Usage: button-utility [OPTION]" << endl << endl
        << "By default single press      echoes \"Hello World!\"" << endl
        << "           double press      restarts" << endl
        << "           long press        shuts down" << endl << endl
        << "Options:" << endl
        << "  -s, --single-press [CMD]   executes [CMD] on button single press" << endl
        << "  -d, --double-press [CMD]   executes [CMD] on button double press" << endl
        << "  -l, --long-press   [CMD]   executes [CMD] on button long press" << endl
        << "  -h, --help                 displays this message" << endl;


      exit(0);
    }
  }

  // register our interrupt handler for the Ctrl+C signal
  signal(SIGINT, intHandler);

  // register our interrupt handler for the ualarm signal
  signal(SIGALRM, alarmHandler);

  wiringPiSetup();

  // button pin is input, pulled up, linked to a dual-edge interrupt
  pinMode(BUTTON_PIN, INPUT);
  pullUpDnControl(BUTTON_PIN, PUD_UP);
  wiringPiISR(BUTTON_PIN, INT_EDGE_BOTH, buttonIsr);

  while(1) {
    delay(10); // we don't need to check in here often...

    if (buttonFlag) {
      if (!digitalRead(BUTTON_PIN)) {
        // button just pressed
        switch (state) {
          case IDLE:
            // disable the button ISR, set state to pressed and set long press timeout
            isrEnabled = false;
            state = PRESSED;
            action = LONG_PRESS; // what we'll do if we time out in this state...
            ualarm(LONGPRESS_TIMEOUT_US,0);
            // delay a bit to avoid erroneous double-presses from switch bounce
            delay(DEBOUNCE_LOCKOUT_MS);
            // re-enable the ISR once we're clear of switch bounce
            isrEnabled = true;
            break;
          case RELEASED:
            // if we get another press when the switch has been released (and before
            // the double-press timeout has occured) we have a double-press
            // so reset the state machine
            action = NONE;
            state = IDLE;
            doublePress(); // call the double press event handler
            break;
          default:
            break;
        }
      }
      else {
        // button just released
        switch (state) {
          case PRESSED:
            // disable the button ISR, set state to released and set double press timeout
            isrEnabled = false;
            action = SINGLE_PRESS; // what we'll do if we timeout in this state
            ualarm(DOUBLEPRESS_TIMEOUT_US,0);
            // delay a bit to avoid erroneous double-presses from switch bounce
            delay(DEBOUNCE_LOCKOUT_MS);
            state = RELEASED;
            // re-enable the ISR once we're clear of switch bounce
            isrEnabled = true;
            break;
          default:
            break;
        }
      }

      buttonFlag = false;
    }
  }

  // make sure we return gracefully
  return(0);
}
