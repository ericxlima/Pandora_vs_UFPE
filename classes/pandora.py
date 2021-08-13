import pygame

from classes.game_object import GameObject


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
        self._velocity = 10
    

    #  Getters to consult this properties
    @property
    def v(self):
        return self._velocity

    #  Pandora for Screen
    @property
    def draw(self):
        """ To Use with screen.blit()"""
        return pygame.image.load('media/pandora.png')


    #  Moviments Methods
    def calculate_rules(self):
        pass
    

    def event_processor(self, events):
        for event in events:

            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_LEFT:
                    self.x -= self.v
                
                if event.key == pygame.K_UP:
                    self.y -= self.v

                if event.key == pygame.K_RIGHT:
                    self.x += self.v

                if event.key == pygame.K_DOWN:
                    self.y += self.v

