

import pygame
import config


def toggle_scent_visible():
    config.SCENT_VISIBLE = not config.SCENT_VISIBLE


keymap = {
    (pygame.K_F5,): toggle_scent_visible
}

def add(keys, action):
    keymap[keys] = action
