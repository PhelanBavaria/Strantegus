

from common.tiles.scent import Scent


class Tunnel(Scent):
    def __init__(self, ant, amount=20.0, level='underground'):
        Scent.__init__(self, ant, amount, level)


class Chamber(Scent):
    def __init__(self, ant, amount=40.0, level='underground'):
        Scent.__init__(self, ant, amount, level)
