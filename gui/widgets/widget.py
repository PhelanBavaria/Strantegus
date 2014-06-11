

import pygame


class Widget(pygame.sprite.Sprite):
    __slots__ = []

    def __init__(self, gui, position, size=(50, 25)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(size)
        self.image.convert()
        self.image.fill((148, 148, 148))
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        gui.clickables.add(self)
        gui.elements.add(self)
