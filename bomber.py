import os
import pygame
from pygame.locals import *

import globals

from mainmenu import Mainmenu
from game import Game
from gameover import Gameover

##############################################################################
#                               INITIALIZATION                               #
##############################################################################
pygame.init()

globals.screen = pygame.display.set_mode([globals.width, globals.height])
globals.display = pygame.display.get_surface()
globals.clock = pygame.time.Clock()


def load_image(path):
    image = pygame.image.load(path)
    image = pygame.transform.scale(
                image,
                (globals.square_size, globals.square_size))
    return image

# Load bomb images
for player in xrange(1, 3):
    globals.b_images.append([])
    for frame in xrange(1, 3):
        path = os.path.join("res", "bomb_" + str(player) + "_" + str(frame) + ".png")
        globals.b_images[-1].append(load_image(path))

# Load explosion images
for player in xrange(1, 3):
    globals.e_images.append([])
    for frame in xrange(1, 7):
        path = os.path.join("res", "explosion_" + str(player) + "_" + str(frame) + ".png")
        globals.e_images[-1].append(load_image(path))

# Load player images
for player in xrange(1, 3):
    globals.p_images.append([])

    # Moving
    globals.p_images[-1].append([])
    for direction in xrange(1,5):
        globals.p_images[-1][-1].append([])
        for frame in xrange(1, 3):
            path = os.path.join("res", "player_" + str(player) + "_1_" + str(direction) + "_" + str(frame) + ".png")
            globals.p_images[-1][-1][-1].append(load_image(path))
    # Still
    globals.p_images[-1].append([])
    for direction in xrange(1,5):
        globals.p_images[-1][-1].append([])
        for frame in xrange(1, 2):
            path = os.path.join("res", "player_" + str(player) + "_2_" + str(direction) + "_" + str(frame) + ".png")
            globals.p_images[-1][-1][-1].append(load_image(path))

# Load power ups
for powerup in xrange(1, 4):
    globals.pw_images.append([])
    for player in xrange(1, 3):
        globals.pw_images[-1].append([])
        for frame in xrange(1, 2):
            path = os.path.join("res", "pw_" + str(powerup) + "_" + str(player) + "_" + str(frame) + ".png")
            globals.pw_images[-1][-1].append(load_image(path))


##############################################################################
#                                 GAME LOGIC                                 #
##############################################################################
def update():
    last_game_state = globals.game_state_label

    for event in pygame.event.get():
        if event.type == QUIT:
            globals.game_state_label = globals.EXIT
        else:
            globals.game_state.update_event(event)
    globals.game_state.update()

    if globals.game_state_label != last_game_state:
        change_game_state()


##############################################################################
#                                  DRAWING                                   #
##############################################################################
def render():
    globals.screen.fill(globals.black)
    globals.game_state.render()
    pygame.display.flip()


##############################################################################
#                                   OTHER                                    #
##############################################################################
def change_game_state():
    gs = globals.game_state_label

    if gs == globals.MAIN_MENU:
        globals.game_state = Mainmenu()
    elif gs == globals.RUNNING:
        globals.game_state = Game()
    elif gs == globals.GAME_OVER:
        globals.game_state = Gameover()


##############################################################################
#                                 MAIN LOOP                                  #
##############################################################################
change_game_state()
while globals.game_state_label != globals.EXIT:
    update()
    render()
    globals.clock.tick(60)
