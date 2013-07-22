import pygame
from pygame.locals import *

import globals
import utils

from bomb import Bomb


class Player(object):
    def __init__(self, i, j, color, inverted_color, player_number):
        self.color = color
        self.inverted_color = inverted_color
        self.i = i
        self.j = j
        self.bomb_radious = 2
        if player_number == 1:
            self.up = K_w
            self.down = K_s
            self.left = K_a
            self.right = K_d
            self.place = K_SPACE
        elif player_number == 2:
            self.up = K_UP
            self.down = K_DOWN
            self.left = K_LEFT
            self.right = K_RIGHT
            self.place = K_p

        self.max_bombs = 1
        self.current_bombs = 0
        self.update_center()

    def update(self, event):
        if event.type == KEYDOWN:
            if event.key == self.up:
                self.move(0, -1)
            elif event.key == self.down:
                self.move(0, 1)
            elif event.key == self.left:
                self.move(-1, 0)
            elif event.key == self.right:
                self.move(1, 0)
            elif event.key == self.place:
                self.place_bomb()

    def update_center(self):
        '''updates the center of the circle according to i and j'''
        self.center = (
            utils.index_to_pixel(self.i),
            utils.index_to_pixel(self.j)
        )

    def move(self, di, dj):
        self.i += di
        self.j += dj

        if self.i < 0 or \
           self.j < 0 or \
           self.i >= len(globals.squares) or \
           self.j >= len(globals.squares[0]) or \
           globals.squares[self.i][self.j].owner != self:
            self.j -= dj
            self.i -= di

        self.update_center()

    def place_bomb(self):
        if self.current_bombs < self.max_bombs:
            self.current_bombs += 1
            globals.bombs.append(Bomb(self.i, self.j, self))

    def render(self):
        pygame.draw.circle(
            globals.display,
            self.color,
            self.center,
            globals.p_radious
        )
