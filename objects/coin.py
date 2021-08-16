import pygame

from objects.game_object import GameObject


class Coin(GameObject):
 
    def __init__(self, position_x=350, position_y=510, width=40, height=60) -> None:
        """Returns Pandora Object

        Args:
            pos_x (int): Horizontal Position 
            pos_y (int): Vertical Position
            width (int): Width at Pandora, relative to screen
            height (int): Heignt at Pandora, relative to screen
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


    #  Getter for Print Pandora in Screen
    @property
    def draw(self):
        """ To Use with screen.blit()"""
        return pygame.image.load('media/pandora.png')


