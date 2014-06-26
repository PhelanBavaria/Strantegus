

from common.entities import Ant
from common.entities import Larvae
from common.jobs import Spawner


class Queen(Ant):
    __slots__ = [
        'egg_tally',
        'expecting',
        'first_layed_eggs']

    def __init__(self, world, nation):
        Ant.__init__(self, world, nation)
        self.job = Spawner(self)
        self.egg_tally = 20
        self.expecting = True
        self.first_layed_eggs = 0
