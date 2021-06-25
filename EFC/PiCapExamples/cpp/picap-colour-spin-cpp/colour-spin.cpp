/*******************************************************************************

  Bare Conductive Pi Cap
  ----------------------

  colour-spin.cpp - rainbow colours on the Pi Cap LED

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

#include <stdio.h>
#include <wiringPi.h>
#include <signal.h>
#include <stdlib.h>

#define RED_LED_PIN 22
#define GREEN_LED_PIN 21
#define BLUE_LED_PIN 25

void lightRGB(int r, int g, int b) {
  // we are inverting the values, because the LED is active LOW
  // LOW - on
  // HIGH - off
  digitalWrite(RED_LED_PIN, !r);
  digitalWrite(GREEN_LED_PIN, !g);
  digitalWrite(BLUE_LED_PIN, !b);
}

void intHandler(int dummy) {
  // stop all colors
  lightRGB(0, 0, 0);
  exit(0);
}

int main() {
  // register our interrupt handler for the Ctrl+C signal
  signal(SIGINT, intHandler);

  // init wiring pi
  wiringPiSetup();

  // set up pins as outputs
  pinMode(RED_LED_PIN, OUTPUT);
  pinMode(GREEN_LED_PIN, OUTPUT);
  pinMode(BLUE_LED_PIN, OUTPUT);

  // how long should each colour stay lit before switching to next one
  int delayTime = 500;

  while(1) {
    lightRGB(0, 0, 1); delay(delayTime); // blue
    lightRGB(0, 1, 0); delay(delayTime); // green
    lightRGB(1, 0, 0); delay(delayTime); // red
    lightRGB(0, 1, 1); delay(delayTime); // cyan
    lightRGB(1, 1, 0); delay(delayTime); // yellow
    lightRGB(1, 0, 1); delay(delayTime); // magenta
    lightRGB(1, 1, 1); delay(delayTime); // white
    lightRGB(0, 0, 0); delay(delayTime); // black (off)
  }

  // make sure we return gracefully
  return(0);
}
