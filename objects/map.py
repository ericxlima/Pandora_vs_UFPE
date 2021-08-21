import pygame

from objects.game_object import GameObject


class Map(GameObject):

    def __init__(self, position_x=0, position_y=0, width=6400, height=720, name='big_bg') -> None:
        """Create a map object 5 times larger than the screen in width,
           with functionality for Parallax effect
        Args:
            position_x (int, optional): Horizontal Position. Defaults to 0.
            position_y (int, optional): Vertical Position. Defaults to 0.
            width (int, optional): Width at Map, relative to screen. Defaults to 6400.
            height (int, optional): Height at Pandora, relative to screen. Defaults to 720.
        """

        #  Load basic Superclass properties 
        super().__init__(position_x=position_x,
                         position_y=position_y, 
                         width=width, 
                         height=height, 
                         name=name)
        
        #  Moviment Properties
        self._velocity_x = 0
    

    #  Getters and Setters to moviment velocities in axis x
    @property
    def vel_x(self):
        return self._velocity_x

    @vel_x.setter
    def vel_x(self, value):
        self._velocity_x = value

    def draw(self, screen):
        """ Print in Screen the Coin Object"""
        image =  pygame.image.load(f'media/{self.name}.png')
        coordinates = self.x, self.y
        screen.blit(image, coordinates)


    #  Moviments Methods
    def calculate_rules(self):
        self.x += self.vel_x
        self.vel_x = 0
    

    def event_processor(self, events):
        for event in events:
            #  While the user presses the key
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.vel_x = 5
            
            # If the user drop a key
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.vel_x = 0