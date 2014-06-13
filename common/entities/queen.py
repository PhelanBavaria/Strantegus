

import random
import config
from common.entities import Ant
from common.entities import Larvae
from common.behaviours import rest


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
        self.behaviours['rest'] = rest.indefinite

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
                        in_ants = self.world.levels['underground'][1]
                        out_ants = self.world.levels['surface'][1]
                        if len(in_ants) + len(out_ants) >= config.MAX_ANTS:
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
        elif not self.world.current_tick - self.init_tick % 200:
            self.expecting = True
