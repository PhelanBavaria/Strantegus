

from config import TILE_SIZE
from common import tiles
from common.events import Rain


def create(world):
    w = world.setup['map_size'][0]
    h = world.setup['map_size'][1]
    for y in range(h):
        for x in range(w):
            tiles['grass'](world, x, y)
            tiles['dirt_wall'](world, x, y)
            #draw_groups['tiles'].add(tile)
            #_map[(x, y)] = {
            #    'tile': tile,
            #    'scents': [],
            #    'resources': [],
            #    'structure': None
            #    }
    world.world_events.append(Rain(world, intensity=(100, 100)))
