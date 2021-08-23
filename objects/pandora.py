#from _typeshed import Self
import pygame

pygame.mixer.init()

from objects.game_object import GameObject

jumpSound = pygame.mixer.Sound("media/music/jumpsound.ogg")
#pygame.mixer.jumpSound.play(-1)


class Pandora(GameObject):

    pandora_right = [pygame.image.load('media/pandora/pandora-right1.png'),
                    pygame.image.load('media/pandora/pandora-right2.png'),
                    pygame.image.load('media/pandora/pandora-right3.png'),
                    pygame.image.load('media/pandora/pandora-right4.png')]

    pandora_left = [pygame.image.load('media/pandora/pandora-left1.png'),
                    pygame.image.load('media/pandora/pandora-left2.png'),
                    pygame.image.load('media/pandora/pandora-left3.png'),
                    pygame.image.load('media/pandora/pandora-left4.png')]

    pandora_right_jump = [pygame.image.load('media/pandora/pandora-right-jump2.png'),
                         pygame.image.load('media/pandora/pandora-right-jump3.png'),
                         pygame.image.load('media/pandora/pandora-right-jump4.png')]
    
    pandora_left_jump = [pygame.image.load('media/pandora/pandora-left-jump2.png'),
                         pygame.image.load('media/pandora/pandora-left-jump3.png'),
                         pygame.image.load('media/pandora/pandora-left-jump4.png')]
 
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

        # News moviments
        
        self._right = False
        self._left = False
        self._step_index = 0

    #  Getters and Setters to moviment velocities in axis x and y
    @property
    def vel_x(self):
        return self._velocity_x

    @property
    def vel_y(self):
        return self._velocity_y

    @property
    def move_right(self):
        return self._right

    @property
    def move_left(self):
        return self._left
    
    @property
    def step(self):
        return self._step_index

    @vel_x.setter
    def vel_x(self, value):
        self._velocity_x = value
    
    @vel_y.setter
    def vel_y(self, value):
        self._velocity_y = value
    
    @move_right.setter
    def move_right(self, value):
        self._right = value
    
    @move_left.setter
    def move_left(self, value):
        self._right = value

    @step.setter
    def step(self, value):
        self._step_index = value


    def draw(self, screen):
        """ Print in Screen the Pandora"""
        #Pandora stoped

        image = pygame.image.load('media/pandora/pandora-right1.png')

        if self.vel_x == 0 and self.move_right:
            image = pygame.image.load('media/pandora/pandora-right1.png')
        elif self.vel_x == 0 and self.move_left:
            image = pygame.image.load('media/pandora/pandora-left1.png')
        else:
            if self.move_right:
                print(self.step)
                image = self.pandora_right[self.step]
            if self.move_left:
                print(self.step)
                image = self.pandora_left[self.step]

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
            if self.step == 3:
                self.step = 0
            else:
                self.step += 1
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
                    self.move_left = True
                    self.move_right= False
                    self.vel_x = -5
                if event.key == pygame.K_UP:
                    jumpSound.play()
                    if self._jump == 0:
                        self.jumppattern(20) #jump frame precision
                        self._jump = 14 # jump height
                if event.key == pygame.K_RIGHT:
                    self.move_left = False
                    self.move_right= True
                    self.vel_x = 5
                    
            
            # If the user drop a key
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.move_left = False
                    self.step = 0
                    self.vel_x = 0
                #if event.key == pygame.K_UP:
                   # self.vel_y = 0
                if event.key == pygame.K_RIGHT:
                    self.move_right = False
                    self.step = 0
                    self.vel_x = 0

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
        

