

import random
from species import BaseSpecies
from common import entities


class Media(entities.Worker):
    pass


class Warrior(entities.Warrior):
    pass


class Larvae(entities.Larvae):
    def hatching_type(self):
        if 1 == random.randint(1, 10):
            ant_type = Warrior
        else:
            ant_type = Media
        return ant_type


class Brown(BaseSpecies):
    larvae_type = Larvae
