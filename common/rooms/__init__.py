

import pygame


class Room(pygame.sprite.Sprite):
    colony = None
    content_type = ''
    content = []

    def __init__(self, world, colony):
        pygame.sprite.Sprite.__init__(self)
        self.world = world
        self.colony = colony

    def store(self, content):
        if not self.content_type:
            self.content_type = str(type(content))
        elif str(type(content)) != self.content_type:
            raise TypeError('Has to be same content type')
        self.content.append(content)
