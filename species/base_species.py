

from util.id_generator import id_generator
from common.colonies.dirt import Colony
from common.entities import Queen
from common.entities import Ant

class BaseSpecies:
    colony_type = Colony
    leader_type = Queen
    governor_type = Queen
    default_ant_type = Ant
    leader = None
    colonies = []

    def establish_colony(self, coords, world):
        colony = self.colony_type(self, world)
        colony.coords = coords
        if not self.colonies:
            self.leader = self.leader_type(world)
            colony.leader = self.leader
        else:
            colony.leader = governor_type()
        self.colonies.append(colony)

    def act(self):
        for colony in self.colonies:
            colony.act()
            colony.spawn()
