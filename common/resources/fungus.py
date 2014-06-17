

from common.resources import BaseResource


class Fungus(BaseResource):
    __slots__ = []
    color = (231, 147, 107)

    def __init__(self, world, amount=150):
        BaseResource.__init__(self, world, amount)
        self.name = 'fungus'
