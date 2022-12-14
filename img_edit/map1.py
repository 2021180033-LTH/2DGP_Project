from pico2d import *
import game_framework


class Map1:
    def __init__(self):
        self.image1 = load_image("vertex_steel_block.png")
        self.image2 = load_image("vertical_steel_block.png")
        self.image3 = load_image("vertical_steel_block.png")
        self.x_h, self.y_h = 400, 180
        self.x_v1, self.y_v = 138, 253
        self.x_v2 = 661.5
        self.gap = 32

    def draw(self):
        self.image1.clip_draw(0, 0, 550, 25, self.x_h, self.y_h)
        self.image2.clip_draw(0, 0, 25, 120, self.x_v1, self.y_v)
        self.image3.clip_draw(0, 0, 25, 120, self.x_v2, self.y_v)