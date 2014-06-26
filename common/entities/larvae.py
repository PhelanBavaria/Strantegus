

import random
from common.entities import Ant
from common.entities import Worker
from common.entities import Warrior
from common.jobs import Larvae as LarvaeJob


class Larvae(Ant):
    __slots__ = []

    def __init__(self, world, colony):
        Ant.__init__(self, world, colony.leader.nation)
        self.job = LarvaeJob(self)
        self.colony = colony

    def select_type(self):
        if 1 == random.randint(1, 10):
            ant_type = Warrior
        else:
            ant_type = Worker
        return ant_type
