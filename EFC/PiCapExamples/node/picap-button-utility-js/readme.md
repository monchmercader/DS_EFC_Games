[![Bare Conductive](http://bareconductive.com/assets/images/LOGO_256x106.png)](http://www.bareconductive.com/)

# Bare Conductive Pi Cap Button Utility

Example button code (and useful command line utility) for the  [Bare Conductive Pi Cap](http://www.bareconductive.com/shop/pi-cap/). Allows you to run bash commands when a single-press, double-press or long-press is detected on the Pi Cap button.


## Requirements
* Requires [WiringPi](http://wiringpi.com/) (`apt-get install wiringpi`)
* Requires [Node.js](https://nodejs.org/en/) 6.7.0
* Requires [NPM](https://www.npmjs.com/)


## Install / Build

* You should install this code as part of the Pi Cap Raspbian package: `apt-get install picap`    
* However, if you are doing this yourself, clone the repository and run `npm install && node ./button-utility.js`

## Usage

    Maps three different PiCap button events to system calls - MUST be run as root.
    
    Usage: node button-utility.js [OPTION]
    
    By default single press    echoes "Hello World!"
               double press    restarts
               long press      shuts down
               
    Options:
    -s, --single-press [CMD]   executes [CMD] on button single press
    -d, --double-press [CMD]   executes [CMD] on button double press     
    -l, --long-press   [CMD]   executes [CMD] on button long press      
    -h, --help                 displays this message
    