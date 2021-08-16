#  Import Dependences
import pygame

#  Import Objects
from objects.pandora import Pandora
from objects.map import Map
from objects.coin import Coin

#  Import Utilities
from scripts.constants import LENGHT_SCREEN_HD
from scripts.colision_mod import Colision_mod


#  Inicialize the Package, and a Screen Title
pygame.init()
pygame.display.set_caption('Pandora vs UFPE')

#  Set the Screen Size 
screen = pygame.display.set_mode(size=LENGHT_SCREEN_HD)

#  For nobody to import this module
if __name__ == '__main__':

    #  Inicialize All Objects
    pandora = Pandora()
    background = Map()
    coin = Coin()
    
    # Objects to the colider detector
    list = [pandora,coin]
    colider = Colision_mod(list) 

    #  Game-Loop
    running = True
    while running:
        #-------------------#
        #  Calculate Rules  #
        #-------------------#
        
        pandora.calculate_rules()
        background.calculate_rules()

        coordinates_pandora = pandora.x, pandora.y
        coordinates_coin = coin.x, coin.y


        #-----------------------#
        #  Print in the Screen  #
        #-----------------------#
        screen.blit(background.draw, (0, 0))
        screen.blit(coin.draw, coordinates_coin)
        screen.blit(pandora.draw, coordinates_pandora)
        pygame.display.update()
        

        #--------------------#
        #  Check all Events  #
        #--------------------#
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                running = False
            
        pandora.event_processor(events)
        
        coliders_events = colider.check_colision()  
        if coliders_events:
            print(coliders_events[0].go1.x)
