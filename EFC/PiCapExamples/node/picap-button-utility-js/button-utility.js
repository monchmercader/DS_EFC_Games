/*******************************************************************************

  Bare Conductive Pi Cap
  ----------------------

  button-utility.js - utility for reacting to single-click, long-click and
  double-click events from the Pi Cap button

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

var Gpio  = require('onoff').Gpio;
var argv  = require('yargs').argv;
var spawn = require('child_process').spawn;

var button = new Gpio(4, 'in', 'both', { activeLow: true });

// default button behaviours
var singlePressCommand = 'echo \'Hello World!\' &';
var doublePressCommand = 'sync && reboot now &';
var longPressCommand   = 'sync && halt &';

// sift through the arguments and set stuff up / show help as appropriate

if (argv.h || argv.help) { printHelp(); }
if (argv.s || argv['single-press']) { singlePressCommand = argv.s || argv['single-press']; }
if (argv.d || argv['double-press']) { doublePressCommand = argv.d || argv['double-press']; }
if (argv.l || argv['long-press'])   { longPressCommand   = argv.l || argv['long-press'];   }

function printHelp() {
  console.log('Maps three different PiCap button events to system calls.\n');
  console.log('Usage: node button-utility.js [OPTION]\n');
  console.log('By default single press      echoes \'Hello World!\'');
  console.log('           double press      restarts');
  console.log('           long press        shuts down\n');
  console.log('Options:');
  console.log('  -s, --single-press [CMD]   executes [CMD] on button single press');
  console.log('  -d, --double-press [CMD]   executes [CMD] on button double press');
  console.log('  -l, --long-press   [CMD]   executes [CMD] on button long press');
  console.log('  -h, --help                 displays this message');
  process.exit(0);
}

function exec(cmd) {
  var spawned = spawn(cmd, { shell: '/bin/bash' });

  spawned.stdout.on('data', function(data) { console.log(data.toString()); });
  spawned.stderr.on('data', function(data) { console.log(data.toString()); });
}

function singlePress() { exec(singlePressCommand); }
function doublePress() { exec(doublePressCommand); }
function longPress()   { exec(longPressCommand);   }

// button press timeouts (in ms)
var doublePressTimeout = 300;
var longPressTimeout   = 750;

var isPressed, lastPressed, lastReleased;

button.watch(function(error, value) {
  var now = (new Date()).getTime();

  isPressed = value === 1;

  if (isPressed) {
    lastPressed = now;
  }
  else {
    lastReleased = now;
  }
});

// main program logic - detects single-press, double-press and long-press button events
setInterval(function() {
  var now = (new Date()).getTime();

  if (isPressed) {
    if (lastPressed && lastReleased && lastPressed < (lastReleased + doublePressTimeout)) {
      doublePress();
      lastPressed  = undefined;
      lastReleased = undefined;
    }
    else if (lastPressed && lastPressed < (now - longPressTimeout)) {
      longPress();
      lastPressed  = undefined;
      lastReleased = undefined;
    }
  }
  else {
    if (lastReleased && lastPressed && lastReleased < (now - doublePressTimeout)) {
      singlePress();
      lastPressed = undefined;
    }
  }
}, 10);

// this allows us to exit the program via Ctrl+C while still exiting elegantly
process.on('SIGINT', function () {
  button.unexport();
  process.exit(0);
});
