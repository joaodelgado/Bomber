import pygame
import globals
import utils


class Explosion(pygame.Rect):
    def __init__(self, i, j):
        self.color = globals.orange
        self.i = i
        self.j = j
        self.shrink_v = 0.07
        super(Explosion, self).__init__(
            utils.index_to_pixel(self.i) - globals.e_size/2,
            utils.index_to_pixel(self.j) - globals.e_size/2,
            globals.e_size,
            globals.e_size)

    def update(self):
        shrink_offset = self.shrink_v * globals.clock.get_time()
        self.inflate_ip(-shrink_offset, -shrink_offset)
        if self.width < 0.03:
            globals.explosions.remove(self)

    def render(self):
        pygame.draw.rect(
            globals.display,
            self.color,
            self)
