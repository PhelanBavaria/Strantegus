

import random
import pygame
from pygame.sprite import spritecollide
import config
from util.id_generator import id_generator
from common.entities import Entity
from common.scents import AntScent
from common.behaviours import return_home



class Ant(Entity):
    inside = True
    scent = None
    colony = None
    size = 1
    strength = 2
    smell_timer = 0
    ressource = None

    return_home = return_home.direct

    def __init__(self, world, scent=None):
        Entity.__init__(self, world)
        self.world = world
        if scent:
            self.scent = scent
        else:
            self.scent = id_generator()

    def update(self):
        if (self.world.current_tick - self.init_tick) % config.TICKS_PER_DAY == 0:
            self.age += 1
        if self.age <= 0:
            pass
        elif self.stamina > 0 or self.age <= 0:
            enemies = self.enemies_colliding()
            if enemies:
                self.react_to_enemy(enemies)
            elif self.inside:
                if self.ressource:
                    self.colony.store(self.ressource)
                    self.ressource = None
                elif 1 == random.randint(1, 200):
                    self.homesick = False
                    self.colony.exit(self)
            elif self.smell_timer:
                self.smell_timer -= 1
            elif 1 is random.randint(1, 60):
                self.smell_timer = random.randint(15, 30)
            elif self.ressource or self.homesick:
                self.return_home(self)
            elif 1 == random.randint(1, 1000):
                self.homesick = True
            else:
                self.search_resources()
            #self.job.act(self)
            # for scent in self.trail:
            #     if self.world.current_turn - scent.turn >= config.SCENT_TTL:
            #         scent.disappear()
            #     else:
            #         break

    def react_to_enemy(self, enemies):
        self.attack(random.choice(enemies))

    def search_resources(self):
        # if found ressource: load up ressource and return
        ressources = spritecollide(self, self.world.map.ressources, False)
        scent_loc = self.sniff(self.world.scents)
        if ressources:
            res = ressources[0]
            amount = min(self.strength, res.amount)
            res.amount -= amount
            self.ressource = res.__class__(amount)
        elif scent_loc:
            self.move()
            AntScent(self)
        elif 1 == random.randint(1, 5):
            self.rand_rotate()
            self.move()
            AntScent(self)
        else:
            self.move()
            AntScent(self)
