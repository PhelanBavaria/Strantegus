
from species.base_species import BaseSpecies
from species import formica
from species import myrmica

normal = {
    'formica': {
        'fusca': formica.Fusca
    },
    'myrmica': {
        'rubra': myrmica.Rubra
    },
    'orange': None,
    'leavecutter': None,
    'honeypot': None,
    'driver': None
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
