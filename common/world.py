

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
        'current_level',
        'levels',
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
        self.scents = pygame.sprite.Group()
        self.current_level = 'surface'
        self.levels = {
            'underground': [
                pygame.sprite.OrderedUpdates(),  # Background
                pygame.sprite.OrderedUpdates()   # Foreground
            ],
            'surface': [
                pygame.sprite.OrderedUpdates(),  # Floor
                pygame.sprite.OrderedUpdates(),  # Surface
                pygame.sprite.OrderedUpdates()   # Air
            ]
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
            self.resources.update()
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
        x = random.randint(0, self.setup['map_size'][0])
        y = random.randint(0, self.setup['map_size'][1])
        return (x, y)
