import pygame

pygame.init()

window = pygame.display.set_mode((1280, 720))
title = pygame.display.set_caption("Pandora Vs UFPE")

background = pygame.image.load("Assets/Scenary/background.png")
pandora = pygame.image.load("Assets/Pandora/Pandora1.png")
block = pygame.image.load("Assets/Objects/block-error.png")
pandora_x = 0
pandora_y = 500
pandora_moveup = False
pandora_movedown = False
pandora_moveleft = False
pandora_moveright = False

def move_pandora():
    global pandora_y  
    global pandora_x 
    global pandora_moveleft
    global pandora_moveright

    if pandora_moveup:
        pandora_y -= 2
    else:
        pandora_y += 0

    if pandora_movedown:
        pandora_y += 2
    else:
        pandora_y += 0

    if pandora_moveleft:
        pandora_x += 2
    else:
        pandora_x += 0

    if pandora_moveright:
        pandora_x -= 2
    else:
        pandora_x += 0


def drawn():
    window.blit(background, (pandora_x, 0))
    window.blit(block, (pandora_x+1000, 420))
    window.blit(pandora, (20, pandora_y))
    



loop = True

while loop:
    pygame.display.update()

    for events in pygame.event.get():

        if events.type == pygame.QUIT:
            loop = False

        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_UP:
                pandora_moveup = True
            if events.key == pygame.K_DOWN:
                pandora_movedown = True
            if events.key == pygame.K_LEFT:
                pandora_moveleft = True
            if events.key == pygame.K_RIGHT:
                pandora_moveright = True

        if events.type == pygame.KEYUP:
            if events.key == pygame.K_UP:
                pandora_moveup = False
            if events.key == pygame.K_DOWN:
                pandora_movedown = False
            if events.key == pygame.K_LEFT:
                pandora_moveleft = False
            if events.key == pygame.K_RIGHT:
                pandora_moveright = False

    drawn()
    move_pandora()

    pygame.display.update()