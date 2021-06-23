import pygame
pygame.init()
#Below we are setting up the window size
window = pygame.display.set_mode((640, 480))
while True:
        #We're creating an rectangle with the (colour values), and (x, y, start, width height)
        pygame.draw.rect(window, (255,0,255),
                                (0, 0, 50, 50))
        pygame.draw.rect(window, (0,255,0),
                                (40, 0, 50, 50))
        pygame.draw.rect(window, (0,0,255),
                                (80, 0, 50, 50))
        pygame.draw.circle(window, (255,0,0), (200, 200), 20, 0)
        pygame.draw.line(window, (255,255,255), (50, 50), (75, 75), 1)
        pygame.draw.line(window, (255,255,255), (75, 75), (25, 75), 1)
        pygame.draw.line(window, (255,255,255), (25, 75), (50, 50), 1)

        pygame.display.update()
