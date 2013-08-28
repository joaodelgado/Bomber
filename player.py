import math
from pygame.locals import *

import globals
import utils

from bomb import Bomb
from animation import Animation


class Player(object):
    def __init__(self, i, j, color, inverted_color, player_number):
        self.color = color
        self.inverted_color = inverted_color
        self.i = i
        self.j = j
        self.update_center()
        self.player_number = player_number


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

        self.state = globals.P_S_STILL
        self.direction = globals.P_D_FRONT

        self.animations = [
            [
            Animation(globals.p_images[self.player_number-1] \
                                      [globals.P_S_MOVING] \
                                      [globals.P_D_FRONT]),
            Animation(globals.p_images[self.player_number-1] \
                                      [globals.P_S_MOVING] \
                                      [globals.P_D_LEFT]),
            Animation(globals.p_images[self.player_number-1] \
                                      [globals.P_S_MOVING] \
                                      [globals.P_D_RIGHT]),
            Animation(globals.p_images[self.player_number-1] \
                                      [globals.P_S_MOVING] \
                                      [globals.P_D_BACK]),
            ],
            [
            Animation(globals.p_images[self.player_number-1] \
                                      [globals.P_S_STILL] \
                                      [globals.P_D_FRONT]),
            Animation(globals.p_images[self.player_number-1] \
                                      [globals.P_S_STILL] \
                                      [globals.P_D_LEFT]),
            Animation(globals.p_images[self.player_number-1] \
                                      [globals.P_S_STILL] \
                                      [globals.P_D_RIGHT]),
            Animation(globals.p_images[self.player_number-1] \
                                      [globals.P_S_STILL] \
                                      [globals.P_D_BACK]),
            ]
        ]
        self.current_animation = self.animations[self.state][self.direction]

        self.max_bombs = 1
        self.current_bombs = 0
        self.bomb_radious = 2
        self.speed = 0.2

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
                self.keys['place'] = Falsea

        if self.keys['left']:
            self.change_direction(globals.P_D_LEFT)
        elif self.keys['right']:
            self.change_direction(globals.P_D_RIGHT)
        elif self.keys['up']:
            self.change_direction(globals.P_D_BACK)
        elif self.keys['down']:
            self.change_direction(globals.P_D_FRONT)


        for key in self.keys:
            if self.keys[key]:
                self.change_state(globals.P_S_MOVING)
                break;
            else:
                self.change_state(globals.P_S_STILL)

    def update(self):
        self.current_animation.update()

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

        self.center = self.handle_collisions(dx, dy)
        self.update_index()

    def handle_collisions(self, dx, dy):
        x = self.center[0]
        y = self.center[1]
        #surrounding squares
        if dx:
            x += dx
            left = x - (globals.p_col_width / 2)
            right = x + (globals.p_col_width / 2)
            top = y - (globals.p_col_height / 2)
            bottom = y + (globals.p_col_height / 2)
            index_left = utils.pixel_to_index(left)
            index_right = utils.pixel_to_index(right)
            index_top = utils.pixel_to_index(top)
            index_bottom = utils.pixel_to_index(bottom)
            if globals.squares[index_left][index_top].owner != self or \
               globals.squares[index_left][index_bottom].owner != self or \
               globals.squares[index_right][index_top].owner != self or \
               globals.squares[index_right][index_bottom].owner != self:
                x -= dx
        if dy:
            y += dy
            left = x - (globals.p_col_width / 2)
            right = x + (globals.p_col_width / 2)
            top = y - (globals.p_col_height / 2)
            bottom = y + (globals.p_col_height / 2)
            index_left = utils.pixel_to_index(left)
            index_right = utils.pixel_to_index(right)
            index_top = utils.pixel_to_index(top)
            index_bottom = utils.pixel_to_index(bottom)
            if globals.squares[index_left][index_top].owner != self or \
               globals.squares[index_right][index_top].owner != self or \
               globals.squares[index_left][index_bottom].owner != self or \
               globals.squares[index_right][index_bottom].owner != self:
                y -= dy

        #window borders
        left = x - (globals.p_col_width / 2)
        right = x + (globals.p_col_width / 2)
        top = y - (globals.p_col_height / 2)
        bottom = y + (globals.p_col_height / 2)
        if left < 0:
            x -= dx
        elif right >= globals.width:
            x -= dx
        if top < 0:
            y -= dy
        elif bottom >= globals.height:
            y -= dy

        return (x, y)


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

    def change_state(self, state):
        if self.state != state:
            self.state = state
            self.change_animation()

    def change_direction(self, direction):
        if self.direction != direction:
            self.direction = direction
            self.change_animation()

    def change_animation(self):
        self.current_animation.stop()
        self.current_animation = self.animations[self.state][self.direction]
        self.current_animation.start()

    def render(self):
        self.current_animation.render (
            self.center[0] - globals.square_size / 2,
            self.center[1] - globals.square_size / 2
        )
