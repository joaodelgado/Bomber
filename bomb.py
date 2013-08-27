from pygame.locals import *

import globals
import utils

from explosion import Explosion
from animation import Animation

class Bomb(object):
    def __init__(self, i, j, player):
        self.i = i
        self.j = j
        self.player = player
        self.timer = globals.b_timer
        self.animation = Animation(globals.b_images[player.player_number-1])

    def update(self):
        self.timer -= globals.clock.get_time()
        if self.timer < 0:
            self.explode()
        self.animation.update()

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

                    if globals.squares[i][j].owner != self.player:
                        globals.squares[i][j].change_owner(self.player)
                    globals.explosions.append(Explosion(i, j))

    def remove(self):
        globals.bombs.remove(self)
        self.player.current_bombs -= 1

    def render(self):
        self.animation.render(
            self.i * globals.square_size,
            self.j * globals.square_size,
        )
