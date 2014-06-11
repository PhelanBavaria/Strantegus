

from common.resources import BaseResource


class Sugar(BaseResource):
    __slots__ = []
    color = (255, 255, 255)

    def __init__(self, world, amount=150):
        BaseResource.__init__(self, world, amount)
        self.name = 'sugar'
