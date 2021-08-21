from scripts.constants import WHITE
from objects.game_object import GameObject

import pygame


class Button(GameObject):

    def __init__(self, position_x=0, position_y=0, width=0, height=0, name=None, color=WHITE, image_path=None) -> None:
        super().__init__(position_x=position_x, position_y=position_y, width=width, height=height, name=name)
        
        self._color = color
        self._image_path = image_path

    #  Create Getter and Setter for Color
    @property
    def color(self):
        return self._color

    @property
    def image_path(self):
        return self._image_path

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

    
    #  Draw Image
    def draw_image(self, screen):
        image = pygame.image.load(f'media/{self.image_path}.png')
        coordinates = self.x, self.y
        screen.blit(image, coordinates)
        