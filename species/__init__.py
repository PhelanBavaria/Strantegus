
from species.base_species import BaseSpecies
from species import brown
from species import red

normal = {
    'brown': brown.Brown,
    'red': red.Red,
    'orange': None,
    'leavecutter': None
}
elemental = {
    'earth': None,  #
    'fire': None,  #
    'air': None,  #
    'water': None  # can breath under water and are rain resistent
}
special = {
    'cellulant': None,  # reproduces via body splitting
    'necromant': None,  # lives from dead enemies, colony built out of dead bodies
    'bavarant': None
}