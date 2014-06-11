

from common.resources import Resource


class Sugar(Resource):
    __slots__ = []
    color = (255, 255, 255)

    def __init__(self, world, amount=150):
        Resource.__init__(self, world, amount)
        self.name = 'sugar'
