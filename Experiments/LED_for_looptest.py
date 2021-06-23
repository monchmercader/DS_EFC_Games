# Importing all libraries
import RPi.GPIO as GPIO
import sys, time, atexit, pygame

# Setup GPIO and Pygame
GPIO.setmode(GPIO.BCM)
pygame.init()

# Define Tuples and Variables
leds = (16,17,22,9,5)
switches = (19,4,27,10,11)
button_pressed = False
taskcomplete = False

# Pygame visual variables
screen = pygame.display.set_mode( (1024,240) )
counterfont = pygame.font.Font('DSEG14Modern-Regular.ttf', 70)

# Set Pygame refresh rate variable = clock 
clock = pygame.time.Clock()

# Clock variables
sec_val = 0
sec = 0
mins = 0
hours = 0

# Status variables
paused  = False
running = True

# FUNCTIONS SECTION: -------- Defining Functions ------------------

# Function that renders segment display on screen 
def time_convert(sec):
    sec = sec % 60
    sec_val = ("Timer: {0}".format(round((sec), 2)))
    counting_text = counterfont.render(str(sec_val), 3, (134,145,255))
    counting_rect = counting_text.get_rect(left = screen.get_rect().left)
    screen.fill( (0,0,0) )
    screen.blit(counting_text, (300,40))
    pygame.display.update()
    
# Stopwatch function to compute for a SS:MS based stopwatch
def stop_Watch():
    end_time = time.time()
    time_lapsed = end_time - start_time
    sec_val = time_convert(time_lapsed)

# Press Button 1 to start the game
def escape_quit():
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
                running = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("Escape key was pressed, exiting game")
                    exit()
                    running = False

# Button and LED Active and Light up command
def active_buttLED(buttonID):
    id_GPIO = buttonID
    while GPIO.input(switches[id_GPIO]) == GPIO.LOW:
        escape_quit()
        GPIO.output(leds[id_GPIO],True)
        time.sleep(0.01)
        stop_Watch()
    GPIO.output(leds[id_GPIO],False)
    print("Debug message: button ", id_GPIO+1, "was pressed")



# Confirming if the button was pressed
def buttonPress(channel):
    # This function gets called every time a button is pressed, if the button pressed is the same as the button
    # that is illuminated, then we set the "correct_button" variable to True,
    # otherwise we set the "incorrect_button" variable to True.
    # We need to set some variables to global so that this function can change their value.
    button_pressed = True

# Command to exit program
def exit():
    # This function gets called when we exit our script, using Ctrl+C
    print("GPIO Clean Up!")
    GPIO.cleanup()
    pygame.quit()
    sys.exit()


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


# Main sequence code
# Setup Pygame refresh rate to 120 fps
clock.tick(120)

# Start the clock
# start_time = pygame.time.get_ticks() 
start_time = time.time()

# Main loop
while running:
    # Press Button 1 to start the game
    active_buttLED(0)
    # Press Button 2 to start the game
    active_buttLED(1)
    # Press Button 3 to start the game
    active_buttLED(2)
    running = False
exit()