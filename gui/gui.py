

import pygame
import config
from util.load import load_image


class GUI:
    __slots__ = [
        'exit']
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
    clickables = pygame.sprite.Group()
    font = pygame.font.Font('fonts/freesansbold.ttf', 10)

    def __init__(self):
        self.exit = False

    def draw(self, elements=None):
        if not elements:
            elements = self.elements
        elements.draw(self.screen)

    def draw_info(self, info, pos):
        self.screen.blit(info, pos)

    def update(self):
        pygame.display.flip()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.exit = True
                elif event.key == pygame.K_F3:
                    config.SCENT_VISIBLE = not config.SCENT_VISIBLE
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for clickable in self.clickables:
                    if clickable.rect.collidepoint(mouse_pos):
                        clickable.on_left_click()

    def quit(self):
        if self.exit:
            pygame.quit()
        else:
            self.exit = True
