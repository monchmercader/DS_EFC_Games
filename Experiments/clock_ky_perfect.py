import sys, time, pygame

pygame.init()

screen = pygame.display.set_mode( (1024,240) )

# Set Pygame refresh rate variable = clock 
clock = pygame.time.Clock()
sec_val = 0
counterfont = pygame.font.Font('DSEG14Modern-Regular.ttf', 70)
sec = 0
mins = 0
hours = 0
# Start the clock
start_time = pygame.time.get_ticks() 

# Status variables
paused  = False
running = True

# Function to compute for a HH:MM:SS:MS based stopwatch

def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60    
    mins = mins % 60
    sec_val = ("{0}:{1}:{2}".format(int(hours), int(mins), round((sec), 2)))
    counting_text = counterfont.render(str(sec_val), 3, (134,145,255))
    counting_rect = counting_text.get_rect(left = screen.get_rect().left)
    screen.fill( (0,0,0) )
    screen.blit(counting_text, (300,40))
    pygame.display.update()
    
# Setup Pygame refresh rate to 120 fps
clock.tick(120)
start_time = time.time()

while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            if event.key == pygame.K_SPACE:
                paused = not paused 
    
    if not paused:
            end_time = time.time()
            time_lapsed = end_time - start_time
            sec_val = time_convert(time_lapsed)
            
sys.exit()