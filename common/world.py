

import random
from time import time
import pygame
import config
from util.id_generator import id_generator
from common.worldmap import WorldMap


class World:
    __slots__ = [
        'map',
        'origin',
        'current_tick',
        'day',
        'last_tick',
        'entities',
        'resources',
        'tiles',
        'out_ants',
        'scents',
        'players',
        'events']

    def __init__(self):
        self.origin = (0, 0)
        self.current_tick = 0
        self.day = 0
        self.last_tick = 0
        self.entities = pygame.sprite.Group()
        self.resources = pygame.sprite.Group()
        self.tiles = pygame.sprite.Group()
        self.out_ants = pygame.sprite.Group()
        self.scents = pygame.sprite.Group()
        self.players = {}
        self.events = {}
        self.map = WorldMap()

    def setup(self, setup):
        print('setting up world')
        random.seed(setup['seed'])
        self.map.create(self, *setup['map_size'])
        self.players = setup['players']
        print('setting up world done')

    def turn(self):
        turn_time = time()
        spt = turn_time - self.last_tick
        if spt >= 1/config.TPS:
            self.last_tick = time()
            self.map.update()
            self.entities.update()
            self.map.resources.update()
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
