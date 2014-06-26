

from common.jobs import BaseJob


class Larvae(BaseJob):
    def __init__(self, ant):
        BaseJob.__init__(self, ant)

    def select_behavior(self):
        if self.ant.age <= 80:
            self.hatch(self.ant.select_type())

    def hatch(self, ant_type):
        ant = ant_type(self.ant.world, self.ant.nation, self.ant.scent)
        ant.rect.center = self.ant.rect.center
        self.ant.colony.join(ant)
        self.ant.kill()
