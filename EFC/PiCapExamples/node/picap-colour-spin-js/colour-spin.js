/*******************************************************************************

  Bare Conductive Pi Cap
  ----------------------

  colour-spin.js - rainbow colours on the Pi Cap LED

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

var Gpio      = require('onoff').Gpio;

// set up LED pins - note that the LED is common anode (and hence active low)
var gpioRed   = new Gpio(6,  'out', 'none', { activeLow: true });
var gpioGreen = new Gpio(5,  'out', 'none', { activeLow: true });
var gpioBlue  = new Gpio(26, 'out', 'none', { activeLow: true });

function lightRGB(r, g, b) {
  gpioRed.writeSync(r);
  gpioGreen.writeSync(g);
  gpioBlue.writeSync(b);
}

// initialise to all off
lightRGB(0, 0, 0);

function lightSequence(index) {
  var sequence = [
    [ 0, 0, 1 ], // blue
    [ 0, 1, 0 ], // green
    [ 1, 0, 0 ], // red
    [ 0, 1, 1 ], // cyan
    [ 1, 1, 0 ], // yellow
    [ 1, 0, 1 ], // magenta
    [ 1, 1, 1 ], // white
    [ 0, 0, 0 ]  // off
  ];

  lightRGB.apply(null, sequence[index]);

  index = index + 1;

  if (index >= sequence.length) {
    index = 0;
  }

  // select the next colour in the sequence every 500 ms
  setTimeout(function() {
    lightSequence(index);
  }, 500);
}

// begin the sequence with the led off
lightSequence(0);

// this allows us to exit the program via Ctrl+C while still exiting elegantly
process.on('SIGINT', function () {
  lightRGB(0, 0, 0);
  process.exit(0);
});
