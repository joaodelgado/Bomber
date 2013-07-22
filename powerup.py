import pygame

from random import choice

import globals
import utils


def bigger_bombs(player):
    player.bomb_radious += 0.5
    player.bomb_radious = min(player.bomb_radious, 5)

powerups = [
    bigger_bombs
]


class Powerup(pygame.Rect):
    def __init__(self, i, j):
        global powerups
        self.i = i
        self.j = j
        self.color = globals.yellow
        self.powerup = choice(powerups)
        self.timer = 5000
        super(Powerup, self).__init__(
            utils.index_to_pixel(self.i) - globals.pw_size/2,
            utils.index_to_pixel(self.j) - globals.pw_size/2,
            globals.pw_size,
            globals.pw_size)

    def update(self):
        self.timer -= globals.clock.get_time()
        if self.timer < 0:
            globals.powerups.remove(self)

    def pickup(self, player):
        self.powerup(player)
        globals.powerups.remove(self)

    def render(self):
        pygame.draw.rect(
            globals.display,
            self.color,
            self
        )
