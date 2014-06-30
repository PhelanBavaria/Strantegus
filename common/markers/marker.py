

import pygame
import config


class BaseMarker:
    def __init__(self, world, x, y):
        self.world = world
        self.x, self.y = x, y
        self.groups = set()
        world.markers.add(self)

    def update(self):
        pass

    def add_internal(self, group):
        self.groups.add(group)

    def remove_internal(self, group):
        self.groups.remove(group)

    def delete(self):
        for g in self.groups:
            g.remove_internal(self)
