

from common.resources import BaseResource


class Water(BaseResource):
    __slots__ = []
    color = (61, 123, 159)

    def __init__(self, world, amount=150):
        BaseResource.__init__(self, world, amount)
        self.name = 'water'
