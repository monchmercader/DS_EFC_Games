import pygame, sys, random
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS

pygame.init()
#Below we are setting up the window size
windowWidth = 640
windowHeight = 480
surface = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Pygame Shapes yey!')
print("Before the first while loop")

while True:
    surface.fill((0,0,0))
    pygame.draw.rect(surface, (255,0,0), (random.randint(0, windowWidth), random.randint(0, windowHeight), 10, 10))

greenSquareX = windowWidth / 2
greenSquareY = windowHeight / 2
print("Before next while loop")
while True:
    surface.fill((0,0,0))
    pygame.draw.rect(surface, (0, 255, 0), (greenSquareX, greenSquareY, 10, 10))
    greenSquareX += 1
    greenSquareY += 1
    pygame.draw.rect(surface, (0, 0, 255),
    (blueSquareX, blueSquareY, 10, 10))

    blueSquareX = 0.0
    blueSquareY = 0.0
    blueSquareVX = 1
    blueSquareVY = 1
print("Right before next while True statement")
while True:
        surface.fill((0,0,0))
        pygame.draw.rect(surface, (0, 0, 255),
        (blueSquareX, blueSquareY, 10, 10))
        blueSquareX += blueSquareVX
        blueSquareY += blueSquareVY
        blueSquareVX += 0.1
        blueSquareVY += 0.1

        for event in GAME_EVENTS.get():
            if event.type == GAME_GLOBALS.QUIT:
                pygame.quit()
                sys.exit()
            pygame.display.update()

pygame.quit()
