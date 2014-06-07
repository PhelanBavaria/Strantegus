

import random
from util.randop import weighted_choice
from pygame.sprite import spritecollide
from pygame.sprite import collide_rect
from common.scents import AntScent


def default(ant):
    def only_updated(scent):
        scent.update()
        return collide_rect(ant, scent)

    def only_allies(scent):
        return scent.ant.nation == ant.nation

    def only_ressource(scent):
        return scent.kind == 'ressource'

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
    ressources = spritecollide(ant, ant.world.map.ressources, False)
    scents = spritecollide(ant, ant.world.scents, False)
    # ToDo: would combining filters reduce lag?
    scents = filter(only_updated, scents)
    scents = filter(only_allies, scents)
    scents = filter(only_ressource, scents)
    scents = filter(only_in_los, scents)
    if ressources:
        res = ressources[0]
        amount = min(ant.strength, res.amount)
        res.amount -= amount
        ant.ressource = res.__class__(ant.world, amount)
    elif tuple(scents):
        print(bool(tuple(scents)))
        scent = biased_random(scents)
        print(scent)
        ant.move(scent)
        if not ant.world.current_tick % 20:
            AntScent(ant, 'search')
    elif 1 == random.randint(1, 5):
        ant.rand_rotate()
        ant.move()
        if not ant.world.current_tick % 20:
            AntScent(ant, 'search')
    else:
        ant.move()
        if not ant.world.current_tick % 20:
            AntScent(ant, 'search')
