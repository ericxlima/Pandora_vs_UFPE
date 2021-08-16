import pygame

from objects.pandora import Pandora
from objects.map import Map
from objects.coin import Coin
from scripts.constants import LENGHT_SCREEN_HD
from scripts.colision_mod import Colision_mod
from scripts.colision import Colision
from scripts.vector2 import Vector2

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
    coin = Coin()
    list = [pandora,coin]
    colider = Colision_mod(list) #objs to the colider detector

    #  Game-Loop
    running = True
    while running:

        #  Calculate Rules for print Pandora in other coordinates:


        #  Check the Events
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                running = False
            
        pandora.event_processor(events)

        pandora.calculate_rules()
        background.calculate_rules()

        coordinates = pandora.x, pandora.y
        #print(coordinates)

        #  Print in the Screen
        screen.blit(background.draw, (0, 0))
        screen.blit(coin.draw,(350,510))
        screen.blit(pandora.draw, coordinates)
        pygame.display.update()

        coliders_events = colider.check_colision()  
        if( len(coliders_events)):
            print(coliders_events[0].go1.x)

#dale