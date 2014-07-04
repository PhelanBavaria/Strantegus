

import random
from pygame import K_F4
from config import TICKS_PER_DAY
import keymap
from util.randop import one_in
from common.events import BaseEvent
from common import tiles


class Rain(BaseEvent):
    # ToDo: simplify this class once issue #42 is done
    def __init__(self, world,
                 duration=(TICKS_PER_DAY/24, TICKS_PER_DAY*2),
                 intensity=(1, 100000)):
        BaseEvent.__init__(self, world)
        self.duration = random.randint(*duration)
        self.intensity = random.randint(*intensity)
        self.con = False
        self.intensity_mod = 100
        keymap.add((K_F4,), self.toggle)

    def toggle(self):
        self.con = not self.con
        self.progress = 0

    def condition(self):
        if self.intensity == 0:
            self.end()
        return self.con

    def effect(self):
        # if not self.progress % 1000:
        #     print('rain intensity:', self.intensity)
        #     print('rain effect for:', self.progress, self.duration)
        mod = self.intensity_mod
        extra_drop_chance = mod - (self.intensity % mod)
        extra_drop = one_in(extra_drop_chance)
        drops = self.intensity // mod + extra_drop
        for drop in range(drops):
            x, y = self.world.randloc()
            tile = tiles['water'](self.world, x, y)

    def end(self):
        self.toggle()
