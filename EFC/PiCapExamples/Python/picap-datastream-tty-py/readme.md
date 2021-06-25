[![Bare Conductive](http://bareconductive.com/assets/images/LOGO_256x106.png)](http://www.bareconductive.com/)

# Bare Conductive Pi Cap TTY Data Stream Utility

Example TTY (terminal) data streaming code for the [Bare Conductive Pi Cap](http://www.bareconductive.com/shop/pi-cap/). Streams touch and proximity data from the Pi Cap to stdout.

## Requirements
* Requires [python-dev](https://www.python.org/) (`apt-get install python-dev`)
* Requires [WiringPi](http://wiringpi.com/) (`apt-get install wiringpi`)
* Requires [Bare Conductive's MPR121 libary for WiringPi](https://github.com/BareConductive/wiringpi-mpr121)

## Install / Build

* You should install this code as part of the Pi Cap Raspbian package: `sudo apt-get install picap`    
* However, if you are doing this yourself, clone the repository and follow the usage instructions.

## Usage

    python datastream-tty

N.B. must be run as root    

## Output message formatting

    TOUCH:		electrode touch values (0 not touched, 1 touched)
    TTHS:		electrode touch thresholds (0..255)
    RTHS:		electrode release thresholds (0..255)
    FDAT:		electrode filtered data (0..1023)
    BVAL:		electrode baseline values (0..1023)
    DIFF:		BVAL - FDAT (0..1023)
