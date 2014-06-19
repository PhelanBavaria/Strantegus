

import random
import pygame
from common.tiles.resource import Resource


class Water(Resource):
    def __init__(self, world, x, y):
        Resource.__init__(self, x, y, world, 'water')
        self.start_amount = self.amount
        world.dangers.add(self)

    def update(self):
        Resource.update(self)
        if not random.randint(0, 9):
            self.amount -= 1
            alpha = 255/self.start_amount*self.amount
            self.image.set_alpha(alpha)
