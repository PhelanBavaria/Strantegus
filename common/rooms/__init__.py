

from common.objects import Object


class Room(Object):
    colony = None
    content_type = ''
    content = []

    def __init__(self, world, colony):
        Object.__init__(self, world)
        self.colony = colony

    def store(self, content):
        if not self.content_type:
            self.content_type = str(type(content))
        elif str(type(content)) != self.content_type:
            raise TypeError('Has to be same content type')
        self.content.append(content)
