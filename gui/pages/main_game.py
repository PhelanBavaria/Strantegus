

import events
from gui.pages import BasePage


class MainGame(BasePage):
    def __init__(self, gui, world):
        BasePage.__init__(self, gui)
        self.world = world

    def draw(self):
        events.clickables['world'] = self.world.clickables
        for gobjects in self.world.levels[self.world.current_level].values():
            gobjects.draw(self.gui.screen)
