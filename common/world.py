

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
    colonies = {}
    last_tick = time()
    real_tps = 0
    current_turn = 0
    current_tick = 0
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
        for name, species in setup['players'].items():
            colony = species.colony_type(self, species, setup['start_ant_tally'])
            self.map.add_structure(colony)
            self.colonies[colony.scent] = colony
        print('setting up world done')

    def turn(self):
        turn_time = time()
        spt = turn_time - self.last_tick
        if spt >= 1/config.TPS:
            self.real_tps = round(1/spt)
            self.last_tick = time()
            self.out_ants.empty()
            for scent, colony in self.colonies.items():
                colony.act()
                for ant_scent, ant in colony.out_ants.items():
                    self.out_ants.add(ant)
            self.map.update()
            self.entities.update()
            # if self.current_tick%10 == 0:
            #     self.scents.update()
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
