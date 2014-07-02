

from common.behaviors import return_home
from common.behaviors import react_to_enemy
from common.behaviors import rest


class BaseJob:
    def __init__(self, ant):
        self.ant = ant
        self.behavior = 'rest'
        self.behaviors = {}
        self.behaviors['return_home'] = return_home.follow_trail
        self.behaviors['react_to_enemy'] = react_to_enemy.hostile
        self.behaviors['rest'] = rest.indefinite

    def update(self):
        # Here goes code to check if job changes
        pass

    def execute(self):
        self.select_behavior()
        self.behaviors[self.behavior](self.ant)

    def select_behavior(self):
        self.colliding_enemies = self.enemies_colliding()
        if self.colliding_enemies:
            self.behavior = 'react_to_enemy'
        else:
            self.behavior = 'rest'
