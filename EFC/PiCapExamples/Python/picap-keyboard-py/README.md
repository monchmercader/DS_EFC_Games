[![Bare Conductive](http://bareconductive.com/assets/images/LOGO_256x106.png)](http://www.bareconductive.com/)

# Bare Conductive Keyboard Emulation

Code for the  [Bare Conductive Pi Cap](http://www.bareconductive.com/shop/pi-cap/). Allows you to emulate a keyboard and map keyboard strokes to the Pi Cap's electrodes.

## Requirements
* Requires [python-dev](https://www.python.org/) (`apt-get install python-dev`)
* Requires [WiringPi](http://wiringpi.com/) (`apt-get install wiringpi`)
* Requires [uinput](https://github.com/tuomasjjrasanen/python-uinput) (`sudo pip install python-uinput`)
* Requires [Bare Conductive's MPR121 libary for WiringPi](https://github.com/BareConductive/wiringpi-mpr121)

## Install / Build

* You should install this code as part of the Pi Cap Raspbian package: `sudo apt-get install picap`    
* However, if you are doing this yourself, clone the repository and follow the usage instructions.

## Usage
	
    modprobe uinput
    python keyboard.py

N.B. must be run as root    