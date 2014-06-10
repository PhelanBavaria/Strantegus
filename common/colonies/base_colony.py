

import random
import pygame
from config import TILE_SIZE
from util.randop import weighted_choice
from common.objects import Object
from common.entities import Ant
from common.rooms import Room


class BaseColony(Object):
    world = None
    species = None
    leader = None
    scent = None
    location = (0, 0)
    color = (87, 76, 39)
    surface_size = (32, 32)
    main_pheromone = 'work'
    resource_storage = {}
    scents = {}

    def __init__(self, world, leader):
        Object.__init__(self, world)
        self.leader = leader
        self.leader.rect.center = self.rect.center
        self.in_ants = pygame.sprite.Group()
        self.out_ants = pygame.sprite.Group()
        self.rooms = pygame.sprite.Group()
        self.join(leader)

    def store(self, resource):
        if type(resource) not in self.resource_storage.keys():
            self.resource_storage[type(resource)] = 0
        try:
            self.resource_storage[type(resource)] += resource.amount
        except AttributeError:
            self.resource_storage[type(resource)] += resource.size

    def join(self, ant):
        ant.colony = self
        self.in_ants.add(ant)

    def enter(self, ant):
        self.out_ants.remove(ant)
        self.in_ants.add(ant)
        self.world.out_ants.remove(ant)
        ant.rotate(180)
        ant.inside = True

    def exit(self, ant):
        self.in_ants.remove(ant)
        self.out_ants.add(ant)
        self.world.out_ants.add(ant)
        ant.rand_rotate(full_spin=True)
        ant.inside = False

    def add_room(self):
        self.rooms.add(Room(self.world, self))
