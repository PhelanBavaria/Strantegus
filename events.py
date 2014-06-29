

import pygame
import config


exit = False
clickables = {}
keys_pressed = []


def quit():
    global exit
    if exit:
        pygame.quit()
    else:
        exit = True


def toggle_scent_visible():
    config.SCENT_VISIBLE = not config.SCENT_VISIBLE


keymap = {
    (pygame.K_ESCAPE,): quit,
    (pygame.K_F3,): toggle_scent_visible
}


def check():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key not in keys_pressed:
                keys_pressed.append(event.key)
        elif event.type == pygame.KEYUP:
            if event.key in keys_pressed:
                keys_pressed.remove(event.key)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for name, group in clickables.items():
                for clickable in group:
                    if clickable.rect.collidepoint(mouse_pos):
                        clickable.on_left_click()
    for keys, action in keymap.items():
        if all([True if key in keys_pressed else False
               for key in keys]):
            action()
