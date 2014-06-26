

import random
from common.entities import Ant
from common.jobs import Scout
from common.jobs import Janitor


class Worker(Ant):
    __slots__ = ['on_trail']

    def __init__(self, world, nation, scent=None):
        Ant.__init__(self, world, nation, scent)
        self.lifespan = (100, 365)
        self.job = Scout(self)
        self.on_trail = False
