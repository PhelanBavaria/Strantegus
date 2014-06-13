

import random
import pygame
from config import TILE_SIZE
from util.randop import weighted_choice
from common.entities import Ant
from common.rooms import BaseRoom


class BaseColony(pygame.sprite.Sprite):
    __slots__ = [
        'world',
        'leader',
        'color',
        'surface_size',
        'resource_storage']

    def __init__(self, world, leader):
        pygame.sprite.Sprite.__init__(self)
        self.color = (87, 76, 39)
        self.surface_size = (32, 32)
        self.image = pygame.Surface(self.surface_size)
        self.image.convert()
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.world = world
        self.leader = leader
        self.leader.rect.center = self.rect.center
        self.rooms = pygame.sprite.Group()
        self.resource_storage = {}
        self.join(leader)
        world.tiles.add(self)

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
        ant.inside = False

    def add_room(self):
        self.rooms.add(BaseRoom(self.world, self))
