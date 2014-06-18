

import events
from gui.pages import BasePage


class MainGame(BasePage):
    def __init__(self, gui, world):
        BasePage.__init__(self, gui)
        self.world = world

    def draw(self):
        events.clickables['world'] = self.world.clickables
        for game_objects in self.world.levels[self.world.current_level]:
            game_objects.draw(self.gui.screen)
