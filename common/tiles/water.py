

import pygame
from common.tiles.resource import Resource


class Water(Resource):
    def __init__(self, world, x, y):
        Resource.__init__(self, x, y, world, 'water')
