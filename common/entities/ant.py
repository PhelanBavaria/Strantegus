

import random
import pygame
from pygame.sprite import spritecollide
from util.id_generator import id_generator
from util.mathop import distance
from common.entities import BaseEntity


class Ant(BaseEntity):
    __slots__ = [
        'inside',
        'scent',
        'sniffer',
        'colony',
        'scents',
        'smell_timer',
        'exit_hole',
        'colliding_enemies'
    ]

    def __init__(self, world, nation, scent=None):
        BaseEntity.__init__(self, world)
        self.nation = nation
        self.scent = scent
        self.sniffer = 40
        self.inside = True
        self.colony = None
        self.scents = pygame.sprite.Group()
        self.smell_timer = 0
        self.colliding_enemies = ()
        self.exit_hole = None
        if scent:
            self.scent = scent
        else:
            self.scent = nation.scent + '|' + id_generator()

    def can_sniff(self, scent):
        dist = distance(self.rect.center, (scent.x, scent.y))
        total_range = self.sniffer + scent.amount
        return dist <= total_range
