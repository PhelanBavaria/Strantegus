

import random
import pygame
from config import TILE_SIZE


class Entity(pygame.sprite.Sprite):
    coords = (0, 0)
    world = None
    rotation = 0
    focus_range = 2
    speed = 1
    size = 4
    color = (0, 0, 0)

    age = -85
    strength = 2
    stamina = 10
    ressource = None

    _degree_to_rel = {
        0: (1, 0),
        45: (1, -1),
        90: (0, -1),
        135: (-1, -1),
        180: (-1, 0),
        225: (-1, 1),
        270: (0, 1),
        315: (1, 1)
    }
    _rel_to_degree = dict([reversed(i) for i in _degree_to_rel.items()])

    def __init__(self, world):
        pygame.sprite.Sprite.__init__(self)
        self.world = world
        surface_size = (self.size*2+1, self.size*2+1)
        self.image = pygame.Surface(surface_size)
        self.image.convert()
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.init_tick = world.current_tick
        world.entities.add(self)

    def rand_rotate(self, full_spin=False, forward=True):
        if full_spin:
            rotation = random.choice(list(self._degree_to_rel.keys()))
        elif forward:
            rotation = random.choice((-45, 0, 45))
        elif not forward:
            rotation = random.choice((-135, 180, 135))
        self.rotate(rotation)

    def rotate(self, rotation):
        self.rotation = (self.rotation + rotation) % 360
        if self.rotation < 0:
            self.rotation += 360
        d = self._degree_to_rel[self.rotation]

    def move(self, goal=()):
        # ToDo: Unuglyfy
        if goal:
            dist = [a - b for a, b in zip(goal, self.rect.center)]
            m = max(abs(dist[0]), abs(dist[1]))
            try:
                rel_move = round(dist[0]/m), round(dist[1]/m)
            except ZeroDivisionError:
                print('ZeroDivisionError', dist)
                return
        else:
            rel_move = self._degree_to_rel[self.rotation]
        rel_pos = rel_move[0]*self.speed, rel_move[1]*self.speed
        rect_pos = [x + y for x, y in zip(rel_pos, self.rect.center)]
        self.rect.center = tuple(rect_pos)
        self.rotation = self._rel_to_degree[rel_move]

        oob_right = self.rect.right > self.world.map.w*TILE_SIZE
        oob_bottom = self.rect.bottom > self.world.map.h*TILE_SIZE
        oob_left = self.rect.left < 0
        oob_top = self.rect.top < 0
        if oob_right:
            self.rect.right = self.world.map.w*TILE_SIZE
        if oob_bottom:
            self.rect.bottom = self.world.map.h*TILE_SIZE
        if oob_left:
            self.rect.left = 0
        if oob_top:
            self.rect.top = 0
        if oob_right or oob_bottom or oob_left or oob_top:
            self.rand_rotate(full_spin=True, forward=False)
        if self.ressource:
            rel_pos = self._degree_to_rel[self.rotation]
            new_x = rel_pos[0] * self.size + self.rect.center[0]
            new_y = rel_pos[1] * self.size + self.rect.center[1]
            self.ressource.rect.center = (new_x, new_y)

    def attack(self, enemy):
        enemy.get_hurt(self.strength)

    def get_hurt(self, amount):
        self.stamina -= amount
        if self.stamina <= 0:
            self.stamina = 0

    def is_enemy(self, entity):
        own_colony = entity.colony == self.colony
        own_species = type(entity) == type(self)
        is_dead = entity.stamina == 0
        different_elevation = entity.inside != self.inside
        return not (own_colony or
                    own_species or
                    is_dead or
                    different_elevation)

    def enemies_colliding(self):
        colliding = pygame.sprite.spritecollide(self,
                                                self.world.entities,
                                                False)
        enemies = []
        for entity in colliding:
            if self.is_enemy(entity):
                enemies.append(entity)
        return enemies

    def sprite_in_los(self, sprite):
        sprite.rect
        self.rotation
