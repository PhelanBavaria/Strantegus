

import pygame
import config


exit = False
clickables = {}


def check():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        elif event.type == pygame.KEYDOWN:
            for key, action in keymap.items():
                if event.key == key:
                    action()
                    break
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for name, group in clickables.items():
                for clickable in group:
                    if clickable.rect.collidepoint(mouse_pos):
                        clickable.on_left_click()


def quit():
    global exit
    if exit:
        pygame.quit()
    else:
        exit = True


def toggle_scent_visible():
    config.SCENT_VISIBLE = not config.SCENT_VISIBLE


keymap = {
    pygame.K_ESCAPE: quit,
    pygame.K_F3: toggle_scent_visible
}
