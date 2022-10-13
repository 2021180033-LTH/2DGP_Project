from pico2d import *
import random


class Ball:
    def __init__(self):
        self.image = load_image("ball.png")
        self.x = 400
        self.y = 90
        self.frame = 0

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 25, 25, self.x, self.y)


def handle_events():
    global running
    global dirx
    global diry
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_RIGHT:
                dirx += 1
            elif event.key == SDLK_LEFT:
                dirx -= 1
            elif event.key == SDLK_UP:
                diry -= 1
            elif event.key == SDLK_DOWN:
                diry += 1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dirx -= 1
            elif event.key == SDLK_LEFT:
                dirx += 1
            elif event.key == SDLK_UP:
                diry += 1
            elif event.key == SDLK_DOWN:
                diry -= 1

open_canvas()
ball = Ball()
dirx = 0
diry = 0
running = True

while running:
    clear_canvas()
    ball.draw()
    update_canvas()

    handle_events()
    ball.x += dirx * 0.5
    ball.y -= diry * 0.5
    delay(0.01)
