import pygame


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
