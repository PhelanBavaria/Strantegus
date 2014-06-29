

import random
import pygame
from config import TILE_SIZE
from util.load import load_image


class BaseTile(pygame.sprite.Sprite):
    __slots__ = ['world']
    x = 0
    y = 0

    def __init__(self, x, y, world, image):
        pygame.sprite.Sprite.__init__(self)
        self.x = x*TILE_SIZE
        self.y = y*TILE_SIZE
        self.image = load_image(image+'.bmp')
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y
        self.world = world
        world.tiles.add(self)

    def adjacent(self, collidables):
        result = [[], [], [], []]
        for i, rel in enumerate(((0, -1), (1, 0), (0, 1), (-1, 0))):
            adj = self.rect.move(rel[0]*TILE_SIZE, rel[1]*TILE_SIZE)
            for coll in collidables:
                if adj.colliderect(coll.rect):
                    result[i].append(coll)
        return result

    def free_adjacent(self, collidables):
        result = [[], [], [], []]
        for i, rel in enumerate(((0, -1), (1, 0), (0, 1), (-1, 0))):
            adj = self.rect.move(rel[0]*TILE_SIZE, rel[1]*TILE_SIZE)
            if not any([adj.colliderect(coll.rect) for coll in collidables]):
                result[i].append(adj)
        return result

    def structure(self, amount, replace=True):
        tiles = [self]
        w = self.world.setup['map_size'][0]
        h = self.world.setup['map_size'][1]
        for i in range(amount):
            for tile in tiles[:]:
                adj = tile.free_adjacent(tiles)
                adj = [a for a in adj if bool(a)]
                if any(adj):
                    adj = random.choice(adj)[0]
                    new_tile = self.__class__(0, 0, self.world)
                    new_tile.rect = adj
                    tiles.append(new_tile)
