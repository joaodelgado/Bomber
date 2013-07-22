import pygame
from pygame.locals import *

import globals

from mainmenu import Mainmenu
from game import Game

##############################################################################
#                               INITIALIZATION                               #
##############################################################################
pygame.init()

globals.screen = pygame.display.set_mode([globals.width, globals.height])
globals.display = pygame.display.get_surface()
globals.clock = pygame.time.Clock()


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


##############################################################################
#                                 MAIN LOOP                                  #
##############################################################################
change_game_state()
while globals.game_state_label != globals.EXIT:
    update()
    render()
    globals.clock.tick(60)
