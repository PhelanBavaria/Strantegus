

from species import BaseSpecies
from common import entities


class Media(entities.Worker):
    pass

class Larvae(entities.Larvae):
    def hatching_type(self):
        return Media

class Brown(BaseSpecies):
    larvae_type = Larvae
