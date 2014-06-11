

from common.rooms import BaseRoom


class SpawnCell(BaseRoom):
    __slots__ = ['egg_tally']

    def __init__(self, world, colony):
        BaseRoom.__init__(self, world, colony)
        self.egg_tally = 0

    def update(self):
        if egg_tally:            
        