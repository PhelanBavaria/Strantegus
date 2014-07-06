

import random
import pygame
from config import TILE_SIZE
from config import TICKS_PER_DAY
from util.degrees import Degrees


class BaseEntity(pygame.sprite.Sprite):
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
    __slots__ = [
        'world',
        'rotation',
        'speed',
        'age',
        'strength',
        'stamina',
        'resource',
        'lifespan',
        'job',
        'current_level']
    color = (0, 0, 0)
    size = 4

    def __init__(self, world, level='underground'):
        pygame.sprite.Sprite.__init__(self)
        surface_size = (self.size/2+1, self.size/2+1)
        self.image = pygame.Surface(surface_size)
        self.image.convert()
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.init_tick = world.current_tick
        self.world = world
        self.rotation = Degrees()
        self.speed = 1
        self.age = 0
        self.strength = 2
        self.stamina = 10
        self.resource = None
        self.lifespan = (100, 1000)
        self.job = None
        self.current_level = level
        world.entities.add(self)
        world.levels[level]['foreground'].add(self)

    def update(self):
        ticks_passed = self.world.current_tick - self.init_tick
        if self.age > random.randint(*self.lifespan):
            self.stamina = 0
            return
        elif ticks_passed % TICKS_PER_DAY == 0:
            self.age += 1
        if self.stamina <= 0:
            return
        elif self.job:
            self.job.update()
            self.job.execute()

    def rand_rotate(self, full_spin=False, forward=True):
        if full_spin:
            rotation = random.choice(list(self._degree_to_rel.keys()))
        elif forward:
            rotation = random.choice((-45, 45))
        elif not forward:
            rotation = random.choice((-135, 180, 135))
        self.rotate(rotation)

    def rotate(self, rotation):
        self.on_rotation(rotation)
        self.rotation += rotation
        d = self._degree_to_rel[int(self.rotation)]

    def move(self, goal=()):
        # ToDo: make this more modular so inherited objects don't need to
        #       overwrite all of this
        for danger in self.world.dangers:
            if danger.rect.collidepoint(self.rect.center):
                self.stamina = 0
                return
        if goal:
            dist = [a - b for a, b in zip(goal, self.rect.center)]
            m = max(abs(dist[0]), abs(dist[1]))
            try:
                rel_pos = round(dist[0]/m), round(dist[1]/m)
            except ZeroDivisionError:
                print('ZeroDivisionError', dist)
                return
        else:
            rel_pos = self._degree_to_rel[int(self.rotation)]
        rel_px = rel_pos[0]*self.speed, rel_pos[1]*self.speed
        old_rect = self.rect
        self.rect.move_ip(*rel_px)
        obstacles = pygame.sprite.spritecollide(self,
                                                self.world.obstacles,
                                                False)
        for obstacle in obstacles:
            if obstacle.level == self.current_level:
                self.rect = old_rect
                self.rand_rotate()
                return
        self.rotation = Degrees(self._rel_to_degree[rel_pos])
        self.on_move(self.rect.center)
        # rect_pos = [x + y for x, y in zip(rel_px, self.rect.center)]
        # self.rect.center = tuple(rect_pos)
        # self.rotation = self._rel_to_degree[rel_pos]

        map_width = self.world.setup['map_size'][0]*TILE_SIZE
        map_height = self.world.setup['map_size'][1]*TILE_SIZE
        # oob == out of bounds
        oob_right = self.rect.right > map_width
        oob_bottom = self.rect.bottom > map_height
        oob_left = self.rect.left < 0
        oob_top = self.rect.top < 0
        if oob_right:
            self.rect.right = map_width
        if oob_bottom:
            self.rect.bottom = map_height
        if oob_left:
            self.rect.left = 0
        if oob_top:
            self.rect.top = 0
        if oob_right or oob_bottom or oob_left or oob_top:
            self.rand_rotate(full_spin=True, forward=False)
        if self.resource:
            print(self.rotation)
            try:
                weight = self.resource.amount
            except AttributeError:
                weight = self.resource.size
            if self.strength//2 >= weight:
                rel_px = self._degree_to_rel[self.rotation]
            elif self.strength//2 < weight:
                rel_px = self._degree_to_rel[self.rotation+180]
            new_x = rel_px[0] * self.size + self.rect.center[0]
            new_y = rel_px[1] * self.size + self.rect.center[1]
            self.resource.rect.center = (new_x, new_y)

    def attack(self, enemy):
        enemy.get_hurt(self.strength)

    def get_hurt(self, amount):
        self.stamina -= amount
        if self.stamina <= 0:
            self.stamina = 0

    def is_enemy(self, BaseEntity):
        own_colony = BaseEntity.colony == self.colony
        own_species = type(BaseEntity) == type(self)
        is_dead = BaseEntity.stamina == 0
        different_elevation = BaseEntity.inside != self.inside
        return not (own_colony or
                    own_species or
                    is_dead or
                    different_elevation)

    def enemies_colliding(self):
        colliding = pygame.sprite.spritecollide(self,
                                                self.world.entities,
                                                False)
        enemies = []
        for BaseEntity in colliding:
            if self.is_enemy(BaseEntity):
                enemies.append(BaseEntity)
        return enemies

    def on_rotation(self, rotation):
        pass

    def on_move(self, move):
        pass
