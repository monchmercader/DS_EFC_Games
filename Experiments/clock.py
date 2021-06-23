import pygame
pygame.init()
screen = pygame.display.set_mode((480, 480))
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks() 

paused  = False
running = True

counter, text = 60, '60'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.Font('DSEG14Modern-Regular.ttf', 70)

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

        # change milliseconds into minutes, seconds, milliseconds
        counting_minutes = str(counting_time/60000).zfill(2)
        counting_seconds = str( (counting_time%60000)/1000 ).zfill(2)
        counting_millisecond = str(counting_time%1000).zfill(3)

        counting_string = "%s:%s:%s" % (counting_minutes, counting_seconds, counting_millisecond)

        counting_text = font.render(str(counting_string), 1, (0,255,255))
        counting_rect = counting_text.get_rect(center = screen.get_rect().center)

screen.fill( (0,0,0) )
screen.blit(counting_text, counting_rect)

pygame.display.update()

clock.tick(25)

#while run:
#    for e in pygame.event.get():
#        if e.type == pygame.USEREVENT:
#            counter -= 1
#            text = str(counter).rjust(3) if counter > 0 else 'boom!'
#            if e.type == pygame.QUIT:
#                run = False
#                screen.fill((0, 0, 0))
#                screen.blit(font.render(text, True, (255, 0, 0)), (32, 48))
#                pygame.display.flip()
#                clock.tick(60)