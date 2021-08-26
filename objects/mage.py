import pygame
from objects.game_object import GameObject


class Mage(GameObject):

    def __init__(self, position_x=500, position_y=30, width=180, height=120, name='Mage') -> None:
        super().__init__(position_x=position_x, position_y=position_y, width=width, height=height, name=name)

        self._velocity_x = 5
        self._walking = 0
        self._drop_coin_gold = False
        self._drop_coin_red = False
        self._coins_dropped = 0

    @property
    def vel_x(self):
        return self._velocity_x
    
    @property
    def walking(self):
        return self._walking
    
    @property
    def drop_coin_gold(self):
        return self._drop_coin_gold

    @property
    def drop_coin_red(self):
        return self._drop_coin_red
    
    @property
    def coins_dropped(self):
        return self._coins_dropped
    
    @vel_x.setter
    def vel_x(self, value):
        self._velocity_x = value
    
    @walking.setter
    def walking(self, value):
        self._walking = value
    
    @drop_coin_gold.setter
    def drop_coin_gold(self, value):
        self._drop_coin_gold = value
    
    @drop_coin_red.setter
    def drop_coin_red(self, value):
        self._drop_coin_red = value
    
    @coins_dropped.setter
    def coins_dropped(self, value):
        self._coins_dropped = value
    
    

    def draw(self, screen):
        image =  pygame.image.load('media/level_1/mage.png')
        coordinates = self.x, self.y
        screen.blit(image, coordinates)

    def calculate_rules(self):
        self.x += self.vel_x
        self.walking += abs(self.vel_x)
        self.drop_coin_gold = False
        self.drop_coin_red = False

        if self.x >= 1100:
            self.vel_x = -self.vel_x
        elif self.x <= 0:
            self.vel_x = abs(self.vel_x)
        
    
        # Limit the amount of coins
        if self.coins_dropped < 10:
            if self.walking == 410:
                self.walking = 0
                self.drop_coin_gold = True
                self.coins_dropped += 1
            if self.walking == 205:
                self.drop_coin_red = True
            
                

