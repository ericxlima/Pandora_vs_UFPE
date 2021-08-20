from pygame.event import pump
from objects.menu_background import Map
import pygame
import main

from scripts.constants import GREEN, RED, LENGHT_SCREEN_HD

from scripts.text import create_button, text_format


# Game inicialization
pygame.init()


screen = pygame.display.set_mode(size=LENGHT_SCREEN_HD)

#  Buttons
selected_button = None

background_menu = Map()

running_menu = True
while running_menu:

    #-----------------------#
    #  Print in the Screen  #
    #-----------------------#

    background_menu.draw(screen)

    create_button(screen=screen, position=(366, 400), image_path='start_button')
    create_button(screen=screen, position=(685, 400), image_path='exit_button')

    if selected_button == 'Start':
        create_button(screen=screen, position=(366, 400), size=(220, 90), color=GREEN)
    elif selected_button == 'Exit':
        create_button(screen=screen, position=(685, 400), size=(220, 90), color=RED)

    pygame.display.update()
    
    #--------------------#
    #  Check all Events  #
    #--------------------#
    events = pygame.event.get()
    for event in events:

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        
        if event.type == pygame.KEYDOWN:
            #  Modify user choice
            if event.key == pygame.K_LEFT:
                selected_button = "Start"
                
            elif event.key == pygame.K_RIGHT:
                selected_button = "Exit"
            
            #  Make Action with key ENTER
            if event.key == pygame.K_RETURN:
                selected_button = "Enter"


    
    print(selected_button)
            
            
            
                
