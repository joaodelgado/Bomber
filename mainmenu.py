import pygame
from pygame.locals import *

import globals


class Mainmenu(object):
    def __init__(self):
        self.list = []

        self.font_normal = pygame.font.SysFont('FreeMono', 30)
        self.font_bold = pygame.font.SysFont('FreeMono', 30, bold=True)

        self.list.append({
            'text': 'Play',
            'color': globals.red,
            'x': 40,
            'state': globals.RUNNING
        })
        self.list.append({
            'text': 'Exit',
            'color': globals.white,
            'x': 40,
            'state': globals.EXIT
        })

        for i in range(len(self.list)):
            self.list[i]['y'] = 100 + self.font_normal.get_height() * i

        self.current = 0

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
        for label in self.list:
            image = font.render(label['text'], 1, label['color'])
            globals.display.blit(image, (label['x'], label['y']))
