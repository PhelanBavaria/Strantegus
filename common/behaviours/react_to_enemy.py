

import random


def hostile(ant):
    enemy = random.choice(ant.colliding_enemies)
    ant.attack(enemy)
    if enemy.stamina <= 0:
        ant.ressource = enemy
