import pygame

from random import choice

import globals
import utils


def bigger_bombs(player):
    player.bomb_radious += 0.5
    player.bomb_radious = min(player.bomb_radious, 5)


def increase_bombs(player):
    player.max_bombs += 1
    player.max_bombs = min(player.max_bombs, 5)


def increase_speed(player):
    player.speed += 0.05
    player.speed = min(player.speed, 0.4)

powerups = [
    (bigger_bombs, globals.yellow),
    (increase_bombs, globals.green),
    (increase_speed, globals.brown)
]


class Powerup(pygame.Rect):
    def __init__(self, i, j):
        global powerups
        self.i = i
        self.j = j
        pw = choice(powerups)
        self.color = pw[1]
        self.powerup = pw[0]
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
