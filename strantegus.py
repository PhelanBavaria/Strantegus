
import sys
from time import time
import config
import util
import technologies
import gui


if __name__ == '__main__':
    from pprint import pprint
    import species
    from gui_setup import gui
    from common.world import World
    from common import resources

    setup = {
        'players': {
            'brown': species.normal['brown'],
            'red': species.normal['red']
        },
        'map_name': 'test',
        'map_size': (100, 60),
        'seed': 333
    }
    world = World(setup)

    test_sugar = resources['sugar'](world)
    test_sugar.rect.topleft = (500, 300)
    #world.map.resources.add(test_sugar)

    last_frame = time()
    while not gui.exit:
        turn_time = time()
        world.turn()
        if turn_time - last_frame >= 1/config.FPS:
            gui.draw(world.tiles)
            if config.SCENT_VISIBLE:
                if not world.current_tick % 250:
                    world.scents.update()
                gui.draw(world.scents)
            gui.draw(world.resources)
            gui.draw(world.out_ants)
            info_current_day = gui.font.render('Day:' + str(world.day), 1, ((10, 10, 10)))
            info_current_tick = gui.font.render('Current Tick:' + str(world.current_tick), 1, ((10, 10, 10)))
            info_scent_tally = gui.font.render('Scent Tally:' + str(len(world.scents)), 1, ((10, 10, 10)))
            gui.draw_info(info_current_day, (10, 10))
            gui.draw_info(info_current_tick, (10, 20))
            gui.draw_info(info_scent_tally, (10, 30))
            gui.draw()
            gui.update()
            gui.check_events()
            last_frame = time()

    print(len(tuple(world.entities)), 'entities')
    print('testing ends')
    gui.quit()
    sys.exit()
