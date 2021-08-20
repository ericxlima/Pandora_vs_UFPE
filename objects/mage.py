from typing import Counter
import pygame
from pygame.constants import DROPBEGIN

from objects.game_object import GameObject
from objects.coin import Coin

class Mage(GameObject):

    def __init__(self, position_x=500, position_y=30, width=180, height=120, name='Mage') -> None:
        super().__init__(position_x=position_x, position_y=position_y, width=width, height=height, name=name)

        self._velocity_x = 5
        self._counter = 0
        self._drop_coin = True

    @property
    def vel_x(self):
        return self._velocity_x
    
    @property
    def counter(self):
        return self._counter
    
    @property
    def drop_coin(self):
        return self._drop_coin
    
    @vel_x.setter
    def vel_x(self, value):
        self._velocity_x = value
    
    @counter.setter
    def counter(self, value):
        self._counter = value
    
    @drop_coin.setter
    def drop_coin(self, value):
        self._drop_coin = value
    
    

    def draw(self, screen):
        image =  pygame.image.load('media/level_1/mage.png')
        coordinates = self.x, self.y
        screen.blit(image, coordinates)

    def calculate_rules(self):
        self.x += self.vel_x
        self.counter += abs(self.vel_x)
        self.drop_coin = False

        if self.x >= 1100:
            self.vel_x = -self.vel_x
        elif self.x <= 0:
            self.vel_x = abs(self.vel_x)
        
        if self.counter == 205:
            self.counter = 0
            self.drop_coin = True

