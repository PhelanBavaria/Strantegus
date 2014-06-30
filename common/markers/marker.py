

import pygame
import config


class BaseMarker:
    def __init__(self, world, x, y, color=(50, 50, 50), alpha=190):
        self.world = world
        self.x, self.y = x, y
        self.groups = set()
        self.color = color
        self.alpha = alpha
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
