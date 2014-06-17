

from common.resources import BaseResource


class Stone(BaseResource):
    __slots__ = []
    color = (148, 148, 148)

    def __init__(self, world, amount=150):
        BaseResource.__init__(self, world, amount)
        self.name = 'stone'
