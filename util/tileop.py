

def get_free_adjacent(tile, collidable):
    for rel in ((0, -1), (1, 0), (0, 1), (-1, 0)):
        adj = tile.rect.copy()
        adj.move(*rel)
        if 