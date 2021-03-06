

from util.randop import one_in
from config import MAX_ANTS
from config import TICKS_PER_DAY
from common.jobs import BaseJob
from common.behaviors import lay_eggs


class Spawner(BaseJob):
    def __init__(self, ant):
        BaseJob.__init__(self, ant)
        self.behaviors['lay_eggs'] = lay_eggs.default

    def select_behavior(self):
        def establish_colony():
            coords = self.ant.world.randloc()
            self.ant.nation.establish_colony(coords, self.ant.world, self.ant)
        if not self.ant.colony:
            if one_in(200):
                establish_colony()
        elif self.ant.expecting:
            for room in self.ant.colony.rooms:
                if room.content_type in ('', 'spawn_cell'):
                    for egg in range(self.ant.egg_tally):
                        if len(list(self.ant.colony.ants)) >= MAX_ANTS:
                            break
                        larvae = self.ant.nation.larvae_type(self.ant.world,
                                                         self.ant.colony)
                        larvae.rect.center = self.ant.rect.center
                        self.ant.colony.join(larvae)
                        room.store(larvae)
                    self.ant.expecting = False
                    if not self.ant.first_layed_eggs:
                        self.ant.first_layed_eggs = self.ant.age
            else:
                self.ant.colony.add_room()
        elif not (self.ant.world.current_tick - self.ant.init_tick) % TICKS_PER_DAY:
            self.ant.expecting = True
