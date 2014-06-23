

import random
from config import MAX_ANTS
from config import TICKS_PER_DAY
from common.entities import Ant
from common.entities import Larvae


class Queen(Ant):
    __slots__ = [
        'egg_tally',
        'expecting',
        'first_layed_eggs']

    def __init__(self, world, nation):
        Ant.__init__(self, world, nation)
        self.egg_tally = 20
        self.expecting = True
        self.first_layed_eggs = 0

    def behave_check(self):
        # ToDo: move everything that is no behavior checking
        #       into separate funcitons
        if not self.colony:
            if 1 == random.randint(1, 200):
                coords = self.world.randloc()
                self.nation.establish_colony(coords, self.world, self)
        elif self.expecting:
            for room in self.colony.rooms:
                if room.content_type in ('', 'spawn_cell'):
                    for egg in range(self.egg_tally):
                        in_ants = self.world.levels['underground']['foreground']
                        out_ants = self.world.levels['surface']['foreground']
                        if len(in_ants) + len(out_ants) >= MAX_ANTS:
                            break
                        larvae = self.nation.larvae_type(self.world,
                                                         self.colony)
                        larvae.rect.center = self.rect.center
                        self.colony.join(larvae)
                        room.store(larvae)
                    self.expecting = False
                    if not self.first_layed_eggs:
                        self.first_layed_eggs = self.age
            else:
                self.colony.add_room()
        elif not (self.world.current_tick - self.init_tick) % TICKS_PER_DAY:
            self.expecting = True
