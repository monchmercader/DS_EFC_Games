import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
apprun = True


#Game Loop
while apprun:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            apprun = False