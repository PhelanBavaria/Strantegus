

from collections import OrderedDict
import random
from time import time
import pygame
from pygame.sprite import OrderedUpdates
import config
import events
from maps import maps


class World:
    __slots__ = [
        'setup',
        'create',
        'origin',
        'current_tick',
        'day',
        'last_tick',
        'entities',
        'resources',
        'tiles',
        'current_level',
        'levels',
        'markers',
        'dangers',
        'obstacles',
        'players',
        'speed_mod',
        'world_events',
        'clickables']

    def __init__(self, setup):
        print('setting up world')
        random.seed(setup['seed'])
        self.setup = setup
        self.origin = (0, 0)
        self.current_tick = 0
        self.day = 0
        self.last_tick = 0
        self.entities = pygame.sprite.Group()
        self.resources = pygame.sprite.Group()
        self.tiles = pygame.sprite.Group()
        self.dangers = pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group()
        self.current_level = 'surface'
        self.levels = {
            'underground': OrderedDict(),
            'surface': OrderedDict()
        }
        self.levels['underground']['background'] = OrderedUpdates()
        self.levels['underground']['foreground'] = OrderedUpdates()
        self.levels['surface']['background'] = OrderedUpdates()
        self.levels['surface']['foreground'] = OrderedUpdates()
        self.levels['surface']['air'] = OrderedUpdates()
        self.markers = pygame.sprite.Group()
        self.players = {}
        self.clickables = pygame.sprite.Group()
        self.create = maps[setup['map_name']].create
        self.players = setup['players']
        self.speed_mod = 1
        self.world_events = []
        self.create(self)
        for name, player in self.players.items():
            self.players[name] = player(self)
        events.keymap[(pygame.K_SPACE,)] = self.toggle_speed
        events.keymap[(pygame.K_KP_PLUS,)] = self.increase_speed
        events.keymap[(pygame.K_KP_MINUS,)] = self.decrease_speed
        events.keymap[(pygame.K_PAGEUP,)] = self.level_up
        events.keymap[(pygame.K_PAGEDOWN,)] = self.level_down
        events.keymap[(278,)] = self.first_level  # Pos1
        events.keymap[(279,)] = self.last_level  # End
        print('setting up world done')

    def turn(self):
        turn_time = time()
        spt = turn_time - self.last_tick
        if spt*self.speed_mod >= 1/config.TPS:
            self.last_tick = time()
            self.entities.update()
            self.resources.update()
            if self.current_tick % config.TICKS_PER_DAY == 0:
                self.day += 1
            for we in self.world_events:
                we.update()
            self.current_tick += 1

    def randloc(self):
        x = random.randint(0, self.setup['map_size'][0]-1)
        y = random.randint(0, self.setup['map_size'][1]-1)
        return (x, y)

    def toggle_speed(self):
        if self.speed_mod == 0:
            self.speed_mod = 1
        elif self.speed_mod == 1:
            self.speed_mod = 0

    def increase_speed(self):
        if self.speed_mod == 1:
            self.speed_mod = 2
        elif self.speed_mod == 2:
            self.speed_mod = 5
        elif self.speed_mod == 5:
            self.speed_mod = 10

    def decrease_speed(self):
        if self.speed_mod == 10:
            self.speed_mod = 5
        elif self.speed_mod == 5:
            self.speed_mod = 2
        elif self.speed_mod == 2:
            self.speed_mod = 1

    def level_up(self):
        keys = list(self.levels.keys())
        i_up = keys.index(self.current_level) - 1
        if i_up >= 0:
            k_up = keys[i_up]
            self.current_level = k_up
        else:
            return

    def level_down(self):
        keys = list(self.levels.keys())
        i_down = keys.index(self.current_level) + 1
        try:
            k_down = keys[i_down]
        except IndexError:
            return
        self.current_level = k_down

    def first_level(self):
        k_first = list(self.levels.keys())[0]
        self.current_level = k_first

    def last_level(self):
        k_last = list(self.levels.keys())[-1]
        self.current_level = k_last
