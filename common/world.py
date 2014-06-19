

import random
from time import time
import pygame
import config
import events
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
        'dangers',
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
        self.scents = pygame.sprite.Group()
        self.dangers = pygame.sprite.Group()
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
        self.clickables = pygame.sprite.Group()
        self.create = maps[setup['map_name']].create
        self.players = setup['players']
        self.speed_mod = 1
        self.world_events = []
        self.create(self)
        for name, player in self.players.items():
            self.players[name] = player(self)
        events.keymap[pygame.K_SPACE] = self.toggle_speed
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
        x = random.randint(0, self.setup['map_size'][0])
        y = random.randint(0, self.setup['map_size'][1])
        return (x, y)

    def toggle_speed(self):
        if self.speed_mod == 0:
            self.speed_mod = 1
        elif self.speed_mod == 1:
            self.speed_mod = 0
