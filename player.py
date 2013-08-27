import math
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
        self.player_number = player_number


        self.keys = {
            "up": False,
            "down": False,
            "left": False,
            "right": False,
            "place": False,
        }

        if player_number == 1:
            self.images = globals.p1_images
            self.up = K_w
            self.down = K_s
            self.left = K_a
            self.right = K_d
            self.place = K_SPACE
        elif player_number == 2:
            self.images = globals.p2_images
            self.up = K_UP
            self.down = K_DOWN
            self.left = K_LEFT
            self.right = K_RIGHT
            self.place = K_p

        self.state = globals.P_S_STILL
        self.direction = globals.P_D_FRONT
        self.frame_timer = globals.animation_speed
        self.current_frame = 0
        self.frames = self.images[self.state][self.direction]
        self.max_bombs = 1
        self.current_bombs = 0
        self.bomb_radious = 2
        self.speed = 0.2
        self.update_center()

    def update_event(self, event):
        if event.type == KEYDOWN:
            if event.key == self.up:
                self.change_direction(globals.P_D_BACK)
                self.keys['up'] = True
            elif event.key == self.down:
                self.change_direction(globals.P_D_FRONT)
                self.keys['down'] = True
            elif event.key == self.left:
                self.change_direction(globals.P_D_LEFT)
                self.keys['left'] = True
            elif event.key == self.right:
                self.change_direction(globals.P_D_RIGHT)
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

        for key in self.keys:
            if self.keys[key]:
                self.change_state(globals.P_S_MOVING)
                break;
            else:
                self.change_state(globals.P_S_STILL)

    def update(self):
        self.frame_timer -= globals.clock.get_time()
        if self.frame_timer < 0:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.frame_timer = globals.animation_speed


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
        x, y = self.center[0] + dx, self.center[1] + dy
        left = x - (globals.square_size / 2)
        right = x + (globals.square_size / 2)
        top = y - (globals.square_size / 2)
        bottom = y + (globals.square_size / 2)
        index_x = utils.pixel_to_index(x)
        index_y = utils.pixel_to_index(y)
        index_left = utils.pixel_to_index(left)
        index_right = utils.pixel_to_index(right)
        index_top = utils.pixel_to_index(top)
        index_bottom = utils.pixel_to_index(bottom)

        #surrounding squares
        if globals.squares[index_left][index_y].owner != self:
            x = globals.square_size * index_left + \
                globals.square_size + (globals.square_size / 2)
        elif globals.squares[index_right][index_y].owner != self:
            x = globals.square_size * index_right - \
                (globals.square_size / 2)
        if globals.squares[index_x][index_top].owner != self:
            y = globals.square_size * index_top + \
                globals.square_size + (globals.square_size / 2)
        elif globals.squares[index_x][index_bottom].owner != self:
            y = globals.square_size * index_bottom - \
                (globals.square_size / 2)

        #recalculate variables
        left = x - (globals.square_size / 2)
        right = x + (globals.square_size / 2)
        top = y - (globals.square_size / 2)
        bottom = y + (globals.square_size / 2)

        #window borders
        if left < 0:
            x = (globals.square_size / 2)
        elif right >= globals.width:
            x = globals.width - (globals.square_size / 2) - 1
        if top < 0:
            y = (globals.square_size / 2)
        elif bottom >= globals.height:
            y = globals.height - (globals.square_size / 2) - 1

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

    def change_state(self, state):
        if self.state != state:
            self.state = state
            self.frame_timer = globals.animation_speed
            self.frames = self.images[self.state][self.direction]
            self.current_frame = 0

    def change_direction(self, direction):
        if self.direction != direction:
            self.direction = direction
            self.frame_timer = globals.animation_speed
            self.frames = self.images[self.state][self.direction]
            self.current_frame = 0

    def render(self):
        globals.display.blit(
            self.frames[self.current_frame],
            (
                self.center[0] - globals.square_size / 2,
                self.center[1] - globals.square_size / 2
            )
        )
