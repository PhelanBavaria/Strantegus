
import sys
from time import time
import config
import util
import technologies
import gui
import events


if __name__ == '__main__':
    from pprint import pprint
    import species
    from common.world import World
    from gui.gui import GUI
    from common.tiles import Sugar
    from gui.pages import MainGame

    gui = GUI()
    setup = {
        'players': {
            #'brown': species.normal['formica']['fusca'],
            'red': species.normal['myrmica']['rubra']
        },
        'map_name': 'test',
        'map_size': (100, 60),
        'seed': 666
    }
    world = World(setup)

    current_page = 'main_game'
    pages = {
        'main_game': MainGame(gui, world)
    }
    test_sugar = Sugar(50, 30, world)
    test_sugar.structure(10)

    last_frame = time()
    while not events.exit:
        turn_time = time()
        world.turn()
        if turn_time - last_frame >= 1/config.FPS:
            pages[current_page].draw()
            if config.SCENT_VISIBLE:
                gui.draw_markers(world.markers)
                if not world.current_tick % 250:
                    world.markers.update()
            info_current_day = gui.font.render('Day:' + str(world.day), 1, ((10, 10, 10)))
            info_current_tick = gui.font.render('Current Tick:' + str(world.current_tick), 1, ((10, 10, 10)))
            info_speed_mod = gui.font.render('Speed Modifier:' + str(world.speed_mod), 1, ((10, 10, 10)))
            info_current_level = gui.font.render('Current Level:' + world.current_level, 1, ((10, 10, 10)))
            gui.draw_info(info_current_day, (10, 10))
            gui.draw_info(info_current_tick, (10, 20))
            gui.draw_info(info_speed_mod, (10, 30))
            gui.draw_info(info_current_level, (10, 40))
            gui.draw()
            gui.update()
            events.check()
            last_frame = time()

    print(len(tuple(world.entities)), 'entities')
    print('testing ends')
    events.quit()
    sys.exit()
