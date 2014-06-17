

import pygame
from config import TILE_SIZE
from common.tiles.resource import Resource
from common import resources


class Sugar(Resource):
    def __init__(self, x, y, world, level='surface'):
        Resource.__init__(self, x, y, world, 'sugar')
