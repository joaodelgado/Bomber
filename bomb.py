import pygame
from pygame.locals import *

import globals
import utils

from explosion import Explosion


class Bomb(pygame.Rect):
    def __init__(self, i, j, player):
        self.i = i
        self.j = j
        self.player = player
        self.timer = 2000
        self.color = globals.red
        super(Bomb, self).__init__(
            utils.index_to_pixel(self.i) - globals.b_size/2,
            utils.index_to_pixel(self.j) - globals.b_size/2,
            globals.b_size,
            globals.b_size)

    def update(self):
        self.timer -= globals.clock.get_time()
        if self.timer < 0:
            self.explode()

    def explode(self):
        bomb.remove()

        # rewrite for loops
        for i in range(
                max(0,
                    int(self.i - self.player.bomb_radious)),
                min(globals.squares_per_line,
                    int(self.i+1 + self.player.bomb_radious))):
            for j in range(
                    max(0,
                        int(self.j - self.player.bomb_radious)),
                    min(globals.squares_per_line,
                        int(self.j+1 + self.player.bomb_radious))):
                center = (self.i, self.j)
                square = (i, j)

                if utils.distance(center, square) <= self.player.bomb_radious:

                    # delete powerup in that square, if any
                    for powerup in globals.powerups:
                        if powerup.i == square[0] and \
                           powerup.j == square[1]:
                            globals.powerups.remove(powerup)
                            break

                    # delete bomb in that square, if any
                    for bomb in globals.bombs:
                        if bomb.i == square[0] and \
                           bomb.j == square[1]:
                            bomb.remove()
                            break

                    globals.explosions.append(Explosion(i, j))
                    if globals.squares[i][j].owner != self.player:
                        globals.squares[i][j].change_owner(self.player)

    def remove(self):
        globals.bombs.remove(self)
        self.player.current_bombs -= 1

    def render(self):
        pygame.draw.rect(
            globals.display,
            self.color,
            self)
