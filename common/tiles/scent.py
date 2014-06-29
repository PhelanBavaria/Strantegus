

import pygame
from util.load import load_image
from config import TILE_SIZE
from config import SCENT_UPDATE_TICKS
from config import SCENT_VISIBLE
from common.tiles.tile import BaseTile


class Scent(BaseTile):
    def __init__(self, ant, amount=20.0, level='surface'):
        x = ant.rect.x//TILE_SIZE
        y = ant.rect.y//TILE_SIZE
        BaseTile.__init__(self, x, y, ant.world, 'scent')
        self._type = self.__class__.__name__.lower()
        existing = self.exists(ant)
        if existing:
            existing.amount += amount
            existing.ants.add(ant)
        else:
            if SCENT_VISIBLE and ant.world.current_level == level:
                self.image.set_alpha(min(255, amount))
            else:
                self.image.set_alpha(0)
            self.ants = pygame.sprite.Group(ant)
            self.colony = ant.colony
            self.nation = ant.nation
            self.world = ant.world
            self.amount = amount
            self.last_update = ant.world.current_tick
            self.current_level = level
            ant.world.scents.add(self)
            ant.world.levels[level]['scents'].add(self)

    def exists(self, ant):
        scent_level = ant.world.levels[ant.current_level]['scents']
        colliding = pygame.sprite.spritecollide(self, scent_level, False)
        for scent in colliding:
            same_colony = ant.colony == scent.colony
            same_type = scent._type == self._type
            if same_colony and same_type:
                return scent

    def update(self):
        if self.last_update < self.world.current_tick:
            ticks_passed = self.world.current_tick - self.last_update
            self.amount -= ticks_passed / SCENT_UPDATE_TICKS
            self.last_update = self.world.current_tick
        if self.amount <= 0:
            self.kill()
        if SCENT_VISIBLE and self.current_level == self.world.current_level:
            self.image.set_alpha(min(255, self.amount))
        else:
            self.image.set_alpha(0)
