import pygame

#Initialize pygame
pygame.init()

#creating screen parameters
screen = pygame.display.set_mode((800,600))
apprun = True
#Defining Clock
clock = pygame.time.Clock()

#Title and Icon
pygame.display.set_caption("EFC Pivot")
icon = pygame.image.load('EssendonFC_A_Icon.png')
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load('EssendonFC_A_logo.png')
playerX = 260
playerY = 200

#Timer
clock = pygame.time.Clock()

counter, text = 10, '10'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('MaisonNeue-Book', 30)
text = font.render("Essendon Football Club", True, (0, 128, 0))

run = False

def player():
    screen.blit(playerImg, (playerX, playerY))

#Game Loop
while not apprun:
    #Screen fill command
    screen.fill((255, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            apprun = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            apprun = True
            
            player()
            screen.blit(font.render(text, True, (0, 0, 0)), (32, 48))
            screen.blit(text,
                (320 - text.get_width() // 2, 240 - text.get_height() // 2 ))

            pygame.display.flip()
            clock.tick(60)

    pygame.display.update()