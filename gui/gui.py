

import pygame
import config
from util.load import load_image


class GUI:
    __slots__ = []
    pygame.init()
    pygame.display.set_caption('Strantegus')
    screen = pygame.display.set_mode((1000, 500))
    icon = pygame.image.load('gfx/ant.jpg').convert_alpha()
    pygame.display.set_icon(icon)
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((111, 11, 11))
    screen.blit(background, (0, 0))
    pygame.display.flip()
    elements = pygame.sprite.Group()
    font = pygame.font.Font('fonts/freesansbold.ttf', 10)

    def draw(self, elements=None):
        if not elements:
            elements = self.elements
        elements.draw(self.screen)

    def draw_info(self, info, pos):
        self.screen.blit(info, pos)

    def draw_markers(self, markers):
        for marker in markers:
            visual = pygame.Surface((config.MARKER_SIZE, config.MARKER_SIZE))
            visual = visual.convert()
            try:
                visual.fill(marker.color)
            except TypeError:
                print(marker.color)
            visual.set_alpha(marker.alpha)
            self.screen.blit(visual, (marker.x, marker.y))

    def update(self):
        pygame.display.flip()
