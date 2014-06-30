

from util.randop import one_in
from species import BaseSpecies
from common import entities


class Media(entities.Worker):
    pass


class Warrior(entities.Warrior):
    pass


class Larvae(entities.Larvae):
    def select_type(self):
        if one_in(10):
            ant_type = Warrior
        else:
            ant_type = Media
        return ant_type


class BaseFormica(BaseSpecies):
    larvae_type = Larvae
