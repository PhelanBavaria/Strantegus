

import sys
from time import time
import pygame
import config
import util
import technologies
import gui
import keymap
from common.world import World
from gui.gui import GUI


class Game:
    def __init__(self, player):
        self.player = player
        self.gui = GUI()
        self.worlds = []
        self.current_page = 'main_menu'
        self.pages = {}
        self.exit = False
        self.keys_pressed = []
        keymap.add((pygame.K_ESCAPE,), self.quit)

    def add_world(self, setup):
        self.worlds.append(World(setup))

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if self.gui.selected:
                    if self.gui.selected.key_input(event.key):
                        continue
                if event.key not in self.keys_pressed:
                    self.keys_pressed.append(event.key)
            elif event.type == pygame.KEYUP:
                if event.key in self.keys_pressed:
                    self.keys_pressed.remove(event.key)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for widget in self.gui.widgets:
                    if widget.rect.collidepoint(mouse_pos):
                        widget.select()
        for keys, action in keymap.keymap.items():
            if all([True if key in self.keys_pressed else False
                   for key in keys]):
                action()

    def main_loop(self):
        last_frame = time()
        while not self.exit:
            turn_time = time()
            for world in self.worlds:
                world.update()
            if turn_time - last_frame >= 1/config.FPS:
                self.pages[self.current_page].draw()
                if config.SCENT_VISIBLE:
                    # ToDo: replace world below with self.player.world
                    self.gui.draw_markers(world.markers)
                    if not world.current_tick % 250:
                        world.markers.update()
                self.gui.draw()
                self.gui.update()
                last_frame = time()
            self.check_events()

    def quit(self):
        if self.exit:
            pygame.quit()
        else:
            self.exit = True



if __name__ == '__main__':
    from pprint import pprint
    import species
    from common.tiles import Sugar
    from gui.pages import MainGame

    local_player = None
    game = Game(local_player)
    setup = {
        'players': {
            #'brown': species.normal['formica']['fusca'],
            'red': species.normal['myrmica']['rubra']
        },
        'map_name': 'test',
        'map_size': (100, 60),
        'seed': 888
    }
    game.add_world(setup)
    game.current_page = 'main_game'
    game.pages['main_game'] = MainGame(game)

    test_sugar = Sugar(50, 30, game.worlds[0])
    test_sugar.structure(10)

    game.main_loop()

    print('Keymap:')
    for keys, action in keymap.keymap.items():
        print([pygame.key.name(key) for key in keys], action)
    print(len(tuple(game.worlds[0].entities)), 'entities')
    print('testing ends')
    sys.exit()
