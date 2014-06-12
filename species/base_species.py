

from config import TILE_SIZE
from util.id_generator import id_generator
from common.colonies.dirt import Colony
from common.entities import Larvae
from common.entities import Queen
from common.entities import Ant


class BaseSpecies:
    colony_type = Colony
    leader_type = Queen
    governor_type = Queen
    larvae_type = Larvae
    leader = None

    def __init__(self, world):
        self.scent = id_generator()
        self.leader = self.leader_type(world, self)
        self.colonies = []

    def establish_colony(self, coords, world, leader):
        colony = self.colony_type(world, leader)
        colony.rect.topleft = coords[0], coords[1]
        colony.leader.rect.center = colony.rect.center
        print('New colony at:', colony.rect.center)
        self.colonies.append(colony)
