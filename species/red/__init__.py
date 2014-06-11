

import random
from species import BaseSpecies
from common import entities


class Media(entities.Worker):
    color = (155, 15, 15)

    def is_enemy(self, BaseEntity):
        own_colony = BaseEntity.colony == self.colony
        is_dead = BaseEntity.stamina == 0
        return not (own_colony or is_dead)


class Larvae(entities.Larvae):
    def hatching_type(self):
        return Media


class Red(BaseSpecies):
    larvae_type = Larvae
