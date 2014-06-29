

import random
from pygame.sprite import spritecollide
from common.jobs import BaseJob
from common.behaviors import dig
from common.behaviors import relocate
from common.behaviors import walk


class Janitor(BaseJob):
    def __init__(self, ant):
        BaseJob.__init__(self, ant)
        self.behaviors['walk'] = walk.random_walk
        self.behaviors['dig_tunnel'] = dig.tunnel
        self.behaviors['dig_chamber'] = dig.chamber
        self.behaviors['relocate'] = relocate.resources
        self.overcrowded_counter_stage = 0

    def _filter_same_level(self, obj):
        return obj.current_level == self.ant.current_level

    def select_behavior(self):
        if self.ant.inside:
            scents = self.ant.world.levels[self.ant.current_level]['scents']
            scents = spritecollide(self.ant, scents, False)
            #  If there are already existing scents:
            for scent in scents:
                if scent._type == 'chamber':
                    self.behavior = 'dig_chamber'
                    return
                elif scent._type == 'tunnel':
                    self.behavior = 'dig_tunnel'
                    return
            #  If there are no scents but it's getting too overcrowded:
            colliding = spritecollide(self.ant, self.ant.world.entities, False)
            colliding = list(filter(self._filter_same_level, colliding))
            if len(colliding) > 5:
                self.overcrowded_counter_stage += 1
            elif self.overcrowded_counter_stage > 0:
                    self.overcrowded_counter_stage -= 1
            if self.overcrowded_counter_stage >= 5:
                pass #self.behavior = 'dig_tunnel'
            elif self.behavior == 'dig_tunnel' and 1 == random.randint(1, 1500):
                self.behavior = 'dig_chamber'
            else:
                if scents:
                    pass
                else:
                    self.behavior = 'walk'
