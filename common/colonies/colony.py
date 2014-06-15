

import random
import pygame
from config import TILE_SIZE
from util.randop import weighted_choice
from common.entities import Ant
from common import tiles
from common.rooms import BaseRoom


class BaseColony:
    __slots__ = [
        'world',
        'leader',
        'tiles',
        'resource_storage']

    def __init__(self, world, leader):
        self.world = world
        self.leader = leader
        self.rooms = pygame.sprite.Group()
        self.tiles = {
            'entrance': tiles['colony_entrance'],
            'wall': tiles['colony_wall']
        }
        self.entrances = pygame.sprite.Group()
        self.resource_storage = {}
        self.join(leader)
        # world.tiles.add(self)

    def store(self, resource):
        if type(resource) not in self.resource_storage.keys():
            self.resource_storage[type(resource)] = 0
        try:
            self.resource_storage[type(resource)] += resource.amount
        except AttributeError:
            self.resource_storage[type(resource)] += resource.size

    def join(self, ant):
        ant.colony = self
        self.world.levels['underground'][1].add(ant)

    def enter(self, ant):
        self.world.levels['surface'][1].remove(ant)
        self.world.levels['underground'][1].add(ant)
        ant.rotate(180)
        ant.inside = True

    def exit(self, ant):
        self.world.levels['underground'][1].remove(ant)
        self.world.levels['surface'][1].add(ant)
        ant.rand_rotate(full_spin=True)
        if ant.exit_hole is None:
            ant.exit_hole = random.choice(list(self.entrances))
        ant.rect.center = ant.exit_hole.rect.center
        ant.inside = False

    def add_room(self):
        self.rooms.add(BaseRoom(self.world, self))
