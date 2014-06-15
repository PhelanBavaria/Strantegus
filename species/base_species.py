

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
        colony.leader.rect.center = coords[0], coords[1]
        colony.tiles['entrance'](world, colony, coords[0], coords[1])
        print('New colony at:', coords)
        self.colonies.append(colony)
