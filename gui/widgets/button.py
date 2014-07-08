

import pygame
from gui.widgets import Widget


class Button(Widget):
    __slots__ = ['action']

    def __init__(self, gui, position, action, size=(50, 25)):
        Widget.__init__(self, gui, position, size)
        self.action = None

    def select(self):
        Widget.select(self)
        self.action()
        print('Action', self.action, 'successful executed!')
