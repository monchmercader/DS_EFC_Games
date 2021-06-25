/*******************************************************************************

  Bare Conductive Pi Cap
  ----------------------

  datastream-tty.js - streams capacitive sense data from MPR121 to stdout

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

var MPR121 = require('node-picap');
var mpr121;

// this is the touch threshold - setting it low makes it more like a proximity trigger
// default value is 40 for touch
var touchThreshold = 40;

// this is the release threshold - must ALWAYS be smaller than the touch threshold
// default value is 20 for touch
var releaseThreshold = 20;

// correct address for the Pi Cap - other boards may vary
mpr121 = new MPR121('0x5C');

mpr121.setTouchThreshold(touchThreshold);
mpr121.setReleaseThreshold(releaseThreshold);

mpr121.on('data', function(data) {
  // split out each of the various data streams...
  var touch = data.map(function(electrode) { return electrode.isTouched ? 1 : 0; });
  var tths  = data.map(function(electrode) { return electrode.touchThreshold; });
  var rths  = data.map(function(electrode) { return electrode.releaseThreshold; });
  var fdat  = data.map(function(electrode) { return electrode.filtered; });
  var bval  = data.map(function(electrode) { return electrode.baseline; });
  var diff  = data.map(function(electrode) { return electrode.baseline - electrode.filtered; });

  // ...and send them out via stdout - simples!
  console.log('TOUCH: ' + touch.join(' '));
  console.log('TTHS: ' + tths.join(' '));
  console.log('RTHS: ' + rths.join(' '));
  console.log('FDAT: ' + fdat.join(' '));
  console.log('BVAL: ' + bval.join(' '));
  console.log('DIFF: ' + diff.join(' '));
});

// this allows us to exit the program via Ctrl+C while still exiting elegantly
process.on('SIGINT', function () {
  process.exit(0);
});
