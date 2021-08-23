import pygame

from objects.game_object import GameObject


class Coin(GameObject):
 
    def __init__(self, position_x= 600, position_y=520, width=40, height=40, name='') -> None:
        """Returns a Coin Object

        Args:
            pos_x (int): Horizontal Position 
            pos_y (int): Vertical Position
            width (int): Width at Coin, relative to screen
            height (int): Heignt at Coin, relative to screen
        """

        #  Basic Properties
        super().__init__(position_x, position_y, width, height, name)

        #  Moviment Properties
        self._velocity_y = 5
    

    #  Getters and Setters to moviment velocities in axis x and y
    @property
    def vel_y(self):
        return self._velocity_y
    
    @vel_y.setter
    def vel_y(self, value):
        self._velocity_y = value


    def draw(self, screen):
        """ Print in Screen the Coin Object"""
        image =  pygame.image.load(f'media/level_1/{self.name}.png')
        coordinates = self.x, self.y
        screen.blit(image, coordinates)
    
    def calculate_rules(self):
        self.y += self.vel_y

        if self.y == 520:
            self.vel_y = 0
        


