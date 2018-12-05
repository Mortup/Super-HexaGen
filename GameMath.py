import math
import Settings

EPSILON = 0.00000001
RAD2DEG = 180/math.pi

def cart2cil(x, y):
    centered_pos = (x - Settings.SCREEN_CENTER[0], y - Settings.SCREEN_CENTER[1])
    magnitude = math.sqrt(centered_pos[0] ** 2 + centered_pos[1] ** 2)
    angle = math.atan2(centered_pos[1], centered_pos[0]) % 2*math.pi

    return (magnitude, angle)


def cil2cart(magnitude, angle):
    return (magnitude * math.cos(angle) + Settings.SCREEN_CENTER[0], magnitude * math.sin(angle) + Settings.SCREEN_CENTER[1])


def cart2cil_local(x, y):
    magnitude = math.sqrt(x ** 2 + y ** 2)
    angle = math.atan2(y, x) % 2*math.pi

    return (magnitude, angle)


def cil2cart_local(magnitude, angle):
    return (magnitude * math.cos(angle), magnitude * math.sin(angle))

def lerp(a, b, t):
    if t > 1:
        t = 1
    elif t < 0:
        t = 0

    return (b-a)*t + a

def no_clamp_lerp(a, b, t):
    return (b-a)*t + a

def pow_lerp(a, b, t, n):
    return lerp(a,b,t**n)

def color_lerp(c_a, c_b, t):
    r = lerp(c_a[0], c_b[0], t)
    g = lerp(c_a[1], c_b[1], t)
    b = lerp(c_a[2], c_b[2], t)
    return(r,g,b)

def palette_lerp(p_a, p_b, t):
    new_palette = []

    for x in range(len(p_a)):
        new_palette.append(color_lerp(p_a[x], p_b[x], t))

    return new_palette

def inverse_lerp(a, b, current):
    return (float(current) - a) / float(b - a)

# Uses cylindric coordinates
def is_point_on_rect(p, bottom_left, upper_right):
    is_between_magnitudes = p[0] >= bottom_left[0] and p[0] <= upper_right[0]
    is_between_angles = p[1] >= bottom_left[1] and p[1] <= upper_right[1]

    return is_between_angles and is_between_magnitudes

# In cartesian coords
def intersection_between_lines(p1, p2, p3, p4):
    x1 = p1[0]
    x2 = p2[0]
    x3 = p3[0]
    x4 = p4[0]
    y1 = p1[1]
    y2 = p2[1]
    y3 = p3[1]
    y4 = p4[1]

    px_upper = determinant(determinant(x1, y1, x2, y2), determinant(x1, 1, x2, 1), determinant(x3, y3, x4, y4),
                           determinant(x3, 1, x4, 1))
    px_bottom = determinant(determinant(x1, 1, x2, 1), determinant(y1, 1, y2, 1), determinant(x3, 1, x4, 1),
                            determinant(y3, 1, y4, 1))

    py_upper = determinant(determinant(x1, y1, x2, y2), determinant(y1, 1, y2, 1), determinant(x3, y3, x4, y4),
                           determinant(y3, 1, y4, 1))
    py_bottom = determinant(determinant(x1, 1, x2, 1), determinant(y1, 1, y2, 1), determinant(x3, 1, x4, 1),
                            determinant(y3, 1, y4, 1))

    if (px_bottom == 0):
        px_bottom = EPSILON
    if (py_bottom == 0):
        py_bottom = EPSILON

    return (px_upper/px_bottom,py_upper/py_bottom)

def determinant(a, b, c, d):
    return a*d - b*c