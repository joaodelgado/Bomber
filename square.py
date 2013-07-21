import pygame
import globals


class Square(pygame.Rect):
    def __init__(self, i, j, owner):
        self.color = owner.inverted_color
        self.i = i
        self.j = j
        self.owner = owner
        super(Square, self).__init__(
            i*globals.square_size,
            j*globals.square_size,
            globals.square_size,
            globals.square_size)

    def change_owner(self, owner):
        self.owner = owner
        self.color = owner.inverted_color

    def render(self):
        pygame.draw.rect(globals.display, self.color, self)
