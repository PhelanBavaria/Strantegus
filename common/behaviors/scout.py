

import random
from util.randop import weighted_choice
from util.randop import one_in
from pygame.sprite import spritecollide
from pygame.sprite import collide_rect
from common.markers import Scent
from common.resources import resources as default_resources


def default(ant):
    def only_in_range(scent):
        scent.update()
        if scent.groups:
            return ant.can_sniff(scent)
        else:
            return False

    def only_allies(scent):
        return scent.nation == ant.nation

    def only_resource(scent):
        return scent.kind == 'resource'

    def only_in_los(scent):
        # ToDo: Unuglyfy
        x = ant.rect.center[0]
        y = ant.rect.center[1]
        dist = scent.x - x, scent.y - y
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
        # ToDo: add distance to be a weight, not just amount
        weights = []
        for scent in scents:
            weights.append(scent.amount)
        return weighted_choice(weights, scents)

    if ant.inside:
        ant.colony.exit(ant)
    elif ant.smell_timer:
        ant.smell_timer -= 1
        return
    elif one_in(60):
        ant.smell_timer = random.randint(15, 30)
        return
    entities = spritecollide(ant, ant.world.entities, False)
    entities = [entity for entity in entities if entity.stamina <= 0]
    resources = spritecollide(ant, ant.world.resources, False)
    resources += entities
    if resources:
        res = resources[0]
        try:
            amount = min(ant.strength, res.amount)
            res.amount -= amount
            ant.resource = default_resources[res.name](ant.world, amount)
            return
        except AttributeError:
            if ant.strength > res.size:
                ant.resource = res
                print('here')
                return
    # ToDo: would combining filters reduce lag?
    scents = filter(only_in_range, ant.colony.scents)
    scents = filter(only_allies, scents)
    # scents = filter(only_resource, scents)
    scents = filter(only_in_los, scents)
    scents = tuple(scents)
    if scents:
        ant.on_trail = True
        scent = biased_random(scents)
        ant.move((scent.x, scent.y))
        if not ant.world.current_tick % 20:
            Scent(ant, 'resource', amount=10.0)
    elif one_in(50):
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
