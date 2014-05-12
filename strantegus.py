
import sys
from time import time
import config


if __name__ == '__main__':
    from pprint import pprint
    import species
    from common.gui import GUI
    from common.world import World
    from common import ressources

    gui = GUI()
    world = World()

    setup = {
        'players': {
            'brown': species.normal['brown'](),
            'red': species.normal['red']()
        },
        'map_size': (25, 15),
        'start_ant_tally': 100,
        'seed': 666
    }
    world.setup(setup)

    test_sugar = ressources['sugar'](world)
    test_sugar.rect.topleft = (500, 300)
    world.map.ressources.add(test_sugar)

    last_frame = time()
    while not gui.exit:
        turn_time = time()
        world.turn()
        if turn_time - last_frame >= 1/config.FPS:
            gui.draw()
            gui.draw(world.map.draw_groups['tiles'])
            if config.SCENT_VISIBLE:
                gui.draw(world.scents)
            gui.draw(world.objects)
            gui.draw(world.out_ants)
            info_tps = gui.font.render('Real TPS:' + str(world.real_tps), 1, ((10, 10, 10)))
            info_current_tick = gui.font.render('Current Tick:' + str(world.current_tick), 1, ((10, 10, 10)))
            info_scent_tally = gui.font.render('Scent Tally:' + str(len(world.scents)), 1, ((10, 10, 10)))
            gui.draw_info(info_tps, (10, 10))
            gui.draw_info(info_current_tick, (10, 20))
            gui.draw_info(info_scent_tally, (10, 30))
            gui.update()
            gui.check_events()
            last_frame = time()

    print(len([a.rect for a in world.entities]), 'entities')
    print('testing ends')
    gui.quit()
    sys.exit()
