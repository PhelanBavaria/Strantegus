

from common.scents import Scent


class FoodTrail(Scent):
    color = (255, 255, 255)
    def __init__(self, ant):
        Scent.__init__(self, ant)
        self.ant.world.food_trails.add(self)

    def disappear(self):
        self.ant.world.food_trails.remove(self)
