import pygame

from objects.game_object import GameObject


class Pandora(GameObject):
 
    def __init__(self, position_x=400, position_y=320, width=40, height=60) -> None:
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


    #  Moviments Methods
    def calculate_rules(self):
        self.x += self.vel_x
        self.y += self.vel_y
    

    def event_processor(self, events):
        for event in events:
            #  While the user presses the key
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.vel_x = -1
                if event.key == pygame.K_UP:
                    self.vel_y = -1
                if event.key == pygame.K_RIGHT:
                    self.vel_x = 1
                if event.key == pygame.K_DOWN:
                    self.vel_y = 1
            
            # If the user drop a key
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.vel_x = 0
                if event.key == pygame.K_UP:
                    self.vel_y = 0
                if event.key == pygame.K_RIGHT:
                    self.vel_x = 0
                if event.key == pygame.K_DOWN:
                    self.vel_y = 0

