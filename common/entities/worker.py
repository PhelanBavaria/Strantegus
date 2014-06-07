

import random
from common.entities import Ant
from common.behaviours import scout
from common.behaviours import store


class Worker(Ant):
    def __init__(self, world, nation, scent=None):
        Ant.__init__(self, world, nation, scent)
        self.behaviours['scout'] = scout.default
        self.behaviours['store'] = store.default
        self.behaviour = 'scout'

    def behave_check(self):
        if self.inside:
            if self.ressource:
                self.behaviour = 'store'
            else:
                self.behaviour = 'rest'
        elif self.ressource:
            base = self._degree_to_rel[self.rotation]
            res_coord = [self.size*2*(a+b)
                         for a, b
                         in zip(base, self.rect.center)]
            self.ressource.rect.center = res_coord
            self.behaviour = 'return_home'
        elif 1 == random.randint(1, 1000):
            self.behaviour = 'return_home'
        elif not self.behaviour:
            self.behaviour = 'scout'
