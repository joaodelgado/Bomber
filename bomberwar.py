import sys
import pygame
from pygame.locals import *

# import pdb

import globals

from player import Player
from square import Square

##############################
# INITIALIZATION
###################d###########
pygame.init()

running = True

globals.screen = pygame.display.set_mode([globals.width, globals.height])
globals.display = pygame.display.get_surface()
globals.clock = pygame.time.Clock()

player1 = Player(4, 4, globals.white, globals.black, 1)
player2 = Player(14, 4, globals.black, globals.white, 2)

#initialize squares
for i in range(globals.squares_per_line):
    globals.squares.append([])
    for j in range(globals.squares_per_column):
        globals.squares[i].append(Square(i, j, player2))

for column in globals.squares[:len(globals.squares)/2]:
    for square in column:
        square.change_owner(player1)


##############################
# GAME LOGIC
##############################
def update():
    global running
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        player1.update(event)
        player2.update(event)

    for bomb in globals.bombs:
        bomb.update()

    for explosion in globals.explosions:
        explosion.update()
        # checks if a player was hit by an explosion
        if explosion.i == player1.i and \
           explosion.j == player1.j or  \
           explosion.i == player2.i and \
           explosion.j == player2.j:
            running = False

    # checks if a player is in a square that he doesn't own
    if globals.squares[player1.i][player1.j].owner != player1 or \
       globals.squares[player2.i][player2.j].owner != player2:
        running = False


##############################
# DRAWING
##############################
def render():
    globals.screen.fill(globals.black)

    for line in globals.squares:
        for rect in line:
            rect.render()

    for bomb in globals.bombs:
        bomb.render()

    for explosion in globals.explosions:
        explosion.render()

    player1.render()
    player2.render()
    pygame.display.flip()


##############################
# MAIN LOOP
##############################
while running:
    update()
    render()
    globals.clock.tick(60)
