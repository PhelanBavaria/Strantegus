

import pygame


class BaseRoom(pygame.sprite.Sprite):
    __slots__ = [
        'colony',
        'content_type',
        'content']

    def __init__(self, world, colony):
        pygame.sprite.Sprite.__init__(self)
        self.world = world
        self.colony = colony
        self.content_type = ''
        self.content = []

    def store(self, content):
        if not self.content_type:
            self.content_type = str(type(content))
        elif str(type(content)) != self.content_type:
            raise TypeError('Has to be same content type')
        self.content.append(content)
