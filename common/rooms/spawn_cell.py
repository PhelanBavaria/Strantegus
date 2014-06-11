

from common.rooms import Room


class SpawnCell(Room):
    __slots__ = ['egg_tally']

    def __init__(self, world, colony):
        Room.__init__(self, world, colony)
        self.egg_tally = 0

    def update(self):
        if egg_tally:            
        