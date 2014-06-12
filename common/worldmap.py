

import random
import pygame
from config import TILE_SIZE
from common.tiles import tiles


class WorldMap:
    w = 0
    h = 0
    _map = {}
    draw_groups = {
        'tiles': pygame.sprite.Group()
    }
    resources = pygame.sprite.Group()

    def info(self, location=None):
        if location:
            return self._map[location]
        else:
            return self._map

    def update(self):
        self.draw_groups['tiles'].update()

    def randloc(self):
        return random.choice(list(self._map.keys()))

    def create(self, world, w, h):
        

    def add_structure(self, structure):
        self._map[structure.location]['structure'] = structure

    def mark_scent(self, location, scent, amount):
        self._map[location]['scents'].append([scent, amount])
