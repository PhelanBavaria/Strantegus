

import pygame
from util.load import load_image
from config import TILE_SIZE
from config import SCENT_UPDATE_TICKS
from common.tiles.tile import BaseTile


class Scent(BaseTile):
    def __init__(self, ant, amount=20.0):
        x = ant.rect.x//TILE_SIZE
        y = ant.rect.y//TILE_SIZE
        BaseTile.__init__(self, x, y, ant.world, 'scent')
        existing = self.exists(ant)
        if existing:
            existing.amount += amount
            existing.ants.add(ant)
        else:
            self.image.set_alpha(min(255, amount*2))
            self.ants = pygame.sprite.Group(ant)
            self.colony = ant.colony
            self.nation = ant.nation
            self.world = ant.world
            self.amount = amount
            self.last_update = ant.world.current_tick
            ant.world.tiles.add(self)
            ant.world.scents.add(self)

    def exists(self, ant):
        colliding = pygame.sprite.spritecollide(self, ant.world.scents, False)
        for scent in colliding:
            if ant.colony == scent.colony:
                return scent

    def update(self):
        if self.amount <= 0:
            self.kill()
        elif self.last_update < self.world.current_tick:
            ticks_passed = self.world.current_tick - self.last_update
            self.amount -= ticks_passed / SCENT_UPDATE_TICKS
            self.last_update = self.world.current_tick
            self.image.set_alpha(min(255, self.amount*2))
