import math
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

        self.keys = {
            "up": False,
            "down": False,
            "left": False,
            "right": False,
            "place": False,
        }

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
        self.bomb_radious = 2
        self.speed = 0.2
        self.update_center()

    def update_event(self, event):
        if event.type == KEYDOWN:
            if event.key == self.up:
                self.keys['up'] = True
            elif event.key == self.down:
                self.keys['down'] = True
            elif event.key == self.left:
                self.keys['left'] = True
            elif event.key == self.right:
                self.keys['right'] = True
            elif event.key == self.place:
                self.keys['place'] = True
        elif event.type == KEYUP:
            if event.key == self.up:
                self.keys['up'] = False
            elif event.key == self.down:
                self.keys['down'] = False
            elif event.key == self.left:
                self.keys['left'] = False
            elif event.key == self.right:
                self.keys['right'] = False
            elif event.key == self.place:
                self.keys['place'] = False

    def update(self):
        self.move()
        if self.keys['place']:
            self.place_bomb()
            self.keys['place'] = False

    def move(self):
        dx = dy = 0
        velocity = self.speed * globals.clock.get_time()
        if self.keys['left']:
            dx = -velocity
        elif self.keys['right']:
            dx = velocity
        if self.keys['up']:
            dy = -velocity
        elif self.keys['down']:
            dy = velocity

        if dx and dy:
            if dx > 0:
                dx = math.cos(math.pi / 4) * velocity
            else:
                dx = -math.cos(math.pi / 4) * velocity
            if dy > 0:
                dy = math.sin(math.pi / 4) * velocity
            else:
                dy = -math.sin(math.pi / 4) * velocity

        # collision checking #
        x = self.center[0] + dx
        y = self.center[1] + dy
        left = x - globals.p_radious
        right = x + globals.p_radious
        top = y - globals.p_radious
        bottom = y + globals.p_radious

        #window borders
        if left < 0:
            x = globals.p_radious
        elif right > globals.width:
            x = globals.width - globals.p_radious - 1
        if top <= 0:
            y = globals.p_radious
        elif bottom > globals.height:
            y = globals.height - globals.p_radious - 1

        # need to recalculate variables, in case something changed
        left = x - globals.p_radious
        right = x + globals.p_radious
        top = y - globals.p_radious
        bottom = y + globals.p_radious
        index_x = utils.pixel_to_index(x)
        index_y = utils.pixel_to_index(y)
        index_left = utils.pixel_to_index(left)
        index_right = utils.pixel_to_index(right)
        index_top = utils.pixel_to_index(top)
        index_bottom = utils.pixel_to_index(bottom)

        #surrounding squares
        if globals.squares[index_left][index_y].owner != self:
            x = globals.square_size * index_left + \
                globals.square_size + globals.p_radious
        elif globals.squares[index_right][index_y].owner != self:
            x = globals.square_size * index_right - \
                globals.p_radious
        if globals.squares[index_x][index_top].owner != self:
            y = globals.square_size * index_top + \
                globals.square_size + globals.p_radious
        elif globals.squares[index_x][index_bottom].owner != self:
            y = globals.square_size * index_bottom - \
                globals.p_radious

        self.center = [
            x,
            y,
        ]
        self.update_index()

    def update_center(self):
        '''updates the center of the circle according to i and j'''
        self.center = [
            utils.index_to_pixel(self.i),
            utils.index_to_pixel(self.j)
        ]

    def update_index(self):
        '''updates the i and j indexes according to the current center'''
        self.i = utils.pixel_to_index(self.center[0])
        self.j = utils.pixel_to_index(self.center[1])

    def place_bomb(self):
        if self.current_bombs < self.max_bombs:
            self.current_bombs += 1
            globals.bombs.append(Bomb(self.i, self.j, self))

    def render(self):
        pygame.draw.circle(
            globals.display,
            self.color,
            (int(self.center[0]), int(self.center[1])),
            globals.p_radious
        )
