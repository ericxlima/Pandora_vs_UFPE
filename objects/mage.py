import pygame

from objects.game_object import GameObject

class Mage(GameObject):

    def __init__(self, position_x=500, position_y=30, width=180, height=120, name='Mage') -> None:
        super().__init__(position_x=position_x, position_y=position_y, width=width, height=height, name=name)

        self._velocity_x = 5

    @property
    def vel_x(self):
        return self._velocity_x
    
    @vel_x.setter
    def vel_x(self, value):
        self._velocity_x = value
    

    def draw(self, screen):
        image =  pygame.image.load('media/level_1/mage.png')
        coordinates = self.x, self.y
        screen.blit(image, coordinates)

    def calculate_rules(self):
        self.x += self.vel_x

        if self.x >= 1100:
            self.vel_x = -self.vel_x
        if self.x <= 0:
            self.vel_x = abs(self.vel_x)