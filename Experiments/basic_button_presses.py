# Importing all libraries
# import RPi.GPIO as GPIO
from signal import pause
from gpiozero import LED, Button, LEDBoard


import sys, time, atexit, pygame

# Initialization, Set the GPIO numbering mode to BCM - BroadCom standard
# GPIO.setmode(GPIO.BCM)
# Initialize PyGame
pygame.init()

# Tuples and Variables for main GPIO and game
# There are 5 Buttons/LED labeled 1 to 5 in the real world. Each GPIO value is arranged in the right sequence
# Button1 = GPIO 16/19, Button2 = GPIO 17/4, Button3 = GPIO 22/27, Button4 = GPIO 9/10, BUTTON5 = GPIO 5/11
my_butt = Button(19, pull_up=False)
#my_butt = Button(19)
s_width = 640
s_height = 480
leds = LEDBoard(16,17,22,9,5)
switches = (19,4,27,10,11)
taskcomplete = False
button_pressed = False
aa = True
bananas = 0
potatos = 0
clock = pygame.time.Clock()
start_01 = False


# Main EXIT command to quit and clear all system functions
# This function gets called when we exit our script, using Ctrl+C
def exit():
    leds.off()
    print("GPIOs All Clear")
    pygame.quit()
    print("Pygame quit successfully")
    sys.exit()
    print("Python system quit successfully")
    
# This tells our script to use the "exit()" without this, our "exit()" function would never be called.
atexit.register(exit)

# Escape function to quit game by pressing ESC key
def escape_quit():
    for event in pygame.event.get():
            if event.type == pygame.QUIT  or  event.type == pygame.KEYDOWN and  event.key == pygame.K_ESCAPE:
                print("Escape key was pressed, exiting game")
                exit()
                running = False

# Button and LED Active and Light up command
def start_buttLED():
    global aa
    my_led.on()
    if  my_butt.is_pressed:
        print("button is pressed")
        aa = False
    escape_quit()
    my_led.off()
    
def add_banana():
    global bananas
    bananas +=1
    
def add_potatos():
    global potatos
    bananas +=1

def idle_scrn():
    leds.on(0)
    while True:
        color1 = 255
        for x in range(color1):
            screen.fill((255,254,color1))
            pygame.display.update()
            time.sleep(0.01)
            color1 -= 1
            escape_quit()
            if my_butt.is_pressed:
                time.sleep(0.01)
                print("Button is pressed")
                print(color1)
                break
            continue
        if my_butt.is_pressed:
                time.sleep(0.01)
                print("Button is pressed")
                print(color1)
                break
        escape_quit()
        
pygame.display.set_caption("EFC Pivot Game")
# Hide mouse pointer
pygame.mouse.set_visible(0)
# Setup the display size
screen = pygame.display.set_mode((s_width,s_height))
clock = pygame.time.Clock()
# Main
# Setup Pygame refresh rate to 60 fps
clock.tick(120)
#while aa:
    #start_buttLED()
#button
#for led in range(len(leds)):
#    leds.on(led)
#    time.sleep(1)
#    leds.off(led)
#    time.sleep(1)
leds.off(0)
Next = False
idle_scrn()
screen.fill((127,12,104))
pygame.display.update()
time.sleep(5)
#while Next == False:
#   print("Waiting for press")
#   leds.on(0)
#    escape_quit()
#    screen.fill((223,255,255))
#    pygame.display.update()
#    my_butt.wait_for_press()
#    Next = True
exit()
