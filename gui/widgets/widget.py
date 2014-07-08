

import pygame


class Widget(pygame.sprite.Sprite):
    __slots__ = []

    def __init__(self, gui, position, size=(50, 25)):
        pygame.sprite.Sprite.__init__(self)
        self.gui = gui
        self.image = pygame.Surface(size)
        self.image.convert()
        self.image.fill((148, 148, 148))
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        gui.widgets.add(self)

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

    def select(self):
        self.gui.selected = self

    def key_input(self, key):
        pass
