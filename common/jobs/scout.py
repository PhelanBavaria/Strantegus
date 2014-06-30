

from util.randop import one_in
from common.jobs import BaseJob
from common.behaviors import scout
from common.behaviors import store
from common.behaviors import rest


class Scout(BaseJob):
    def __init__(self, ant):
        BaseJob.__init__(self, ant)
        self.behaviors['search'] = scout.default
        self.behaviors['store'] = store.default
        self.behaviors['rest'] = rest.rand_time

    def select_behavior(self):
        if self.ant.inside:
            if self.ant.resource:
                self.behavior = 'store'
            else:
                self.behavior = 'rest'
        elif self.ant.resource:
            base = self.ant._degree_to_rel[self.ant.rotation]
            res_coord = [self.ant.size*2*(a+b)
                         for a, b
                         in zip(base, self.ant.rect.center)]
            self.ant.resource.rect.center = res_coord
            self.behavior = 'return_home'
        elif not self.ant.on_trail and one_in(1000):
            self.behavior = 'return_home'
        else:
            self.behavior = 'search'
