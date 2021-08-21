from scripts.constants import GREEN, RED, WHITE
import pygame

from objects.map import Map
from objects.button import Button


class Menu:

    def __init__(self) -> None:
        self._choice = None
        self._selected_button = None
    
    #  Define Getters and Setters 
    @property
    def selected_button(self):
        return self._selected_button
    
    @property
    def choice(self):
        return self._choice
        
    @selected_button.setter
    def selected_button(self, value):
        self._selected_button = value
    
    @choice.setter
    def choice(self, value):
        self._choice = value

    #  Print in Screen
    def draw(self, screen):
        background = Map(name='menu/background-menu')
        background.draw(screen)

        button = Button()

        #  Calculate Rules for Selected Button 
        if self.selected_button == 'Start':
            button.x, button.y = 376, 400
            button.color = GREEN
            
        elif self.selected_button == 'Exit':
            button.x, button.y = 695, 400
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
    
            