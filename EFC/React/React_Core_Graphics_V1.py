# DS-EFC01-REACT-MM-RpiCode
# Version Beta 1.00
# 20210623V100

# GAME APPLICATION DESCRIPTION:
# This game application is designed for the EFC Museum Space React game
# The objective of the game is for the player to press as many of the activated (lit up) buttons as they can
# within the alloted time. More correct buttons pressed = Winner.

# Libraries section - import the libraries and functions that we will be using in our script
# - gpiozero as GPIO controller
# - OS: file management and importing files
# - Pygame: Game libraries
# - Time: Timer function for stopwatch

# Importing all libraries
import sys, time, atexit, pygame, random
from gpiozero import LED, Button, LEDBoard

# Initialize PyGame
pygame.init()
pygame.joystick.init()
joystickA = pygame.joystick.Joystick(0)

# VARIABLES SECTION ---- Defining Variables ------

# Tuples and Variables for used in the Game
# This game will use a zerodelay arcade joystick board as an input and a custom board to control the LED lights
# There are 12 Buttons & LED arranged in a grid in the real world. Each GPIO value is arranged in the right sequence
s_width = 1920
s_height = 1080

# Define our LED tuples
leds = LEDBoard(24,23,22,27,17,4,19,18,7,11,9,10)

# Define our variables
random_num = 0
time_Out = 0
current_Time = 0
game_running = True
button = 0
B = 0
start = 0
end = 0
correct_button = False
score = 0

# Wait times for following screens
start_01 = False
on_screen = 0.2
scorescn_time = 5
starter01 = True

# Pygame visual variables, loading in visual assets, fonts,
s_width = 1920
s_height = 1080
# Pygame window title
pygame.display.set_caption("EFC React Game")
# Hide mouse pointer
pygame.mouse.set_visible(0)
# Setup the display size
screen = pygame.display.set_mode((s_width,s_height))
#screen = pygame.display.set_mode((s_width,s_height), pygame.FULLSCREEN)
score_font = pygame.font.Font('Fonts/DSEG14Modern-Regular.ttf', 350)
# Loading images, Game_screen 14 images
Game_screen = [pygame.image.load('Images/01-Ambient.png').convert(), \
               pygame.image.load('Images/02-Instruction-1.png').convert(), \
               pygame.image.load('Images/02-Instruction-2.png').convert(), \
               pygame.image.load('Images/02-Instruction-3.png').convert(), \
               pygame.image.load('Images/02-Instruction-4.png').convert(), \
               #5
               pygame.image.load('Images/02-Instruction-4-Diagram.png').convert(), \
               pygame.image.load('Images/02-Instruction-4.png').convert(), \
               pygame.image.load('Images/02-Instruction-4-Diagram.png').convert(), \
               pygame.image.load('Images/03-InUse-Header.png').convert(), \
               pygame.image.load('Images/04-Finished-CTA.png').convert(), \
               #10
               pygame.image.load('Images/04-Finished-Footer.png').convert(), \
               pygame.image.load('Images/04-Finished-Header.png').convert(), \
               pygame.image.load('Images/04-Finish-Initial.png').convert()]

Pattern_ins = pygame.image.load('Images/03-InUse-Header.png').convert()

Timebar_bg =  pygame.image.load('Images/03-InUse-ScoreBg.png').convert()

Timebar =  pygame.image.load('Images/03-InUse-Timer.png').convert()

Bg_screen = [pygame.image.load('Images/02-Instruction-Bg.png').convert(), pygame.image.load('Images/04-Finished-Bg.png').convert()]

# !!!!!!!!!!!  Set Pygame refresh rate variable = clock ??????????????????????????
clock = pygame.time.Clock()

def exit():
    # This function gets called when we exit our script, using Ctrl+C
    print("Cleaning up all interfaces!")
    leds.off()
    pygame.joystick.init()
    print("LEDs and Joysticks clean")
    pygame.quit()
    print("Pygame quit successfully")
    sys.exit()
    print("Python system quit successfully")

# This tells our script to use the "exit()" without this, our "exit()" function would never be called.
atexit.register(exit)

# Escape function to quit game by pressing ESC key
def escape_quit():
    global game_running
    for event in pygame.event.get():
        if event.type == pygame.QUIT  or  event.type == pygame.KEYDOWN and  event.key == pygame.K_ESCAPE:
            print("ESC key was pressed, exiting game")
            exit()
            game_running = False
        
# Idle Screen
def idle_scrn():
    leds.off()
    idle_slide = (Game_screen[0])
    fadeout_fps = 0
    stay_scrn = 0
    a = 0
    leds.on(0)
    while starter01:
        fade_fps = 0
        fade_rate = 10
        escape_quit()
        for fade_fps in range(45):
            fade_rate += 20
            idle_slide.set_alpha(fade_rate)
            screen.fill((255,255,255))
            screen.blit(idle_slide, (0,0))
            for event in pygame.event.get():
                if event.type == pygame.JOYBUTTONDOWN:
                    if event.button == 0:
                        leds.off()
                        print("turn off LED")
                        return()
            pygame.time.delay(1)
            pygame.display.update()
        escape_quit()

# Instruction screen sequence.
# Playing all the instructions with screen time of !!!!!!!1!!!!!!!! seconds each
def inst_seq():
    inst_wait = True
    escape_quit()
    # Instruction 1
    escape_quit()
    screen.fill((255,255,255))
    screen.blit(Bg_screen[0], (0,0))
    screen.blit(Game_screen[1], (90,0))
    pygame.display.update()
    time.sleep(on_screen)
    # Instruction 2
    escape_quit()
    screen.fill((255,255,255))
    screen.blit(Bg_screen[0], (0,0))
    screen.blit(Game_screen[2], (90,0))
    pygame.display.update()
    time.sleep(on_screen)
    # Instruction 03
    escape_quit()
    screen.fill((255,255,255))
    screen.blit(Bg_screen[0], (0,0))
    screen.blit(Game_screen[4], (40,0))
    screen.blit(Pattern_ins, (420,360))
    pygame.display.update()
    time.sleep(on_screen)
    escape_quit()
    # Instruction 04 screen
    screen.fill((255,255,255))
    screen.blit(Bg_screen[0], (0,0))
    screen.blit(Game_screen[4], (70,1040))
    screen.blit(Game_screen[6], (40,0))
    pygame.display.update()
    time.sleep(on_screen)
    # Button 1 LED blink
    while inst_wait:
        escape_quit()
        leds.on(0)
        time.sleep(0.7)
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0:
                    leds.off()
                    print("Instruction segment...waiting to start...")
                    return()
        pygame.time.delay(1)
        pygame.display.update()
        escape_quit()

# Final Score screen
def final_Score():
    final_time = time_lapsed
    f_score = str(round(final_time, 2))
    screen.fill((255,255,255))
    screen.blit(Bg_screen, (0,0))
    screen.blit(Game_screen[13], (50,10))
    final_score = counterfont.render(f_score, 3, (0, 101, 177))
    finalscore_rect = final_score.get_rect(center = screen.get_rect().center)
    screen.blit(final_score, (580,470))
    pygame.display.flip()
    time.sleep(scorescn_time)


# GAME PROPER ------------------------------------------------------------------------------------

# Idle Screen
idle_scrn()

# Instructions
inst_seq()

# GAME PLAY SECTION --------------------
score = 0
start_Time = pygame.time.Clock()
start = int(time.time())
leds.off()
random_num = random.randint(0, 11)
leds.on(random_num)
print(random_num)
while time_Out != 30:
    #while game_running:
    for event in pygame.event.get():
        print("For Event started, Game screen started")
        screen.fill((255,255,255))
        screen.blit(Bg_screen[0], (0,0))
        screen.blit(Game_screen[8], (110,9))
        score_text = score_font.render(str(score), 3, "red")
        score_rect = score_text.get_rect(center = screen.get_rect().center)
        screen.blit(score_text, (580,470))
        pygame.display.update()
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
    #print("TIMER: ", time_Out)
    #print(type(start_Time))
    #print(current_Time)
    #print(type(current_Time))
# FINAL SCORE ------------------------
leds.off()
screen.fill((255,255,255))
screen.blit(Bg_screen[0], (0,0))
screen.blit(Game_screen[12], (50,10))
screen.blit(score_text, (580,470))
pygame.display.flip()
time.sleep(scorescn_time)
print("Your Score: ", score)
exit()