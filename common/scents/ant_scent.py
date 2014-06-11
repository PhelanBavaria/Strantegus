

from config import SCENT_UPDATE_TICKS
from common.scents import BaseScent


class AntScent(BaseScent):
    __slots__ = [
        'last_update',
        'kind']

    def __init__(self, ant, kind, amount=20.0):
        BaseScent.__init__(self, ant, amount)
        self.ant.world.scents.add(self)
        self.last_update = ant.world.current_tick
        self.kind = kind

    def update(self):
        if self.last_update < self.ant.world.current_tick:
            ticks_passed = self.ant.world.current_tick - self.last_update
            self.amount -= ticks_passed / SCENT_UPDATE_TICKS
            self.last_update = self.ant.world.current_tick
            self.image.set_alpha(min(255, self.amount*2))
        if self.amount <= 0:
            self.kill()
