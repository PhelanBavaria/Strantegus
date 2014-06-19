

class BaseEvent:
    def __init__(self, world):
        self.world = world
        self.duration = 1  # Tick
        self.progress = 0

    def update(self):
        if self.progress:
            if self.progress >= self.duration:
                self.progress = 0
                self.end()
            else:
                self.effect()
                self.progress += 1
        elif self.condition():
            self.effect()
            self.progress += 1

    def condition(self):
        return False

    def effect(self):
        pass

    def end(self):
        pass
