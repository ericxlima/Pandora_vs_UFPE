import pygame

from objects.pandora import Pandora
from objects.map import Map

from scripts.constants import LENGHT_SCREEN_HD


#  Inicialize the Package, and a Screen Title
pygame.init()
pygame.display.set_caption('Pandora vs UFPE')

#  Set the Screen Size 
screen = pygame.display.set_mode(size=LENGHT_SCREEN_HD)


#  For nobody to import this module
if __name__ == '__main__':

    #  Inicialize Pandora and Map
    pandora = Pandora()
    background = Map()

    #  Game-Loop
    running = True
    while running:

        #  Calculate Rules for print Pandora in other coordinates:
        pandora.calculate_rules()
        background.calculate_rules()
        
        coordinates = pandora.x, pandora.y
        print(coordinates)

        #  Print in the Screen
        screen.blit(background.draw, (0, 0))
        screen.blit(pandora.draw, coordinates)
        pygame.display.update()

        #  Check the Events
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                running = False
            
        pandora.event_processor(events)
  
#dale