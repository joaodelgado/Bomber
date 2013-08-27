import globals


class Explosion(object):
    def __init__(self, i, j):
        self.color = globals.orange
        self.i = i
        self.j = j
        player = globals.squares[i][j].owner.player_number
        self.frames = globals.e_images[player-1]
        self.frame_timer = globals.animation_speed / 3
        self.current_frame = 0

    def update(self):
        self.frame_timer -= globals.clock.get_time()

        if self.frame_timer < 0:
            self.current_frame += 1
            self.frame_timer = globals.animation_speed / 3

        if self.current_frame == len(self.frames):
            globals.explosions.remove(self)

    def render(self):
        globals.display.blit(
            self.frames[self.current_frame],
            (
                self.i * globals.square_size,
                self.j * globals.square_size,
            )
        )
