

import random
from species import BaseSpecies
from common.colonies.dirt import Colony
from common.entities import Queen as Leader
from common.entities import Ant


class FireAnt(Ant):
    color = (155, 15, 15)

    def is_enemy(self, entity):
        own_colony = entity.colony == self.colony
        is_dead = entity.stamina == 0
        return not (own_colony or is_dead)



class Red(BaseSpecies):
    default_ant_type = FireAnt
