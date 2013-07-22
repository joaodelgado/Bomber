from pygame.locals import *

import globals

from player import Player
from square import Square


class Game(object):
    def __init__(self):
        del globals.squares[0:len(globals.squares)]

        self.p1 = Player(4, 4, globals.white, globals.black, 1)
        self.p2 = Player(14, 4, globals.black, globals.white, 2)

        #initialize squares
        for i in range(globals.squares_per_line):
            globals.squares.append([])
            for j in range(globals.squares_per_column):
                globals.squares[i].append(Square(i, j, self.p2))

        for column in globals.squares[:len(globals.squares)/2]:
            for square in column:
                square.change_owner(self.p1)

        del globals.bombs[0:len(globals.bombs)]
        del globals.explosions[0:len(globals.explosions)]
        del globals.powerups[0:len(globals.powerups)]

    def update_event(self, event):
        if event.type == QUIT:
            globals.game_state_label = globals.EXIT
        elif event.type == KEYDOWN:
            self.p1.update(event)
            self.p2.update(event)

    def update(self):
        for powerup in globals.powerups:
            powerup.update()
            if powerup.i == self.p1.i and \
               powerup.j == self.p1.j:
                powerup.pickup(self.p1)
            if powerup.i == self.p2.i and \
               powerup.j == self.p2.j:
                powerup.pickup(self.p2)

        for bomb in globals.bombs:
            bomb.update()

        for explosion in globals.explosions:
            explosion.update()
            # checks if a player was hit by an explosion
            if explosion.i == self.p1.i and \
               explosion.j == self.p1.j or  \
               explosion.i == self.p2.i and \
               explosion.j == self.p2.j:
                globals.game_state_label = globals.MAIN_MENU

        # checks if a player is in a square that he doesn't own
        if globals.squares[self.p1.i][self.p1.j].owner != self.p1 or \
           globals.squares[self.p2.i][self.p2.j].owner != self.p2:
            globals.game_state_label = globals.MAIN_MENU

    def render(self):
        for line in globals.squares:
            for rect in line:
                rect.render()

        for powerup in globals.powerups:
            powerup.render()

        for bomb in globals.bombs:
            bomb.render()

        for explosion in globals.explosions:
            explosion.render()

        self.p1.render()
        self.p2.render()
