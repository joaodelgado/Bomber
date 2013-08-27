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
for frame in xrange(1, 3):
    path = os.path.join("res", "bomb_1_" + str(frame) + ".png")
    globals.b_1_images.append(load_image(path))
for frame in xrange(1, 3):
    path = os.path.join("res", "bomb_2_" + str(frame) + ".png")
    globals.b_2_images.append(load_image(path))



globals.b_1_images.append(pygame.image.load(os.path.join("res/bomb_1_1.png")))
globals.b_1_images.append(pygame.image.load(os.path.join("res/bomb_1_2.png")))
for i in range(len(globals.b_1_images)):
    globals.b_1_images[i] = pygame.transform.scale(
                                globals.b_1_images[i],
                                (globals.square_size, globals.square_size))
globals.b_1_images.append(pygame.image.load(os.path.join("res/bomb_1_1.png")))
globals.b_1_images.append(pygame.image.load(os.path.join("res/bomb_1_2.png")))
for i in range(len(globals.b_1_images)):
    globals.b_1_images[i] = pygame.transform.scale(
                                globals.b_1_images[i],
                                (globals.square_size, globals.square_size))


##############################################################################
#                                 GAME LOGIC                                 #
##############################################################################
def update():
    last_game_state = globals.game_state_label

    for event in pygame.event.get():
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
