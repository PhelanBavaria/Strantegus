

from common.scents import BaseScent


class AntScent(BaseScent):
    __slots__ = [
        'last_update',
        'kind']

    def __init__(self, ant, kind, amount=20):
        BaseScent.__init__(self, ant, amount)
        self.ant.world.scents.add(self)
        self.last_update = ant.age
        self.kind = kind

    def update(self):
        if self.last_update < self.ant.age:
            self.amount -= self.ant.age - self.last_update
            self.last_update = self.ant.age
            self.image.set_alpha(min(255, self.amount*2))
        if self.amount <= 0:
            self.kill()
