

from common.scents import BaseScent


class FoodTrail(BaseScent):
    color = (255, 255, 255)
    def __init__(self, ant):
        BaseScent.__init__(self, ant)
        self.ant.world.food_trails.add(self)

    def disappear(self):
        self.ant.world.food_trails.remove(self)
