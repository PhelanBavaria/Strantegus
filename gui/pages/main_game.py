

import pygame
import keymap
from gui.pages import BasePage
from gui.widgets import Entry


class MainGame(BasePage):
    def __init__(self, game):
        BasePage.__init__(self, game.gui)
        self.game = game
        self.debug_mode = False
        self.command_mode = False
        self.command_line = Entry(game.gui, (0, game.gui.height-25))
        self.command_line.action = 
        keymap.add((pygame.K_F3,), self.toggle_debug)
        keymap.add((pygame.K_RETURN,), self.toggle_commandline)

    def toggle_debug(self):
        self.debug_mode = not self.debug_mode

    def toggle_commandline(self):
        self.command_mode = not self.command_mode

    def draw(self):
        world = self.game.worlds[0]
        #ToDo: only a placeholder, has to be replaced once Player objects are implemented')
        # world = self.game.player.world
        for gobjects in world.levels[world.current_level].values():
            gobjects.draw(self.gui.screen)
        if self.command_mode:
            self.command_line.draw(self.gui.screen)
        if self.debug_mode:
            render = self.game.gui.font.render
            current_day_text = 'Day:' + str(world.day)
            current_tick_text = 'Current Tick:' + str(world.current_tick)
            speed_mod_text = 'Speed Modifier:' + str(world.speed_mod)
            current_level_text = 'Current Level:' + world.current_level
            info_current_day = render(current_day_text, 1, ((10, 10, 10)))
            info_current_tick = render(current_tick_text, 1, ((10, 10, 10)))
            info_speed_mod = render(speed_mod_text, 1, ((10, 10, 10)))
            info_current_level = render(current_level_text, 1, ((10, 10, 10)))
            self.game.gui.draw_info(info_current_day, (10, 10))
            self.game.gui.draw_info(info_current_tick, (10, 20))
            self.game.gui.draw_info(info_speed_mod, (10, 30))
            self.game.gui.draw_info(info_current_level, (10, 40))
