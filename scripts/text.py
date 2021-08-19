import pygame
from pygame import color
from pygame import surface
from pygame.constants import WINDOWHITTEST


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

    font = pygame.font.Font(font, size=size)
    new_text = font.render(text=message, 
                             antialias=False,
                             color=color)

    return new_text



def create_button(screen=None, size=None, position=None, image_path=None, color=None):
    """[summary]

    Args:
        screen ([type], optional): [description]. Defaults to None.
        size ([type], optional): Retangle size (x, y). Defaults to None.
        position ([tuple], optional): [description]. Defaults to None.
        imagem ([type], optional): [description]. Defaults to None.
    """
    if image_path:
        image = pygame.image.load(f'media/{image_path}.png')
        screen.blit(image, position)
    if size:
        square = pygame.Surface(size)
        square.set_alpha(150)
        square.fill(color)
        
        screen.blit(square, position)