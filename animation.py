import globals

class Animation(object):
    def __init__(self, frames, speed=globals.animation_speed, loop=True):
        self.frames = frames
        self.speed = speed
        self.frame_timer = self.speed
        self.nframes = len(frames)
        self.current_frame = 0
        self.running = True
        self.loop = loop

    def start(self):
        self.current_frame = 0
        self.frame_timer = self.speed
        self.running = True

    def stop(self):
        self.running = False

    def update(self):
        if self.running:
            if self.current_frame < self.nframes:  # if this fails, then loop=False
                self.frame_timer -= globals.clock.get_time()

                if self.frame_timer < 0:
                    self.current_frame += 1
                    if self.loop:
                        self.current_frame %= self.nframes
                    self.frame_timer = self.speed
            else:
                self.running = False

    def render(self, x, y):
        if self.current_frame < self.nframes:
            globals.display.blit(self.frames[self.current_frame], (x, y))
