import pygame, time, gpiozero, atexit
from gpiozero import LED, Button, LEDBoard

# Define some colors.
BLACK = pygame.Color('black')
WHITE = pygame.Color('white')

# Main EXIT command to quit and clear all system functions
# This function gets called when we exit our script, using Ctrl+C
def exit():
    leds.off()
    start_led.off()
    print("GPIOs All Clear")
    pygame.quit()
    print("Pygame quit successfully")
    sys.exit()
    print("Python system quit successfully")
    
# This tells our script to use the "exit()" without this, our "exit()" function would never be called.
atexit.register(exit)

# Function that renders time/segment display on screen 
def time_convert(sec):
    sec = sec % 60
    sec_val = ("{0}".format(round((sec), 1)))
    screen.fill((255,255,255))
    screen.blit(Bg_screen, (0,0))
    screen.blit(Game_screen[9], (100,0))
    counting_text = counterfont.render(str(sec_val), 3, (0,101,177))
    counting_rect = counting_text.get_rect(center = screen.get_rect().center)
    screen.blit(counting_text, (counting_rect)) 
    pygame.display.update()
    
# Stopwatch function to compute for a SS:MS based stopwatch
def stop_Watch():
    global time_lapsed
    end_time = time.time()
    time_lapsed = end_time - start_time
    sec_val = time_convert(time_lapsed)

# Escape function to quit game by pressing ESC key
def escape_quit():
    for event in pygame.event.get():
            if event.type == pygame.QUIT  or  event.type == pygame.KEYDOWN and  event.key == pygame.K_ESCAPE:
                print("Escape key was pressed, exiting game")
                exit()
                running = False


# This is a simple class that will help us print to the screen.
# It has nothing to do with the joysticks, just outputting the
# information.
class TextPrint(object):
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 20)

    def tprint(self, screen, textString):
        textBitmap = self.font.render(textString, True, BLACK)
        screen.blit(textBitmap, (self.x, self.y))
        self.y += self.line_height

    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15

    def indent(self):
        self.x += 10

    def unindent(self):
        self.x -= 10


pygame.init()

# Set the width and height of the screen (width, height).
screen = pygame.display.set_mode((500, 700))

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates.
clock = pygame.time.Clock()

# Initialize the joysticks.
pygame.joystick.init()

# Get ready to print.
textPrint = TextPrint()
#GPIO.setmode(GPIO.BCM)
#leds = (6,17,22,9,5)
leds = LEDBoard(17,22,9,5)
start_led = LED(12)
    
# -------- Main Program Loop -----------
while not done:
    #
    # EVENT PROCESSING STEP
    #
    # Possible joystick actions: JOYAXISMOTION, JOYBALLMOTION, JOYBUTTONDOWN,
    # JOYBUTTONUP, JOYHATMOTION
    
    for event in pygame.event.get(): # User did something.
        if event.type == pygame.QUIT: # If user clicked close.
            done = True # Flag that we are done so we exit this loop.
        elif event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
    
        elif event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")
            
    #
    # DRAWING STEP
    #
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
    textPrint.reset()

    # Get count of joysticks.
    joystick_count = pygame.joystick.get_count()

    textPrint.tprint(screen, "Number of joysticks: {}".format(joystick_count))
    textPrint.indent()

    # For each joystick:
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()

        try:
            jid = joystick.get_instance_id()
        except AttributeError:
            # get_instance_id() is an SDL2 method
            jid = joystick.get_id()
        textPrint.tprint(screen, "Joystick {}".format(jid))
        textPrint.indent()

        # Get the name from the OS for the controller/joystick.
        name = joystick.get_name()
        textPrint.tprint(screen, "Joystick name: {}".format(name))

        try:
            guid = joystick.get_guid()
        except AttributeError:
            # get_guid() is an SDL2 method
            pass
        else:
            textPrint.tprint(screen, "GUID: {}".format(guid))

        # Usually axis run in pairs, up/down for one, and left/right for
        # the other.
        axes = joystick.get_numaxes()
        textPrint.tprint(screen, "Number of axes: {}".format(axes))
        textPrint.indent()

        for i in range(axes):
            axis = joystick.get_axis(i)
            textPrint.tprint(screen, "Axis {} value: {:>6.3f}".format(i, axis))
        textPrint.unindent()

        buttons = joystick.get_numbuttons()
        textPrint.tprint(screen, "Number of buttons: {}".format(buttons))
        textPrint.indent()

        for i in range(buttons):
            button = joystick.get_button(i)
            textPrint.tprint(screen,"Button {:>2} value: {}".format(i, button))
            if button == 1:
                start_led.on()
                time.sleep(1)
                start_led.off()
        textPrint.unindent()

        hats = joystick.get_numhats()
        textPrint.tprint(screen, "Number of hats: {}".format(hats))
        textPrint.indent()

        # Hat position. All or nothing for direction, not a float like
        # get_axis(). Position is a tuple of int values (x, y).
        for i in range(hats):
            hat = joystick.get_hat(i)
            textPrint.tprint(screen, "Hat {} value: {}".format(i, str(hat)))
        textPrint.unindent()

        textPrint.unindent()

    #
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    #

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 20 frames per second.
    clock.tick(20)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()