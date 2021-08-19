import pygame

from scripts.constants import LENGHT_SCREEN_HD
from scripts.constants import BLACK

# Game inicialization
pygame.init()

# Text renderer
def text_format(message=None, size=None, color=None):
    """Treat text and it return
    Args:
        message (str, optional): Mensage to show in screen. Defaults to None.
        size (int, optional): Size of Text. Defaults to None.
        color (tuple, optional): Color of text. Defaults to None.
    Returns:
        Font: Font to rendering
    """
    font = "Poppins-Medium.ttf"

    new_font = pygame.font.Font(font, size=size)
    new_text = new_font.render(text=message, 
                             antialias=False,
                             color=color)

    return new_text

    
screen = pygame.display.set_mode(size=LENGHT_SCREEN_HD)
menu = True
selected_button = "Start"

while menu:

    #-----------------------#
    #  Print in the Screen  #
    #-----------------------#

    image =  pygame.image.load('media/big_bg.png')
    coordinates = (0, 0)
    screen.blit(image, coordinates)
    screen.update()
    
    #--------------------#
    #  Check all Events  #
    #--------------------#
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
                
