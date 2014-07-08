

import pygame
from gui.widgets import Widget


class Entry(Widget):
    __slots__ = ['text']

    def __init__(self, gui, position, text='', size=(250, 25)):
        Widget.__init__(self, gui, position, size)
        self.text = text
        self.img_inner = pygame.Surface((self.rect.width-6, self.rect.height-6))
        self.img_inner.convert()
        self.img_inner.fill((255, 255, 255))
        self.rect_inner = self.img_inner.get_rect()
        self.rect_inner.topleft = (self.rect.left+3, self.rect.top+3)
        self.action = None

    def draw(self, surface):
        Widget.draw(self, surface)
        text = self.gui.font.render(self.text, 1, (0, 0, 0))
        surface.blit(self.img_inner, self.rect_inner.topleft)
        surface.blit(text, self.rect_inner.topleft)

    def key_input(self, key):
        if key == pygame.K_BACKSPACE:
            self.text = self.text[0:-1]
        elif key == pygame.K_RETURN:
            if self.action:
                self.action(self.text)
            self.text = ''
        elif key <= 127 and key >= 32:
            self.text += chr(key)
        else:
            return False
        return True
