from scripts.constants import WHITE
from objects.game_object import GameObject

import pygame


class Button(GameObject):

    def __init__(self, position_x=0, position_y=0, width=0, height=75, name=None, color=WHITE) -> None:
        super().__init__(position_x=position_x, position_y=position_y, width=width, height=height, name=name)
        
        self._color = color


    #  Create Getter and Setter for Color
    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value


    #  Draw in Screen
    def draw_retangle(self, screen):
        size = self.w, self.h
        position = self.x, self.y
        
        retangle = pygame.Surface(size)
        #  Add transparency in retangle
        retangle.set_alpha(150)
        retangle.fill(self.color)
        screen.blit(retangle, position)
        