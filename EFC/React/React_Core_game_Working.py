# Here we import the libraries and function that we will be using in our script
import sys, random, pygame, time, gpiozero, atexit
import RPi.GPIO as GPIO
from gpiozero import LED, Button, LEDBoard

pygame.init()
pygame.joystick.init()

# Define our LED and Button tuples
leds = LEDBoard(24,23,22,27,17,4,19,18,7,11,9,10)
random_num = -1
# Define our variables
time_Out = 0
current_Time = 0
game_Run = True
button = 0
B = 0

def exit():
    # This function gets called when we exit our script, using Ctrl+C
    print("GPIO Clean Up!")
    leds.off()
    print("GPIOs All Clear")
    pygame.quit()
    print("Pygame quit successfully")
    sys.exit()
    print("Python system quit successfully")

start = 0
end = 0
# This tells our script to use the "exit()" without this, our "exit()" function would never be called.
atexit.register(exit)
pygame.joystick.init()
joystickA = pygame.joystick.Joystick(0)
buttons = joystickA.get_numbuttons()
start_Time = pygame.time.Clock()
start = int(time.time())

correct_button = False
score = 0

leds.off()
random_num = random.randint(0, 11)
leds.on(random_num)
print(random_num)
while time_Out != 30:
#    while game_Run:
    for event in pygame.event.get():    
        print("For Event started")
        if event.type == pygame.JOYBUTTONDOWN:
            print("If then, event type started")
            if event.button == random_num:
                B = event.button
                print(B, " button pressed, CORRECT")
                leds.off()
                random_num = random.randint(0, 11)
                leds.on(random_num)
                print(random_num)
                score += 1
    current_Time = int(time.time())
    time_Out = current_Time - start
    print("TIMER: ", time_Out)
    #print(type(start_Time))
    #print(current_Time)
    #print(type(current_Time))
print("Your Score: ", score)
exit()