from classes.pandora import Pandora
import pygame

from scripts.constants import LENGHT_SCREEN_MEDIUM


#  Inicialize the Package, and a Screen Title
pygame.init()
pygame.display.set_caption('Pandora vs UFPE')

#  Set the Screen Size, and load the background 
screen = pygame.display.set_mode(size=LENGHT_SCREEN_MEDIUM)
background = pygame.image.load('media/bg_geral.png')

#  For not to import this module
if __name__ == '__main__':
    
    #  Inicialize Pandora
    pandora = Pandora()

    #  Game-Loop
    running = True
    while running:

        #  Calculate Rules:
        coordinates = pandora.x, pandora.y

        #  Print in the Screen
        screen.blit(background, (0, 0))
        screen.blit(pandora.draw, coordinates)
        pygame.display.update()
        
        #  Check the Events

        events = pygame.event.get()
        
        for event in events:
            if event.type == pygame.QUIT:
                running = False
        
        pandora.event_processor(events)

# Ana Carla