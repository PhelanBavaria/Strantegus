

import os
import pygame
from pygame.locals import RLEACCEL

gfx_path = os.path.join(os.getcwd(), 'gfx')

def load_image(name, colorkey=None):
    path = os.path.join(gfx_path, name)
    try:
        image = pygame.image.load(path)
    except pygame.error:
        print('Cannot load image:', path)
        return 'test'
    #image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image.convert()