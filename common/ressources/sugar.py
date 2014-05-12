

from common.objects import Ressource

class Sugar(Ressource):
    color = (255, 255, 255)
    def __init__(self, world, amount=150):
        size = amount//10
        self.surface_size = (size, size)
        Ressource.__init__(self, world, amount)
        self.name = 'sugar'
