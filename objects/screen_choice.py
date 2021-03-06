from os import name
from scripts.constants import GREEN, RED
import pygame

from objects.map import Map
from objects.button import Button


class ScreenChoice:

    def __init__(self, name) -> None:
        self._choice = None
        self._selected_button = None
        self._name = name
    
    #  Define Getters and Setters 
    @property
    def selected_button(self):
        return self._selected_button
    
    @property
    def choice(self):
        return self._choice

    @property
    def name(self):
        return self._name
        
    @selected_button.setter
    def selected_button(self, value):
        self._selected_button = value
    
    @choice.setter
    def choice(self, value):
        self._choice = value

    @name.setter
    def name(self, value):
        self._choice = None
        self._name = value

    #  Print in Screen
    def draw(self, screen):
        # Load Menu Interface
        if self.name == "Menu":
            background = Map(name='menu/background-menu')
            background.draw(screen)

        # Load Game Over Win Interface
        elif self.name == "Win":
            background = Map(name='menu/GAME-OVER-SCREEN-1')
            background.draw(screen)
        
        # Load Game Over Lose Interface
        elif self.name == "Lose":
            background = Map(name='menu/GAME-OVER-SCREEN-1')
            background.draw(screen)

        # Load Button Images
        play_again_image = Button(position_x=376, position_y=400, image_path='menu/start_button')
        play_again_image.draw_image(screen=screen)
        exit_image = Button(position_x=695, position_y=400, image_path='menu/exit_button')
        exit_image.draw_image(screen=screen)

        
        # Load Button Menu
        button = Button()

        #  For all buttons selecteds
        if self.selected_button:
            button.w, button.h = 205, 75
        
        #  Calculate Rules for Selected Button
        if self.selected_button == 'Start':
            button.x, button.y = 385, 400
            button.color = GREEN
        elif self.selected_button == 'Exit':
            button.x, button.y = 705, 400
            button.color = RED
        
        button.draw_retangle(screen)


    def event_processor(self, event):        
        if event.type == pygame.KEYDOWN:
            #  Modify user choice
            if event.key == pygame.K_LEFT:
                self.selected_button = "Start"
                
            elif event.key == pygame.K_RIGHT:
                self.selected_button = "Exit"
            
            #  Make Action with key ENTER
            if event.key == pygame.K_RETURN:
                self.choice = self.selected_button
    
            