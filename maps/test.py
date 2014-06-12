

from config import TILE_SIZE
from common import tiles


def create(world):
    w = world.setup['map_size'][0]
    h = world.setup['map_size'][1]
    for y in range(h):
        for x in range(w):
            tile = tiles['grass'](world, x*TILE_SIZE, y*TILE_SIZE)
            #draw_groups['tiles'].add(tile)
            #_map[(x, y)] = {
            #    'tile': tile,
            #    'scents': [],
            #    'resources': [],
            #    'structure': None
            #    }
