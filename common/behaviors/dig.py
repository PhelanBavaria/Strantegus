

from common.tiles import scents


def tunnel(ant):
    scents.Tunnel(ant)


def chamber(ant):
    tile = scents.Chamber(ant)
    tiles = ant.world.tiles
    adjacent = tile.adjacent(tiles)
    for space in adjacent:
        for adj in space:
            if adj in ant.world.obstacles:
                adj.kill()
    #scents.Chamber(ant)
    tile.kill()
