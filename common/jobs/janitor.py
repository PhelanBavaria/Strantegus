

from common.jobs import BaseJob
from common.behaviors import dig
from common.behaviors import relocate


class Janitor(BaseJob):
    def __init__(self, ant):
        BaseJob.__init__(self)
        self.behaviors['dig'] = dig.chamber
        self.behaviors['relocate'] = relocate.resources

    def select_behavior(self):
        pass
