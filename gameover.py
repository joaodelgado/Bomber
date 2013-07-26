import pygame
from pygame.locals import *

import globals


class Gameover(object):
    def __init__(self):
        self.list = []

        self.font_normal = pygame.font.SysFont('FreeMono', 30)
        self.font_bold = pygame.font.SysFont('FreeMono', 30, bold=True)

        self.list.append({
            'text': 'Continue',
            'color': globals.red,
            'x': globals.width / 2,
            'state': globals.RUNNING
        })
        self.list.append({
            'text': 'Main Menu',
            'color': globals.white,
            'x': globals.width / 2,
            'state': globals.MAIN_MENU
        })

        list_height = self.font_normal.get_height() * len(self.list)
        start_y = globals.height/4*3 - list_height/2
        for i in range(len(self.list)):
            self.list[i]['y'] = start_y + self.font_normal.get_height() * i

        self.current = 0

        self.scores = []
        self.scores.append({
            'text': 'Player 1',
            'color': globals.white,
            'x': globals.width / 4,
            'y': globals.height / 4
        })
        self.scores.append({
            'text': str(globals.player1_score),
            'color': globals.white,
            'x': globals.width / 4,
            'y': globals.height / 4 + self.font_normal.get_height()
        })
        self.scores.append({
            'text': 'Player 2',
            'color': globals.white,
            'x': globals.width / 4 * 3,
            'y': globals.height / 4
        })
        self.scores.append({
            'text': str(globals.player2_score),
            'color': globals.white,
            'x': globals.width / 4 * 3,
            'y': globals.height / 4 + self.font_normal.get_height()
        })

        if globals.player1_score != globals.player2_score:
            if globals.player1_score > globals.player2_score:
                self.scores[1]['color'] = globals.green
            else:
                self.scores[-1]['color'] = globals.green

    def update_event(self, event):
        if event.type == QUIT:
            globals.game_state = globals.EXIT
        elif event.type == KEYDOWN:
            if event.key == K_RETURN:
                globals.game_state_label = self.list[self.current]['state']
            elif event.key == K_UP:
                self.current -= 1
            elif event.key == K_DOWN:
                self.current += 1

            if self.current < 0:
                self.current = len(self.list) - 1
            elif self.current == len(self.list):
                self.current = 0

            for i in range(len(self.list)):
                if i != self.current:
                    self.list[i]['color'] = globals.white
                else:
                    self.list[i]['color'] = globals.red

    def update(self):
        pass

    def render(self):
        font = self.font_normal
        for label in self.list + self.scores:
            image = font.render(label['text'], 1, label['color'])
            globals.display.blit(
                image,
                (
                    label['x'] - image.get_width()/2,
                    label['y'] - image.get_height()/2,
                )
            )
