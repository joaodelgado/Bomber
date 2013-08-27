import pygame
from pygame.locals import *

import globals
import utils

from explosion import Explosion


class Bomb(object):
    def __init__(self, i, j, player):
        self.i = i
        self.j = j
        self.player = player
        self.timer = globals.b_timer
        self.frame_timer = globals.animation_speed

        if player.player_number == 1:
            self.frames = globals.b_1_images
        else:
            self.frames = globals.b_2_images
        self.current_frame = 0

    def update(self):
        self.timer -= globals.clock.get_time()
        self.frame_timer -= globals.clock.get_time()

        if self.frame_timer < 0:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.frame_timer = globals.animation_speed
        if self.timer < 0:
            self.explode()

    def explode(self):
        self.remove()

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
        globals.display.blit(
            self.frames[self.current_frame],
            (
                self.i * globals.square_size,
                self.j * globals.square_size,
            )
        )
