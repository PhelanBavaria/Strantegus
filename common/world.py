

import random
from time import time
import pygame
import config
from util.id_generator import id_generator
from common.worldmap import WorldMap
from common.entities import Entity
from common.objects import Object


class World:
    map = None
    spt = 0.05  # seconds per turn
    origin = (0, 0)
    current_turn = 0
    current_tick = 0
    last_tick = 0
    players = {}
    entities = Entity._entities
    objects = Object._objects
    out_ants = pygame.sprite.Group()
    scents = pygame.sprite.Group()
    events = {}

    def setup(self, setup):
        print('setting up world')
        random.seed(setup['seed'])
        self.map = WorldMap()
        self.map.create(*setup['map_size'])
        self.players = setup['players']
        print('setting up world done')

    def turn(self):
        turn_time = time()
        spt = turn_time - self.last_tick
        if spt >= 1/config.TPS:
            self.real_tps = round(1/spt)
            self.last_tick = time()
            self.map.update()
            self.entities.update()
            self.map.ressources.update()
            if self.current_tick in self.events.keys():
                for event in self.events[self.current_tick]:
                    event()
            self.current_tick += 1

    def add_event(self, event, turn):
        if turn not in self.events.keys():
            self.events[turn] = []
        self.events[turn].append(event)
        # print(turn)
        # print(len(self.events.items()))
