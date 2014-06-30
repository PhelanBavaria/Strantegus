

from util.randop import one_in
from species import BaseSpecies
from common import entities


class Media(entities.Worker):
    color = (155, 15, 15)

    def is_enemy(self, BaseEntity):
        own_colony = BaseEntity.colony == self.colony
        is_dead = BaseEntity.stamina == 0
        return not (own_colony or is_dead)


class Warrior(entities.Warrior):
    pass


class Larvae(entities.Larvae):
    def select_type(self):
        if one_in(9):
            ant_type = Warrior
        else:
            ant_type = Media
        return ant_type


class BaseMyrmica(BaseSpecies):
    larvae_type = Larvae
