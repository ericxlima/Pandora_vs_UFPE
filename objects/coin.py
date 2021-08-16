import pygame

from objects.game_object import GameObject


class Coin(GameObject):
 
    def __init__(self, position_x= 600, position_y=520, width=40, height=40) -> None:
        """Returns a Coin Object

        Args:
            pos_x (int): Horizontal Position 
            pos_y (int): Vertical Position
            width (int): Width at Coin, relative to screen
            height (int): Heignt at Coin, relative to screen
        """

        #  Basic Properties
        super().__init__(position_x, position_y, width, height)

        #  Moviment Properties
        self._velocity_x = 0
        self._velocity_y = 0
    

    #  Getters and Setters to moviment velocities in axis x and y
    @property
    def vel_x(self):
        return self._velocity_x

    @property
    def vel_y(self):
        return self._velocity_y

    @vel_x.setter
    def vel_x(self, value):
        self._velocity_x = value
    
    @vel_y.setter
    def vel_y(self, value):
        self._velocity_y = value


    def draw(self, screen):
        """ Print in Screen the Coin Object"""
        image =  pygame.image.load('media/coin.png')
        coordinates = self.x, self.y
        screen.blit(image, coordinates)


