from random import choice

import globals

from animation import Animation

def bigger_bombs(player):
    player.bomb_radious += 0.5
    player.bomb_radious = min(player.bomb_radious, 5)


def increase_bombs(player):
    player.max_bombs += 1
    player.max_bombs = min(player.max_bombs, 5)


def increase_speed(player):
    player.speed += 0.05
    player.speed = min(player.speed, 0.4)

powerups = []


def init_powerups():
    global powerups
    # function and image for each player
    powerups = [
        bigger_bombs,
        increase_bombs,
        increase_speed
    ]

class Powerup(object):
    def __init__(self, i, j):
        global powerups
        init_powerups()
        self.i = i
        self.j = j
        self.timer = globals.pw_timer
        self.powerup = choice(powerups)
        index = powerups.index(self.powerup)
        player = globals.squares[i][j].owner.player_number-1
        self.animation = Animation(globals.pw_images[index][player])

    def update(self):
        self.timer -= globals.clock.get_time()
        if self.timer < 0:
            globals.powerups.remove(self)

        self.animation.update()

    def pickup(self, player):
        self.powerup(player)
        globals.powerups.remove(self)

    def render(self):
        self.animation.render(
            self.i * globals.square_size,
            self.j * globals.square_size,
        )
