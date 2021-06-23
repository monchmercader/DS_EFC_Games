# Here we import the libraries and function that we will be using in our script
import sys, random, pygame, time, gpiozero, atexit
import RPi.GPIO as GPIO
from gpiozero import LED, Button, LEDBoard

pygame.init()
pygame.joystick.init()

# Define our LED and Button tuples
leds = LEDBoard(12,17,22,9,5)
# Define our variables
random_number = -1
correct_button = False
incorrect_button = False
button_pressed = False
max_points = 10
deduction = 5

def exit():
    # This function gets called when we exit our script, using Ctrl+C
    print("GPIO Clean Up!")
    leds.off()
    print("GPIOs All Clear")
    pygame.quit()
    print("Pygame quit successfully")
    sys.exit()
    print("Python system quit successfully")

# This tells our script to use the "exit()" without this, our "exit()" function would never be called.
atexit.register(exit)

# Check that we have defined the same amount of leds as switches
#if len(leds) == len(switches):
#    max = (len(leds) - 1)
#else:
#    print("There isn't the same number of LEDS as SWITCHES")
#    exit()
    
# Create an infinite loop, so we can play the game as many times as we want
while(True):

    loop = 10 # This loop tells us how many buttons are going to be illuminated per game.
    counter = 0 # Create a variable to count how many buttons get illuminated.
    score = 0 # Set our score variable to 0.
    
#    print("Press the illuminated button to start")
#    leds.on(0) # Turn on the start LED

#    while GPIO.input(switches[2]) == GPIO.LOW: # Wait until the middle switch has been pressed.
#        time.sleep(0.01)

for i in range(buttons):
    button = joystick.get_button(i)
    print("Initialized button variable")

    # Start the game
    while counter < loop:
        correct_button = False
        incorrect_button = False
        button_pressed = False
        
        counter += 1 # Increment our counter variable by 1.
        random_delay = random.randint(500,1500) / 1000 # Create a random number to be used as a delay to turn on a led. 
        random_number = random.randint(0,4) # Create another random number to be used to turn on one of the leds.
        print("defined randoms")
        time.sleep(random_delay) # Wait for a random amount of time, as defined above
        leds.on(random_number) # Turn on a random led, as defined above
        start = time.time() # Take a note of the time when the led was illuminated (so we can see how long it takes for the player to press the button)
        print("LED lit start timer started")
        if button.is_pressed:
            buttonval = joystick.get_button(i)
            if buttonval == random_number:
                print("pressed the correct button random value is", +random_number, "buttonval is", +buttonval)
            else:
                print("random value", +random_number, "buttonval is", +buttonval)
        time.sleep(1)