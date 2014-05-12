

import random
import pygame
from config import TILE_SIZE
from util.id_generator import id_generator
from util.randop import weighted_choice
from common.objects import Object
from common.entities import Ant


class BaseColony(Object):
    world = None
    species = None
    leader = None
    scent = None
    start_ant_tally = 0
    spawn_cell_tally = 25
    spawn_cells = {}
    ants = {}
    location = (0, 0)
    in_ants = {}
    out_ants = {}
    color = (87, 76, 39)
    surface_size = (32, 32)
    main_pheromone = 'work'
    ressource_storage = {}
    scents = {}

    def __init__(self, world, species, start_ant_tally=25, bloodline=id_generator()):
        Object.__init__(self, world)
        self.location = world.map.randloc()
        self.rect.topleft = tuple([a * TILE_SIZE for a in self.location])
        self.species = species
        self.scent = bloodline + '|' + id_generator()
        self.leader = species.leader_type(world)
        self.leader.rect.center = self.rect.center
        self.leader.age = 0
        self.leader.colony = self
        self.start_ant_tally = start_ant_tally
        for i in range(self.start_ant_tally):
            larvae = species.default_ant_type(world)
            larvae.colony = self
            larvae.age = 0
            larvae.rect.center = self.rect.center
            self.spawn_cells[larvae.scent] = larvae

    def act(self):
        for scent, larvae in list(self.spawn_cells.items()):
            if larvae.age >= 0:
                ant = self.spawn_cells.pop(scent)
                self.ants[scent] = ant
                self.in_ants[scent] = ant

    def store(self, ressource):
        if ressource.name not in self.ressource_storage.keys():
            self.ressource_storage[ressource.name] = 0
        self.ressource_storage[ressource.name] += ressource.amount

    def enter(self, ant):
        self.out_ants.pop(ant.scent)
        self.in_ants[ant.scent] = ant
        ant.inside = True

    def exit(self, ant):
        self.in_ants.pop(ant.scent)
        self.out_ants[ant.scent] = ant
        ant.rand_rotate(full_spin=True)
        ant.inside = False
