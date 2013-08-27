from random import choice

import globals


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
        (bigger_bombs, [None, globals.pw_images[0], globals.pw_images[1]]),
        (increase_bombs, [None, globals.pw_images[2], globals.pw_images[3]]),
        (increase_speed, [None, globals.pw_images[4], globals.pw_images[5]])
    ]

class Powerup(object):
    def __init__(self, i, j):
        global powerups
        init_powerups()
        self.i = i
        self.j = j
        pw = choice(powerups)
        player = globals.squares[i][j].owner.player_number
        self.image = pw[1][player]
        self.powerup = pw[0]
        self.timer = 5000

    def update(self):
        self.timer -= globals.clock.get_time()
        if self.timer < 0:
            globals.powerups.remove(self)

    def pickup(self, player):
        self.powerup(player)
        globals.powerups.remove(self)

    def render(self):
        globals.display.blit(
            self.image,
            (
                self.i * globals.square_size,
                self.j * globals.square_size,
            )
        )
