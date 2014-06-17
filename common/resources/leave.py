

from common.resources import BaseResource


class Leave(BaseResource):
    __slots__ = []
    color = (40, 75, 40)

    def __init__(self, world, amount=150):
        BaseResource.__init__(self, world, amount)
        self.name = 'leave'
