

import random
from util.randop import weighted_choice
from pygame.sprite import spritecollide
from pygame.sprite import collide_rect
from common import tiles
from common.resources import resources as default_resources


def default(ant):
    def only_updated(scent):
        scent.update()
        if scent.groups():
            return collide_rect(ant, scent)  # Check if ant still collides
        else:
            return False

    def only_allies(scent):
        return scent.nation == ant.nation

    def only_resource(scent):
        return scent.kind == 'resource'

    def only_in_los(scent):
        # ToDo: Unuglyfy
        dist = [a - b for a, b in zip(scent.rect.center, ant.rect.center)]
        m = max(abs(dist[0]), abs(dist[1]))
        try:
            rel_move = round(dist[0]/m), round(dist[1]/m)
        except ZeroDivisionError:
            return False  # sniffer is right on top of center of scent
        direct = ant.rotation
        left = (ant.rotation + 45) % 360
        right = (ant.rotation - 45) % 360
        if right < 0:
            right += 360
        direct = ant._degree_to_rel[direct] == rel_move
        left = ant._degree_to_rel[left] == rel_move
        right = ant._degree_to_rel[right] == rel_move
        return any((direct, left, right))

    def biased_random(scents):
        # ToDo: add favor of straight routes
        weights = []
        for scent in scents:
            weights.append(scent.amount)
        return weighted_choice(weights, scents)

    if ant.inside:
        ant.colony.exit(ant)
    elif ant.smell_timer:
        ant.smell_timer -= 1
        return
    elif 1 is random.randint(1, 60):
        ant.smell_timer = random.randint(15, 30)
        return
    resources = spritecollide(ant, ant.world.resources, False)
    scent_level = ant.world.levels[ant.current_level]['scents']
    scents = spritecollide(ant, scent_level, False)
    # ToDo: would combining filters reduce lag?
    # ToDo: get random pixel of each scent into a list
    #       then run filters on that list
    scents = filter(only_updated, scents)
    scents = filter(only_allies, scents)
    # scents = filter(only_resource, scents)
    scents = filter(only_in_los, scents)
    scents = tuple(scents)
    if resources:
        res = resources[0]
        amount = min(ant.strength, res.amount)
        res.amount -= amount
        ant.resource = default_resources[res.name](ant.world, amount)
    elif scents:
        ant.on_trail = True
        scent = biased_random(scents)
        ant.move(scent.rect.center)
        if not ant.world.current_tick % 20:
            tiles['scent'](ant, 10.0)
    elif 1 == random.randint(1, 5):
        ant.on_trail = False
        ant.rand_rotate()
        ant.move()
        # if not ant.world.current_tick % 20:
        #     tiles['scent'](ant)
    else:
        ant.on_trail = False
        ant.move()
        # if not ant.world.current_tick % 20:
        #     tiles['scent'](ant)
