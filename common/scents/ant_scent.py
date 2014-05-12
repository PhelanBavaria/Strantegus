

import config
from common.scents import Scent


class AntScent(Scent):
    def __init__(self, ant, amount=40):
        if ant.rect.center in ant.colony.scents.keys():
            ant.colony.scents[ant.rect.center].amount += amount
        else:
            Scent.__init__(self, ant, amount)
            self.ant.colony.scents[ant.rect.center] = self
            self.ant.world.scents.add(self)
            self.ant.world.add_event(self.update, self.turn+config.SCENT_UPDATE_TICKS)

    def update(self):
        self.amount -= 1
        self.image.set_alpha(min(255, self.amount*2))
        if self.amount <= 0:
            self.ant.colony.scents.pop(self.rect.center)
            self.ant.world.scents.remove(self)
        else:
            self.ant.world.add_event(self.update, self.ant.world.current_tick+config.SCENT_UPDATE_TICKS)
