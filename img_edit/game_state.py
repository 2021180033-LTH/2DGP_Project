from pico2d import *
import game_framework
import random


class Ball:
    def __init__(self):
        self.image = load_image("ball.png")
        self.x, self.y = 400, 90
        self.frame = 0

    def update(self):
        global dirx
        self.x += dirx * 0.3
        if self.x > 800:
            self.x = 800
        elif self.x < 0:
            self.x = 0

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 25, 25, self.x, self.y)


def handle_events():
    global running
    global dirx
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = quit()
            elif event.key == SDLK_RIGHT:
                dirx += 1
            elif event.key == SDLK_LEFT:
                dirx -= 1
            elif event.key == SDLK_UP:
                for i in range(6):
                    ball.y += 1
                    delay(0.01)

                delay(0.01)

                for i in range(6):
                    ball.y -= 1
                    delay(0.01)
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dirx -= 1
            elif event.key == SDLK_LEFT:
                dirx += 1


running = True
ball = None
dirx = 0


def enter():
    global ball, running
    ball = Ball()
    running = True


def exit():
    global ball
    del ball


def update():
    ball.update()


def draw_world():
    ball.draw()


def draw():
    clear_canvas()
    draw_world()
    update_canvas()


def pause():
    pass


def resume():
    pass


def test_self():
    import sys
    this_module = sys.modules['__main__']
    pico2d.open_canvas()
    game_framework.run(this_module)
    pico2d.close_canvas()


if __name__ == '__main__':
    test_self()
