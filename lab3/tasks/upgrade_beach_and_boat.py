from graph import *
import math

x_window_size = 400
y_window_size = 270

# x_window_size = 600
# y_window_size = 500

windowSize(x_window_size, y_window_size)

y_top_bottom = []

def calculate_top_bottom_sky_sea_sand():
    y_fill = (0.46, 0.23, 0.31)
    y_top = 0
    y_bottom = 0

    for i in range(len(y_fill)):
        if i != 0:
            y_top = y_bottom

        y_bottom += y_window_size * y_fill[i]

        y_top_bottom.append([y_top, y_bottom])

def draw_sky(y_top_bottom_arr):
    penColor(162, 245, 255)
    brushColor(162, 245, 255)

    x_top, x_bottom = 0, x_window_size
    y_top, y_bottom = y_top_bottom_arr

    rectangle(x_top, y_top, x_bottom, y_bottom)

def draw_sea(y_top_bottom_arr):
    penColor(66, 30, 224)
    brushColor(66, 30, 224)

    x_top, x_bottom = 0, x_window_size
    y_top, y_bottom = y_top_bottom_arr

    rectangle(x_top, y_top, x_bottom, y_bottom)

def draw_sand(y_top_bottom_arr, radius = 30):
    brushColor(239, 246, 4)
    penColor(239, 246, 4)

    x_top, x_bottom = 0, x_window_size
    y_top, y_bottom = y_top_bottom_arr

    rectangle(x_top, y_top, x_bottom,  y_bottom)

    count_of_sand_waves = x_window_size // radius
    x1 = 15
    y_top_circle = y_top - radius * 0.86
    y_bottom_circle = y_top + radius * 0.86
    # x1, y1, y2 = 15, 210, 160

    for i in range(count_of_sand_waves):
        if i % 2 == 0:
            penColor(239, 246, 4)
            brushColor(239, 246, 4)
            circle(x1 + i * 33, y_bottom_circle, radius)
        else:
            penColor(66, 30, 224)
            brushColor(66, 30, 224)
            circle(x1 + i * 33, y_top_circle, radius)

def draw_sun(length = 30):
    penColor(254, 247, 25)
    brushColor(255, 247, 23)

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


def draw_boats(size = 1, x = 235, y = 135):
    penColor(165, 70, 41)
    brushColor(187, 79, 1)

    x_length = 95 * size
    y_length = 25 * size

    x1 = x + x_length
    y1 = y + y_length

    rectangle(x, y, x1, y1)
    polygon([(x1, y1), (x1 + 45 * size, y),
             (x1, y), (x1, y1)])
    arc(x - y_length, y - y_length, x + y_length, y1, 180, 270)

    penSize(3 * size)
    brushColor(255, 255, 255)
    penColor(0, 0, 0)
    circle(x1 + 10 * size, y1 - 16.5 * size, 6 * size)

    penSize(5 * size)
    line(x + (x1 - x) / 2 - 15 * size, y, x + (x1 - x) / 2 - 15 * size, y - 60 * size)

    penSize(1)
    penColor(170, 173, 132)
    brushColor(223, 214, 154)
    polygon([(x + (x1 - x) / 2 - 15 * size + (5 * size) / 2, y),
             (x + (x1 - x) / 2 - 15 * size + (5 * size) / 2 + 12.5 * size, y - (y - (y - 60 * size)) / 2),
             (x + (x1 - x) / 2 - 15 * size + (5 * size) / 2 + 37.5 * size, y - (y - (y - 60 * size)) / 2),
             (x + (x1 - x) / 2 - 15 * size + (5 * size) / 2, y)])
    polygon([(x + (x1 - x) / 2 - 15 * size + (5 * size) / 2, y - 60 * size),
             (x + (x1 - x) / 2 - 15 * size + (5 * size) / 2 + 12.5 * size, y - (y - (y - 60 * size)) / 2),
             (x + (x1 - x) / 2 - 15 * size + (5 * size) / 2 + 37.5 * size, y - (y - (y - 60 * size)) / 2),
             (x + (x1 - x) / 2 - 15 * size + (5 * size) / 2, y - 60 * size)])

def main():
    calculate_top_bottom_sky_sea_sand()

    draw_sky(y_top_bottom_arr = y_top_bottom[0])
    draw_sea(y_top_bottom_arr = y_top_bottom[1])
    draw_sand(y_top_bottom_arr = y_top_bottom[2])

    draw_sun()

    draw_clouds(1, 1, 30, 25, 20)
    draw_clouds(1, 1.1, 150, 10, 40)
    draw_clouds(1.4, 0.9, 50, 65, 30)

    draw_umbrella(size = 1, x = 75, y = 175)
    draw_umbrella(size = 1.5, x = 175, y = 200)

    draw_boats(size = 1, x = 235, y = 135)
    draw_boats(size = 0.5, x = 130, y = 150)


main()
run()