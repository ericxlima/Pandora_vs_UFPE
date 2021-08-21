#  Import Dependences
import pygame

#  Import Objects
from objects.pandora import Pandora
from objects.map import Map
from objects.coin import Coin
from objects.mage import Mage
from objects.menu import Menu

#  Import Utilities
from scripts.constants import LENGHT_SCREEN_HD, RED, WHITE
from scripts.colision_mod import Colision_mod


#  Inicialize the Package, and a Screen Title
pygame.init()
pygame.display.set_caption('Pandora vs UFPE')
icon = pygame.image.load('media/venus_space.png')
pygame.display.set_icon(icon)

#  Set the Screen Size 
screen = pygame.display.set_mode(size=LENGHT_SCREEN_HD)


#moves every objects 
def move_obj(objs,location_x,location_y):
    for i in objs:
        i.x += location_x
        i.y += location_y

#  For nobody to import this module
if __name__ == '__main__':

    #  Inicialize All Objects
    pandora = Pandora()
    background = Map()
    mage = Mage()
    menu = Menu()

    #======================== border controls=============
    scroll = 0 #border left wall: 0 for left border and  1200 for right border
    right_border = 1200
    left_border = 0
    speed = 5
    moveble_objs = [pandora,background] #objs to be moved
    
    #=====================================================
    # Objects to the colider detector
    list_objs = [pandora]  
    colider = Colision_mod(list_objs) 

    coins = []

    #  Game-Loop
    running = True
    while running:
        #--------------------#
        #  For exit Menu     #
        #--------------------#
        if menu.choice == 'Start':
            print('Startou mermo')
        if menu.choice == 'Exit':
            print('Sai')

        #--------------------#
        #      Drop Coin     #
        #--------------------#

        if mage.drop_coin:
            coin = Coin(position_x=mage.x,
                        position_y=mage.y)
            coins.append(coin)

        #--------------------#
        # frame rate control #
        #--------------------#
        time = pygame.time.get_ticks()
        pygame.time.delay(1)

        #-------------------#
        #  Calculate Rules  #
        #-------------------#
        pandora.calculate_rules()
        background.calculate_rules()
        mage.calculate_rules()

        for coin in coins:
            coin.calculate_rules()


        #-----------------------#
        #  Print in the Screen  #
        #-----------------------#
        #background.draw(screen)
        #pandora.draw(screen)
        #mage.draw(screen)
        menu.draw(screen)

        for coin in coins:
            coin.draw(screen)
        
        pygame.display.update()

        

        #--------------------#
        #  Check all Events  #
        #--------------------#
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                running = False

            else:
                menu.event_processor(event)
            
        pandora.event_processor(events)

        #-------------------#
        #     Border        #
        #-------------------#
        if pandora.x < 20 and scroll>left_border:
            scroll += -speed
            move_obj(moveble_objs,speed,0)
        elif pandora.x > (1280//2) - 20 and scroll<right_border:
            scroll += speed
            move_obj(moveble_objs,-speed,0)

        #-------------------#
        #     Colisions     #
        #-------------------#
        coliders_events = colider.check_colision()  
        clock = pygame.time.get_ticks() -time
        wait = 10-clock
        if wait>0:
            pygame.time.delay(wait)# frame rate control

        #print(wait)
        #if len(coliders_events)>0:
        #print("fps: " + str(int(6000/(pygame.time.get_ticks() - x))))

                    

