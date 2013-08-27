import globals

from animation import Animation

class Explosion(object):
    def __init__(self, i, j):
        self.color = globals.orange
        self.i = i
        self.j = j
        player = globals.squares[i][j].owner.player_number - 1
        self.animation = Animation(
            frames=globals.e_images[player],
            speed=globals.animation_speed / 3,
            loop=False
        )

    def update(self):
        self.animation.update()

        if not self.animation.running:
            globals.explosions.remove(self)

    def render(self):
        self.animation.render(
            self.i * globals.square_size,
            self.j * globals.square_size,
        )
