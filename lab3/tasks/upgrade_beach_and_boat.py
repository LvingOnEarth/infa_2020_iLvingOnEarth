from graph import *
import math

windowSize(400, 270)

def draw_sea(wave = 7):
    penColor(183, 177, 79)
    brushColor(66, 30, 224)
    rectangle(0, 125, 400, 185)

def draw_sand(wave = 14):
    brushColor(239, 246, 4)
    penColor(239, 246, 4)
    rectangle(0, 185, 400, 270)

    x1, y1, y2 = 15, 210, 160
    radius = 30

    for i in range(wave):
        if i % 2 == 0:
            penColor(239, 246, 4)
            brushColor(239, 246, 4)
            circle(x1 + i * 33, y1, radius)
        else:
            penColor(66, 30, 224)
            brushColor(66, 30, 224)
            circle(x1 + i * 33, y2, radius)

def draw_sun(length = 30):
    penColor(254, 247, 25)
    brushColor(255, 247, 23)
    # circle(350, 45, 25)

    bottom_length = length / 5

    polygon([(350, 45 - bottom_length), (350 + length, 45),
             (350, 45 + bottom_length), (350, 45 - bottom_length)])

    for i in range(36):
        alpha = (10 + 10 * i) / 2
        r = 2 * length * math.sin(alpha * (math.pi / 180))
        rx = r * math.cos((90 - alpha) * (math.pi / 180))
        ry = r * math.cos(alpha * (math.pi / 180))

        s = 2 * bottom_length * math.sin(alpha * (math.pi / 180))
        sx = s * math.cos(alpha * (math.pi / 180))
        sy = s * math.cos((90 - alpha) * (math.pi / 180))

        polygon([(350 - sx, 45 - bottom_length + sy), ((350 + length) - rx, 45 - ry),
                 (350 + sx, 45 + bottom_length - sy), (350 - sx, 45 - bottom_length + sy)])



def draw_clouds(size_x = 1, size_y = 1, x = 30, y = 25, step = 20):
    penColor(241, 241, 241)
    brushColor(255, 255, 255)

    x1 = x + step * size_x
    y1 = y + step * size_y
    x_koef_closely = 0.7 # how near will be circles of clouds to each other - horizontal
    y_koef_closely = 2.5 # how near will be circles of clouds to each other - vertical

    oval(x, y, x1, y1)
    oval(x + step * x_koef_closely, y, x1 + step * x_koef_closely, y1)

    oval(x - step / 2, y + step / y_koef_closely, x1 - step / 2, y1 + step / y_koef_closely)
    oval(x - step / 2 + step * x_koef_closely, y + step / y_koef_closely, x1 - step / 2 + step * x_koef_closely, y1 + step / y_koef_closely)
    oval(x - step / 2 + step * x_koef_closely * 2, y + step / y_koef_closely, x1 - step / 2 + step * x_koef_closely * 2, y1 + step / y_koef_closely)

    oval(x + step * x_koef_closely * 2, y, x1 + step * x_koef_closely * 2, y1)
    oval(x - step / 2 + step * x_koef_closely * 3, y + step / y_koef_closely, x1 - step / 2 + step * x_koef_closely * 3, y1 + step / y_koef_closely)

def draw_umbrella(size = 1, x = 75, y = 175):
    height = 80
    size_of_pen = 5 / size
    half_size_of_pen = size_of_pen / 2

    # bottom
    penSize(size_of_pen)
    penColor(228, 131, 18)
    line(x, y, x, height / size + y)
    penColor(244, 80, 80)
    line(x, y, x, y - 25 / size)

    # top
    penSize(1)
    penColor(195, 62, 62)
    brushColor(244, 80, 80)
    polygon([(x - half_size_of_pen - 35 / size, y), (x - half_size_of_pen, y - 25 / size),
             (x - half_size_of_pen, y), (x - half_size_of_pen - 35 / size, y)])
    polygon([(x + half_size_of_pen + 35 / size, y), (x + half_size_of_pen, y - 25 / size),
             (x + half_size_of_pen, y), (x + half_size_of_pen + 35 / size, y)])

    # black lines on umbrella
    penColor(197, 63, 63)
    for i in range(1, 4):
        line(x - half_size_of_pen - 35 / size + 7.5 / size * i, y, x - half_size_of_pen, y - 25 / size)
        line(x + half_size_of_pen + 35 / size - 7.5 / size * i, y, x + half_size_of_pen, y - 25 / size)


def draw_boats(size = 1):
    penColor(165, 70, 41)
    brushColor(187, 79, 1)
    rectangle(235, 135, 330, 160)
    polygon([(330, 160), (375, 135),
             (330, 135), (330, 160)])
    arc(260, 110, 210, 160, 180, 270)

    penSize(3)
    brushColor(255, 255, 255)
    penColor(0, 0, 0)
    circle(340, 143.5, 6)

    penSize(5)
    line(270, 135, 270, 75)

    penSize(1)
    penColor(170, 173, 132)
    brushColor(223, 214, 154)
    polygon([(272.5, 135), (285, 105),
             (310, 105), (272.5, 135)])
    polygon([(272.5, 75), (285, 105),
             (310, 105), (272.5, 75)])

def main():
    # sky
    penColor(82, 63, 229)
    brushColor(162, 245, 255)
    rectangle(0, 0, 400, 125)

    draw_sea()
    draw_sand()
    draw_sun()

    draw_clouds(1, 1, 30, 25, 20)
    draw_clouds(1, 1.1, 150, 10, 40)
    draw_clouds(1.4, 0.9, 50, 65, 30)

    draw_umbrella(size = 1, x = 75, y = 175)
    draw_umbrella(size = 1.5, x = 175, y = 200)

    draw_boats(1)
    draw_boats(2)


main()
run()