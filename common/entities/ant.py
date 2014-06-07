

import random
import pygame
from pygame.sprite import spritecollide
import config
from util.id_generator import id_generator
from common.entities import Entity
from common.behaviours import react_to_enemy
from common.behaviours import return_home
from common.behaviours import rest


class Ant(Entity):
    inside = True
    scent = None
    colony = None
    size = 1
    strength = 2
    smell_timer = 0
    ressource = None
    behaviour = 'rest'
    colliding_enemies = ()

    def __init__(self, world, nation, scent=None):
        Entity.__init__(self, world)
        self.behaviours = {
            'react_to_enemy': react_to_enemy.hostile,
            'rest': rest.rand_time,
            'return_home': return_home.direct
        }
        self.world = world
        self.nation = nation
        if scent:
            self.scent = scent
        else:
            self.scent = nation.scent + '|' + id_generator()

    def update(self):
        ticks_passed = self.world.current_tick - self.init_tick
        if ticks_passed % config.TICKS_PER_DAY == 0:
            self.age += 1
        self.behave_check()
        self.behaviours[self.behaviour](self)

    def behave_check(self):
        if self.stamina > 0:
            self.colliding_enemies = self.enemies_colliding()
            if self.colliding_enemies:
                self.behaviour = 'react_to_enemy'
            else:
                self.behaviour = 'rest'
        else:
            self.behaviour = 'rest'
