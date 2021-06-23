
import pygame

pygame.init()
window = pygame.display.set_mode((500, 400))

while True:
    pygame.display.update()

while True:
    pygame.draw.line(window, (255,255,255), (0, 0), (500, 400), 1)
    pygame.display.update()
