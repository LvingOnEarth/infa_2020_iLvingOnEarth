from graph import *

windowSize(400, 270)

def draw_sea(wave = 7):
    penColor(183, 177, 79)
    brushColor(66, 30, 224)
    rectangle(0, 125, 400, 185)

    # for i in range(1, wave + 1):
    #     circle(28 * i, 185, 14)

def draw_sand(wave = 7):
    brushColor(239, 246, 4)
    rectangle(0, 185, 400, 270)
    circle(28, 195, 14)

def draw_sun(radius = 25):
    penColor(254, 247, 25)
    brushColor(255, 247, 23)
    circle(350, 45, radius)

def draw_clouds(size = 1, radius = 10):
    penColor(241, 241, 241)
    brushColor(255, 255, 255)

    x = 85
    step = 15

    circle(x + step, 35, radius)
    circle(x + 2 * step, 35, radius)

    circle(x + 5, 45, radius)
    circle(x + 5 + step, 45, radius)
    circle(x + 5 + 2 * step, 45, radius)

    circle(x + 3 * step, 35, radius)
    circle(x + 5 + 3 * step, 45, radius)

def draw_umbrella(x, y, size = 1):
    # bottom
    penSize(5 / size)
    penColor(228, 131, 18)
    line(x, y, x, 255)
    penColor(244, 80, 80)
    line(75, 175, 75, 150)
    # top
    penSize(1)
    penColor(195, 62, 62)
    brushColor(244, 80, 80)
    polygon([(35, 175), (72.5, 150),
             (72.5, 175), (35, 175)])
    polygon([(77.5, 175), (77.5, 150),
             (117.5, 175), (77.5, 175)])
    penColor(197, 63, 63)
    line(45, 175, 72.5, 150)
    line(55, 175, 72.5, 150)
    line(65, 175, 72.5, 150)
    line(107, 175, 77.5, 150)
    line(97, 175, 77.5, 150)
    line(87, 175, 77.5, 150)

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

    draw_clouds(1, 10)
    draw_clouds(2, 10)
    draw_clouds(3, 10)

    draw_umbrella(75, 175, 1)
    draw_umbrella(175, 190, 2)

    draw_boats(1)
    draw_boats(2)

main()
run()