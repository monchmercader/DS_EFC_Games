import pygame

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
#Defining the clock
clock = pygame.time.Clock()
done = False
counter, c_text = 5, '5'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)

#Title and Icon
pygame.display.set_caption("EFC Pivot")
icon = pygame.image.load('EssendonFC_A_Icon.png')
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load('EssendonFC_A_logo.png')
playerImg = pygame.transform.scale(playerImg, (220, 220))
playerX = 880
playerY = 70

#Define the Font and text to render
font = pygame.font.SysFont('MaisonNeue-Book', 75)
counterfont = pygame.font.Font('DSEG14Modern-Regular.ttf', 180)
text = font.render("Essendon Football Club Pivot Game", True, (0, 0, 0))

def player():
    screen.blit(playerImg, (playerX, playerY))

while not done:
    for event in pygame.event.get():
        counter -= 1
        c_text = str(counter).rjust(2)
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True

    screen.fill((0, 101, 177))
    screen.blit(text, (950- text.get_width() // 2, 320 - text.get_height() // 2))
    player()
    screen.blit(counterfont.render(c_text, True, (0, 0, 0)), (640, 520))
    pygame.display.flip()
    clock.tick(60)