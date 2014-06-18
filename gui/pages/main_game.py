

from gui.pages import BasePage


class MainGame(BasePage):
    def __init__(self, gui, world):
        BasePage.__init__(self, gui)
        self.world = world

    def draw(self):
        self.gui.clickables = self.world.clickables  # ToDo: Add it to
                                                     #      clickables in
                                                     #      the events,
                                                     #      once they are
                                                     #      separated from
                                                     #      the GUI
        for game_objects in self.world.levels[self.world.current_level]:
            game_objects.draw(self.gui.screen)
