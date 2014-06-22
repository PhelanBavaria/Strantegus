

import random
import pygame
from pygame.sprite import spritecollide
from util.id_generator import id_generator
from common.entities import BaseEntity
from common.behaviours import react_to_enemy
from common.behaviours import return_home
from common.behaviours import rest


class Ant(BaseEntity):
    __slots__ = [
        'inside',
        'scent',
        'colony',
        'smell_timer',
        'behaviour',
        'behaviours',
        'exit_hole',
        'colliding_enemies'
    ]

    def __init__(self, world, nation, scent=None):
        BaseEntity.__init__(self, world)
        self.nation = nation
        self.scent = scent
        self.inside = True
        self.colony = None
        self.smell_timer = 0
        self.behaviour = 'rest'
        self.colliding_enemies = ()
        self.exit_hole = None
        self.behaviours = {
            'react_to_enemy': react_to_enemy.hostile,
            'rest': rest.indefinite,
            'return_home': return_home.direct
        }
        if scent:
            self.scent = scent
        else:
            self.scent = nation.scent + '|' + id_generator()

    def behave_check(self):
        self.colliding_enemies = self.enemies_colliding()
        if self.colliding_enemies:
            self.behaviour = 'react_to_enemy'
        else:
            self.behaviour = 'rest'
