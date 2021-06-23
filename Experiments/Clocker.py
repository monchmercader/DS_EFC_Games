import pygame

pygame.init()

screen = pygame.display.set_mode( (1024,768) )

font = pygame.font.Font('DSEG14Modern-Regular.ttf', 70)
clock = pygame.time.Clock()

start_time = pygame.time.get_ticks() 

paused  = False
running = True

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
        counting_time = pygame.time.get_ticks() - start_time
        county = round(counting_time, 2)

        # change milliseconds into minutes, seconds, milliseconds
        #screen.fill( (0,0,0) )
        counting_minutes = str(county/6).zfill(1)
        counting_seconds = str((county%6)/1 ).zfill(1)
        counting_millisecond = str(county%1).zfill(1)
        #counting_string = "%s:%s:%s" % (counting_minutes, counting_seconds, counting_millisecond)
        counting_string = "%s:%s" % (counting_minutes, counting_seconds)

        counting_text = font.render(str(counting_string), 1, (117,255,255))
        #counting_rect = counting_text.get_rect(center = screen.get_rect().center)

    screen.fill( (0,0,0) )
    screen.blit(counting_text, (15,15))
  
    pygame.display.update()

    clock.tick(60)