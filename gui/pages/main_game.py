

from gui.pages import BasePage


class MainGame(BasePage):
    def __init__(self, game):
        BasePage.__init__(self, game.gui)
        self.game = game

    def draw(self):
        world = self.game.worlds[0]
        print('main_game.py MainGame.__init__ only a placeholder, has to be replaced once Player objects are implemented')
        # world = self.game.player.world
        self.game.clickables['world'] = world.clickables
        for gobjects in self.world.levels[self.world.current_level].values():
            gobjects.draw(self.gui.screen)
