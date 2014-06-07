

import pygame
from gui.widgets import Widget


class Button(Widget):
    def __init__(self, gui, position, size=(50, 25)):
        Widget.__init__(self, gui, position, size)

    def on_left_click(self):
        print('No action done on click of button')
