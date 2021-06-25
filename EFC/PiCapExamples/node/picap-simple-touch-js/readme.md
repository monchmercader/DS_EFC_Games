[![Bare Conductive](http://bareconductive.com/assets/images/LOGO_256x106.png)](http://www.bareconductive.com/)

# Bare Conductive Pi Cap Simple Touch Utility

Example touch detection code for the [Bare Conductive Pi Cap](http://www.bareconductive.com/shop/pi-cap/). Writes simple touch / release event messages to stdout.

## Requirements

* Requires [WiringPi](http://wiringpi.com/) (`apt-get install wiringpi`)
* Requires [Bare Conductive's MPR121 libary for WiringPi](https://github.com/BareConductive/wiringpi-mpr121)
* Requires [Node.js](https://nodejs.org/en/) 6.7.0
* Requires [NPM](https://www.npmjs.com/)

## Install / Build

* You should install this code as part of the Pi Cap Raspbian package: `sudo apt-get install picap`    
* However, if you are doing this yourself, clone the repository and run `npm install && node ./simple-touch.js`

## Usage

    node simple-touch.js

N.B. must be run as root    
    