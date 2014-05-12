

from common.objects import Object


class Ressource(Object):
    def __init__(self, world, amount):
        Object.__init__(self, world)
        self.amount = amount
        self.name = 'noname'

    def update(self):
        if self.amount == 0:
            self.world.ressources.remove(self)
            self.world.objects.remove(self)
        elif self.amount < 0:
            print('Ressource has less than an amount of 0 left:')
            print(self)
