

import random
import pygame
from config import TILE_SIZE
from common import tiles
from common.rooms import BaseRoom


class BaseColony:
    __slots__ = [
        'world',
        'leader',
        'tiles',
        'ants',
        'scents',
        'resource_storage']

    def __init__(self, world, leader):
        self.world = world
        self.leader = leader
        self.rooms = pygame.sprite.Group()
        self.ants = pygame.sprite.Group()
        self.tiles = {
            'entrance': tiles['colony_entrance'],
            'wall': tiles['colony_wall']
        }
        self.scents = pygame.sprite.Group()
        self.entrances = pygame.sprite.Group()
        self.resource_storage = {}
        self.join(leader)
        pos = leader.rect.center
        x, y = pos[0]//TILE_SIZE, pos[1]//TILE_SIZE
        self.tiles['entrance'](world, self, x, y)
        tiles['dirt'](world, self, x, y)

    def store(self, resource):
        if type(resource) not in self.resource_storage.keys():
            self.resource_storage[type(resource)] = 0
        try:
            self.resource_storage[type(resource)] += resource.amount
        except AttributeError:
            self.resource_storage[type(resource)] += resource.size

    def join(self, ant):
        ant.colony = self
        self.ants.add(ant)

    def enter(self, ant):
        self.world.levels['surface']['foreground'].remove(ant)
        self.world.levels['underground']['foreground'].add(ant)
        ant.current_level = 'underground'
        ant.inside = True

    def exit(self, ant):
        self.world.levels['underground']['foreground'].remove(ant)
        self.world.levels['surface']['foreground'].add(ant)
        ant.current_level = 'surface'
        ant.rotate(180)
        if ant.exit_hole is None:
            ant.exit_hole = random.choice(list(self.entrances))
        ant.rect.center = ant.exit_hole.rect.center
        ant.inside = False

    def add_room(self):
        self.rooms.add(BaseRoom(self.world, self))
