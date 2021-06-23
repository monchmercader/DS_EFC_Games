import time, pygame

pygame.init()

screen = pygame.display.set_mode( (1024,768) )
clock = pygame.time.Clock()
sec_val = 0
font = pygame.font.Font('DSEG14Modern-Regular.ttf', 70)

start_time = pygame.time.get_ticks() 

paused  = False
running = True


def time_convert(sec):
    global clock
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins), round((sec), 2)))
    #print("Time Lapsed = {1}:{2}".format(int(mins), round((sec), 2)))
    #sec_val = (int(hours),int(mins), round((sec), 2))
    sec_val = (round((sec), 2))
    counting_text = font.render(str(sec_val), 1, (117,255,255))
    counting_rect = counting_text.get_rect(center = screen.get_rect().center)
    screen.fill( (0,0,0) )
    screen.blit(counting_text, (15,40))
    
    pygame.display.update()

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
            #counting_time = pygame.time.get_ticks() - start_time
            #county = round(counting_time, 2)
            end_time = time.time()
            time_lapsed = end_time - start_time
            sec_val = time_convert(time_lapsed)
            
    clock.tick(60)