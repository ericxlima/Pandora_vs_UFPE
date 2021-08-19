import pygame
import os

# Game inicialization
pygame.init()

# Text renderer
def text_format(message, textFont, textSize, textColor):
    newFont = pygame.font.Font(textFont, textSize)
    newText = newFont.render(message, 0, textColor)

    return newText

black = (0, 0, 0)

# Font
font = "Poppins-Medium.ttf"

# Main menu
def main_menu():
    
    menu = True
    selected_button = "Start"

    while menu:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_button = "Start"
                elif event.key == pygame.K_DOWN:
                    selected_button = "Exit"
                if event.key == pygame.K_RETURN:
                    if selected_button == "Exit":
                        pygame.quit()
                        quit()
                    if selected_button == "Start":
                        print("Start")
                
