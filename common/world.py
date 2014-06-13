

import random
from time import time
import pygame
import config
from util.id_generator import id_generator
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
        'levels',
        'out_ants',
        'scents',
        'players',
        'events']

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
        self.out_ants = pygame.sprite.Group()
        self.scents = pygame.sprite.Group()
        self.levels = {
            'underground': {
                'background': pygame.sprite.Group(),
                'foreground': pygame.sprite.Group()
            },
            'surface': {
                'ground': pygame.sprite.Group(),
                'surface': pygame.sprite.Group(),
                'air': pygame.sprite.Group()
            }
        }
        self.players = {}
        self.events = {}
        self.create = maps[setup['map_name']].create
        self.players = setup['players']
        self.create(self)
        for name, player in self.players.items():
            self.players[name] = player(self)
        print('setting up world done')

    def turn(self):
        turn_time = time()
        spt = turn_time - self.last_tick
        if spt >= 1/config.TPS:
            self.last_tick = time()
            self.entities.update()
            if self.current_tick in self.events.keys():
                for event in self.events[self.current_tick]:
                    event()
            if self.current_tick % config.TICKS_PER_DAY == 0:
                self.day += 1
            self.current_tick += 1

    def add_event(self, event, turn):
        if turn not in self.events.keys():
            self.events[turn] = []
        self.events[turn].append(event)
        # print(turn)
        # print(len(self.events.items()))

    def randloc(self):
        x = random.randint(0, self.setup['map_size'][0]) * config.TILE_SIZE
        y = random.randint(0, self.setup['map_size'][1]) * config.TILE_SIZE
        return (x, y)
