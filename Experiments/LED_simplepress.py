# Importing all libraries
import RPi.GPIO as GPIO
import sys, time, atexit

# Setup GPIO
GPIO.setmode(GPIO.BCM)


# Define Tuples and Variables
leds = (16,17,22,9,5)
switches = (19,4,27,10,11)
button_pressed = False

# Defining Functions

def buttonPress(channel):
    # This function gets called every time a button is pressed, if the button pressed is the same as the button
    # that is illuminated, then we set the "correct_button" variable to True,
    # otherwise we set the "incorrect_button" variable to True.
    # We need to set some variables to global so that this function can change their value.
    button_pressed = True

def exit():
    # This function gets called when we exit our script, using Ctrl+C
    print("GPIO Clean Up!")
    GPIO.cleanup()
    
# This tells our script to use the "exit()" without this, our "exit()" function would never be called.
atexit.register(exit)

#Loop through the leds to set them up
for led in leds:
    # Set the led to be an ouput
    GPIO.setup(led, GPIO.OUT)
    # Turn the led off
    GPIO.output(led,False)

# Loop through the switches to set them up
for switch in switches:
    # Set the switch to be an input
    GPIO.setup(switch, GPIO.IN)
    # Add rising edge detection
    GPIO.add_event_detect(switch, GPIO.RISING, bouncetime=300)
    # Add the function "buttonPress" to be called when switch is pressed.
    GPIO.add_event_callback(switch, buttonPress)

# Main loop
# Press Button 1 to start the game
while GPIO.input(switches[0]) == GPIO.LOW:
    GPIO.output(leds[0],True)
    time.sleep(0.01)
print(" Button 1 is pressed! Exit")           
exit()
