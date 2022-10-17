from pico2d import *
import game_framework


class Wall:
    def __init__(self):
        self.image = load_image("steel_block21X21.png")
        self.x, self.y = 16, 180
        self.gap = 32

    def draw(self):
        self.image.clip_draw(0, 0, 32, 32, self.x, self.y)


wall1 = None


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()


def enter():
    global wall1

    wall1 = Wall()


def exit():
    global wall1
    del wall1


def update():
    pass


def draw():
    clear_canvas()
    draw_world()
    update_canvas()


def draw_world():
    wall1.draw()


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
