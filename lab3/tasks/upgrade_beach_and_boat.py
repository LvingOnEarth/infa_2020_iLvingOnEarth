from graph import *
import math

X_WINDOW_SIZE = 400
Y_WINDOW_SIZE = 270

# x_window_size = X_WINDOW_SIZE
# y_window_size = Y_WINDOW_SIZE

x_window_size = X_WINDOW_SIZE * 1.5
y_window_size = Y_WINDOW_SIZE * 1.5

# x_window_size = X_WINDOW_SIZE * 2.5
# y_window_size = Y_WINDOW_SIZE * 2.5

x_koef_screen = x_window_size / X_WINDOW_SIZE
y_koef_screen = y_window_size / Y_WINDOW_SIZE

windowSize(x_window_size, y_window_size)
canvasSize(x_window_size + 100, y_window_size + 100)

def calculate_top_bottom_sky_sea_sand():
    y_top_bottom_arr = []
    y_fill = (0.46, 0.23, 0.31)
    y_top = 0
    y_bottom = 0

    for i in range(len(y_fill)):
        if i != 0:
            y_top = y_bottom

        y_bottom += y_window_size * y_fill[i]

        y_top_bottom_arr.append([y_top, y_bottom])

    return y_top_bottom_arr

def draw_sky(y_top_bottom_arr):
    penColor(162, 245, 255)
    brushColor(162, 245, 255)

    x_top, x_bottom = 0, x_window_size
    y_top, y_bottom = y_top_bottom_arr

    sky = rectangle(x_top, y_top, x_bottom, y_bottom)

    return sky

def draw_sea(y_top_bottom_arr):
    penColor(66, 30, 224)
    brushColor(66, 30, 224)

    x_top, x_bottom = 0, x_window_size
    y_top, y_bottom = y_top_bottom_arr

    sea = rectangle(x_top, y_top, x_bottom, y_bottom)

    return sea

def draw_sand(y_top_bottom_arr, radius = 30, x1 = 15):
    brushColor(239, 246, 4)
    penColor(239, 246, 4)

    arr_circles = []

    x_top, x_bottom = 0, x_window_size
    y_top, y_bottom = y_top_bottom_arr

    sand = rectangle(x_top, y_top, x_bottom + 100,  y_bottom)

    arr_circles.append(sand)

    count_of_sand_waves = int(x_window_size // radius)
    # x1 *= cycle
    y_top_circle = y_top - radius * 0.86
    y_bottom_circle = y_top + radius * 0.86

    for i in range(count_of_sand_waves):
        if i % 2 == 0:
            penColor(239, 246, 4)
            brushColor(239, 246, 4)
            circ = circle(x1 + i * 33, y_bottom_circle, radius)
        else:
            penColor(66, 30, 224)
            brushColor(66, 30, 224)
            circ = circle(x1 + i * 33, y_top_circle, radius)

        arr_circles.append(circ)

    return arr_circles

def draw_sun(triangle_length = y_window_size * 0.11, alpha = 10):
    penColor(254, 247, 25)
    brushColor(255, 247, 23)

    arr_sun = []

    angle_of_triangle_turn = alpha

    half_bottom_triangle_length = triangle_length / 5

    x_center_of_sun = x_window_size * 0.88
    y_center_of_sun = y_window_size * 0.17

    x_triangle_point_1 = x_center_of_sun
    y_triangle_point_1 = y_center_of_sun - half_bottom_triangle_length

    x_triangle_point_2 = x_center_of_sun + triangle_length
    y_triangle_point_2 = y_center_of_sun

    x_triangle_point_3 = x_center_of_sun
    y_triangle_point_3 = y_center_of_sun + half_bottom_triangle_length


    # if alpha == 10:
    sunray = polygon([(x_triangle_point_1, y_triangle_point_1), (x_triangle_point_2, y_triangle_point_2),
                (x_triangle_point_3, y_triangle_point_3), (x_triangle_point_1, y_triangle_point_1)])

    arr_sun.append(sunray)

    for i in range(36):
        alpha = (angle_of_triangle_turn + angle_of_triangle_turn * i) / 2
        r = 2 * triangle_length * math.sin(alpha * (math.pi / 180))
        rx = r * math.cos((90 - alpha) * (math.pi / 180))
        ry = r * math.cos(alpha * (math.pi / 180))

        s = 2 * half_bottom_triangle_length * math.sin(alpha * (math.pi / 180))
        sx = s * math.cos(alpha * (math.pi / 180))
        sy = s * math.cos((90 - alpha) * (math.pi / 180))

        sunray = polygon([(x_triangle_point_1 - sx, y_triangle_point_1 + sy), (x_triangle_point_2 - rx, y_triangle_point_2 - ry),
                 (x_triangle_point_3 + sx, y_triangle_point_3 - sy), (x_triangle_point_1 - sx, y_triangle_point_1 + sy)])

        arr_sun.append(sunray)

    return arr_sun

def calculate_point_of_cloud_circle(size_x, size_y, x, y, step):
    '''
    :param size_x: size of circle in x coordinate
    :param size_y: size of circle in y coordinate
    :param x: x coordinate for first circle
    :param y: y coordinate for first circle
    :param step: start of next circle of a cloud
    :return: array (point_of_clouds_arr) with coordinate for all circles
    '''
    point_of_clouds_arr = []

    x_independent = x * x_koef_screen
    y_independent = y * y_koef_screen

    size_x *= x_koef_screen
    size_y *= y_koef_screen

    x_koef_closely = 0.7  # how near will be circles of clouds to each other - horizontal
    y_koef_closely = 2.5  # how near will be circles of clouds to each other - vertical

    step_x = step * x_koef_closely * x_koef_screen
    step_y = step // y_koef_closely * y_koef_screen

    circles_in_row_1 = 3
    circles_in_row_2 = 4

    for i in range(circles_in_row_1 - 1):
        x1 = x_independent + step_x * i
        y1 = y_independent

        x2 = x1 + step * size_x
        y2 = y1 + step * size_y

        point_of_clouds_arr.append([x1, y1, x2, y2])

    for i in range(circles_in_row_2 + 1):
        if i != 3:
            if i < 3:
                x1 = x_independent - step // 2 + step_x * i
            else:
                x1 = x_independent - step // 2 + step_x * (circles_in_row_2 - 1)
            y1 = y_independent + step_y

            x2 = x1 + step * size_x
            y2 = y1 + step * size_y

        else:
            x1 = x_independent + step_x * (circles_in_row_1 - 1)
            y1 = y_independent

            x2 = x1 + step * size_x
            y2 = y1 + step * size_y

        point_of_clouds_arr.append([x1, y1, x2, y2])

    return point_of_clouds_arr

def draw_clouds(size_x = 1, size_y = 1, x = 30, y = 25, step = 20):
    penColor(241, 241, 241)
    brushColor(255, 255, 255)

    arr_clouds = []

    point_of_clouds_arr = calculate_point_of_cloud_circle(size_x, size_y, x, y, step)

    for i in point_of_clouds_arr:
        circle_of_cloud = oval(i[0], i[1], i[2], i[3])
        arr_clouds.append(circle_of_cloud)

    return arr_clouds

def draw_umbrella(size = 1, x = 75, y = 175):
    x *= x_koef_screen
    y *= y_koef_screen

    arr_umbrella = []

    height = 80 * y_koef_screen
    size_of_pen = 5 / size * y_koef_screen
    half_size_of_pen = size_of_pen // 2

    # bottom
    penSize(size_of_pen)
    penColor(228, 131, 18)
    line_bottom = line(x, y, x, height // size + y)
    penColor(244, 80, 80)
    line_top = line(x, y, x, y - 25 // size * y_koef_screen)

    arr_umbrella.append(line_bottom)
    arr_umbrella.append(line_top)

    # top
    penSize(1)
    penColor(195, 62, 62)
    brushColor(244, 80, 80)

    x1_left = x - half_size_of_pen - 35 / size * x_koef_screen
    x1_right = x + half_size_of_pen + 35 / size * x_koef_screen
    y1 = y

    x2_left = x - half_size_of_pen
    x2_right = x + half_size_of_pen
    y2 = y - 25 / size * y_koef_screen

    x3_left = x - half_size_of_pen
    x3_right = x + half_size_of_pen
    y3 = y

    # left triangle
    left_triangle = polygon([(x1_left, y1), (x2_left, y2),
             (x3_left, y3), (x1_left, y1)])

    # right triangle
    right_triangle = polygon([(x1_right, y1), (x2_right, y2),
             (x3_right, y3), (x1_right, y1)])

    arr_umbrella.append(left_triangle)
    arr_umbrella.append(right_triangle)

    # black lines on umbrella
    penColor(197, 63, 63)
    for i in range(1, 5):
        left_line = line(x1_left + 7.5 / size * x_koef_screen * i, y1, x2_left, y2)
        right_line = line(x1_right - 7.5 / size * x_koef_screen * i, y1, x2_right, y2)

        arr_umbrella.append(left_line)
        arr_umbrella.append(right_line)

    return arr_umbrella

def draw_boats(size = 1, x = 235, y = 135, direction = 'right'):
    penColor(165, 70, 41)
    brushColor(187, 79, 1)

    arr_boat = []

    x *= x_koef_screen
    y *= y_koef_screen

    x_length = 95 * size * x_koef_screen
    y_length = 25 * size * y_koef_screen

    if direction == 'right':

        x1 = x + x_length
        y1 = y + y_length

        mid_of_boat = rectangle(x, y, x1, y1)
        right_of_boat = polygon([(x1, y1), (x1 + 45 * size * x_koef_screen, y),
                 (x1, y), (x1, y1)])
        left_of_boat = arc(x - y_length, y - y_length, x + y_length, y1, 180, 270)

        penSize(3 * size * x_koef_screen)
        penColor(0, 0, 0)
        brushColor(255, 255, 255)

        circ_of_boat = circle(x1 + 10 * size * x_koef_screen, y1 - 16.5 * size * y_koef_screen, 6 * size * x_koef_screen)

        penSize(5 * size * x_koef_screen)
        mast_of_boat = line(x + (x1 - x) / 2 - 15 * size * x_koef_screen, y, x + (x1 - x) / 2 - 15 * size * x_koef_screen, y - 60 * size * y_koef_screen)

        penSize(1)
        penColor(170, 173, 132)
        brushColor(223, 214, 154)

        # ship sails
        x1_for_both = x + (x1 - x) / 2 - 15 * size * x_koef_screen + (5 * size * x_koef_screen) / 2
        y1_bottom = y
        y1_top = y - 60 * size * y_koef_screen

        x2_for_both = x + (x1 - x) / 2 - 15 * size * x_koef_screen + (5 * size * x_koef_screen) / 2 + 12.5 * size * x_koef_screen
        y2_for_both = y - (y - (y - 60 * size * y_koef_screen)) / 2

        x3_for_both = x + (x1 - x) / 2 - 15 * size * x_koef_screen + (5 * size * x_koef_screen) / 2 + 37.5 * size * x_koef_screen
        y3_for_both = y - (y - (y - 60 * size * y_koef_screen)) / 2

        # bottom sail
        bottom_sail = polygon([(x1_for_both, y1_bottom), (x2_for_both, y2_for_both),
                 (x3_for_both, y3_for_both), (x1_for_both, y1_bottom)])

        # top sail
        top_sail = polygon([(x1_for_both, y1_top), (x2_for_both, y2_for_both),
                 (x3_for_both, y3_for_both), (x1_for_both, y1_top)])

    else:

        x1 = x - x_length
        y1 = y + y_length

        mid_of_boat = rectangle(x, y, x1, y1)
        left_of_boat = arc(x - y_length, y - y_length, x + y_length, y1, 0, -90)
        right_of_boat = polygon([(x1, y1), (x1 - 45 * size * x_koef_screen, y),
                                 (x1, y), (x1, y1)])

        penSize(3 * size * x_koef_screen)
        penColor(0, 0, 0)
        brushColor(255, 255, 255)

        circ_of_boat = circle(x1 - 10 * size * x_koef_screen, y1 - 16.5 * size * y_koef_screen,
                              6 * size * x_koef_screen)

        penSize(5 * size * x_koef_screen)
        mast_of_boat = line(x - (x - x1) / 2 + 15 * size * x_koef_screen, y,
                            x - (x - x1) / 2 + 15 * size * x_koef_screen, y - 60 * size * y_koef_screen)

        penSize(1)
        penColor(170, 173, 132)
        brushColor(223, 214, 154)

        # ship sails
        x1_for_both = x - (x - x1) / 2 + 15 * size * x_koef_screen - (5 * size * x_koef_screen) / 2
        y1_bottom = y
        y1_top = y - 60 * size * y_koef_screen

        x2_for_both = x - (x - x1) / 2 + 15 * size * x_koef_screen - (5 * size * x_koef_screen) / 2 - 12.5 * size * x_koef_screen
        y2_for_both = y - (y - (y - 60 * size * y_koef_screen)) / 2

        x3_for_both = x - (x - x1) / 2 + 15 * size * x_koef_screen - (5 * size * x_koef_screen) / 2 - 37.5 * size * x_koef_screen
        y3_for_both = y - (y - (y - 60 * size * y_koef_screen)) / 2

        # bottom sail
        bottom_sail = polygon([(x1_for_both, y1_bottom), (x2_for_both, y2_for_both),
                               (x3_for_both, y3_for_both), (x1_for_both, y1_bottom)])

        # top sail
        top_sail = polygon([(x1_for_both, y1_top), (x2_for_both, y2_for_both),
                            (x3_for_both, y3_for_both), (x1_for_both, y1_top)])

    arr_boat.append(mid_of_boat)
    arr_boat.append(right_of_boat)
    arr_boat.append(left_of_boat)
    arr_boat.append(circ_of_boat)
    arr_boat.append(mast_of_boat)
    arr_boat.append(bottom_sail)
    arr_boat.append(top_sail)

    return arr_boat

def update_sand():
    pass

def main():

    arr_clouds = []
    arr_boats = []
    arr_umbrellas = []

    def update():
        global sun

        # wave moving
        for i in range(len(sand)):
            moveObjectBy(sand[i], 30, 0)

        if bbox(sand[0])[0] > -1:
            for y in range(len(sand)):
                moveObjectBy(sand[y], -60, 0)

            # sun's rotation
            for l in range(len(sun)):
                deleteObject(sun[l])
            del sun[l]

            sun = draw_sun(alpha=10)
        else:
            for l in range(len(sun)):
                deleteObject(sun[l])
            del sun[l]

            sun = draw_sun(alpha=15)

        # boats moving
        for j in range(len(arr_boats)):
            x_end_of_boat = bbox(arr_boats[j][2])[0]
            forward_of_boat = bbox(arr_boats[j][1])[0] - x_end_of_boat

            if x_end_of_boat >= x_window_size and forward_of_boat > 0:
                for h in range(len(arr_boats[j])):
                    deleteObject(arr_boats[j][h])
                del arr_boats[j]

                if j == 0:
                    boat = draw_boats(size = 1, x = -250, y = 135, direction = 'right')
                elif j == 1:
                    boat = draw_boats(size = 0.5, x = x_window_size, y = 120, direction = 'left')

                arr_boats.insert(j, boat)

            elif x_end_of_boat <= 0 and forward_of_boat < 0:
                for h in range(len(arr_boats[j])):
                    deleteObject(arr_boats[j][h])
                del arr_boats[j]

                if j == 0:
                    boat = draw_boats(size = 1, x = -250, y = 135, direction = 'right')
                elif j == 1:
                    boat = draw_boats(size = 0.5, x = x_window_size, y = 120, direction = 'left')

                arr_boats.insert(j, boat)

            if forward_of_boat > 0:
                for k in range(len(arr_boats[j])):
                    moveObjectBy((arr_boats[j][k]), 15, 0)
            else:
                for k in range(len(arr_boats[j])):
                    moveObjectBy((arr_boats[j][k]), -15, 0)

        # umbrellas
        for k in range(len(arr_umbrellas)):
            for l in range(len(arr_umbrellas[k])):
                deleteObject(arr_umbrellas[k][l])
            del arr_umbrellas[k]

            if k == 0:
                umbrella = draw_umbrella(size=1, x=75, y=175)
            else:
                umbrella = draw_umbrella(size=1.5, x=175, y=200)

            arr_umbrellas.insert(k, umbrella)

        # clouds' moving
        for h in range(len(arr_clouds)):
            for i in range(len(arr_clouds[h])):
                if h == 0:
                    moveObjectBy(arr_clouds[h][i], 15, 0)
                elif h == 1:
                    moveObjectBy(arr_clouds[h][i], 25, 0)
                elif h == 2:
                    moveObjectBy(arr_clouds[h][i], 20, 0)

            if bbox(arr_clouds[h][0])[0] >= x_window_size:
                len_of_cloud = -1 * (bbox(arr_clouds[h][6])[2] - bbox(arr_clouds[h][0])[0])


                for l in range(len(arr_clouds[h])):
                    deleteObject(arr_clouds[h][l])
                del arr_clouds[h]

                if h == 0:
                    cloud = draw_clouds(1, 1, len_of_cloud, 25, 20)
                    arr_clouds.insert(h, cloud)
                elif h == 1:
                    cloud = draw_clouds(1, 1.1, len_of_cloud, 10, 40)
                    arr_clouds.insert(h, cloud)
                elif h == 2:
                    cloud = draw_clouds(1.4, 0.9, len_of_cloud, 65, 30)
                    arr_clouds.insert(h, cloud)


    y_top_bottom_arr = calculate_top_bottom_sky_sea_sand()

    sky = draw_sky(y_top_bottom_arr[0])
    sea = draw_sea(y_top_bottom_arr[1])
    sand = draw_sand(y_top_bottom_arr[2], 30, 15)

    global sun
    sun = draw_sun(alpha = 10)

    clouds_1 = draw_clouds(1, 1, 30, 25, 20)
    clouds_2 = draw_clouds(1, 1.1, 150, 10, 40)
    clouds_3 = draw_clouds(1.4, 0.9, 50, 65, 30)

    boats_1 = draw_boats(size = 1, x = 235, y = 135, direction = 'right')
    boats_2 = draw_boats(size = 0.5, x = 130, y = 120, direction = 'left')

    umbrella_1 = draw_umbrella(size=1, x=75, y=175)
    umbrella_2 = draw_umbrella(size=1.5, x=175, y=200)

    arr_clouds.append(clouds_1)
    arr_clouds.append(clouds_2)
    arr_clouds.append(clouds_3)
    arr_boats.append(boats_1)
    arr_boats.append(boats_2)
    arr_umbrellas.append(umbrella_1)
    arr_umbrellas.append(umbrella_2)

    onTimer(update, 175)


main()
run()