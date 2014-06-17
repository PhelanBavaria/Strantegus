

import random
from common.entities import Ant


class Warrior(Ant):
    __slots__ = []

    def __init__(self, world, nation, scent=None):
        Ant.__init__(self, world, nation, scent)
        self.lifespan = (100, 365)

    def behave_check(self):
        pass  # ToDo: give warrior behaviors
