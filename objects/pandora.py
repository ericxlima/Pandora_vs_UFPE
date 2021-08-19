#from _typeshed import Self
import pygame

from objects.game_object import GameObject


class Pandora(GameObject):
 
    def __init__(self, position_x=350, position_y=525, width=40, height=60) -> None:
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
        self._jump = 0
        self._jump_pattern = []
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
        """ Print in Screen the Pandora"""
        image =  pygame.image.load('media/pandora.png')
        coordinates = self.x, self.y
        screen.blit(image, coordinates)


    #  Moviments Methods
    def calculate_rules(self):
        #  Left limit of Map
        if self.x <= 0:
            self.x += 1
        #  Right limit of Map
        elif self.x >= 1245:
            self.x -= 1
        else:
            self.x += self.vel_x
        
        #  Floor limit of Map
        if self.y >= 525:
            self.y -= 1
        else:
            self.y += self.vel_y
    

    def event_processor(self, events):
        if self._jump > 0:
            self.jump(-20)# jump height negative because gamepy
        for event in events:            
            #  While the user presses the key
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.vel_x = -5
                if event.key == pygame.K_UP:
                    self.jumppattern(20) #jump frame precision
                    self._jump = 20 # jump height
                if event.key == pygame.K_RIGHT:
                    self.vel_x = 5
                if event.key == pygame.K_DOWN:
                    #  For not to enter the floor
                    if self.y < 510:
                        self.vel_y = 5
            
            # If the user drop a key
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.vel_x = 0
                #if event.key == pygame.K_UP:
                   # self.vel_y = 0
                if event.key == pygame.K_RIGHT:
                    self.vel_x = 0
                if event.key == pygame.K_DOWN:
                    self.vel_y = 0

    def jumppattern(self,c):
        a = -1
        b = 0
        c = 20
        x1 = (-b + (- 4*a*c)**(1/2)) / (2*a)
        x2 = (-b - (- 4*a*c)**(1/2)) / (2*a)
        x = ( x2 - x1 )
        list = []
        for i in range(21):
            list.append(x*i/20 + x1)
        self._jump_pattern = list

    def jump(self,height):
        # y = -x^2 + hight          
        if self._jump < 21 and self._jump > 10:
            self._jump -= 1
            x = self._jump_pattern[self._jump]
            y = -1*(x*x) + height
            self.y += y
        elif self._jump < 11 and self._jump > 0:
            self._jump -= 1
            x = self._jump_pattern[self._jump]
            y = -1*(x*x) + height
            if (self.y - y) < 530:
                self.y -= y
            else:
                self.y = 530
                self._jump = 0 #jump ended
        

