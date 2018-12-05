import random
import Colors


# Pauta o guion con los cambios de velocidad de camara y de intensidad de zoom de cada nivel
class Pattern:

    def __init__(self, rotation, sides, starting_palettes, bars_to_win):
        self.bars_to_win = bars_to_win
        self.rotation_points = []
        self.bars_points = []
        self.shape_change_points = []

        self.starting_rotation = rotation
        self.starting_sides_number = sides
        self.current_palettes = starting_palettes

    def add_rotation_point(self, beat, speed):
        self.rotation_points.append((beat,speed))

    def add_bar_point(self, beat, index, speed, width):
        self.bars_points.append((beat, index, speed, width))

    def add_shape_change_point(self, beat, sides):
        self.shape_change_points.append((beat,sides))

levels = [None, None, None]


def reload_patterns():
    global levels
    levels[0] = Pattern(0.01, 6, (Colors.redPalette1, Colors.greenPalette1),80)
    levels[1] = Pattern(-0.01, 5, (Colors.bluePalette1, Colors.orangePalette1), 140)
    levels[2] = Pattern(0.02, 6, (Colors.greenPalette2, Colors.bluePalette2), 204)

    # Level rotations
    levels[0].add_rotation_point(4, 0.02)
    levels[0].add_rotation_point(8, 0.03)
    levels[0].add_rotation_point(12, 0.04)
    levels[0].add_rotation_point(16, -0.05)
    levels[0].add_rotation_point(24, -0.06)
    levels[0].add_rotation_point(32, 0.01)
    levels[0].add_rotation_point(36, 0.06)
    levels[0].add_rotation_point(40, -0.01)
    levels[0].add_rotation_point(48, 0.06)
    levels[0].add_rotation_point(52, 0.01)
    levels[0].add_rotation_point(56, -0.06)
    levels[0].add_rotation_point(60, 0.06)
    levels[0].add_rotation_point(64, -0.06)
    levels[0].add_rotation_point(68, 0.06)
    levels[0].add_rotation_point(72, -0.06)
    levels[0].add_rotation_point(76, 0.06)
    levels[0].add_rotation_point(77, 0.12)
    levels[0].add_rotation_point(78, 0.18)
    levels[0].add_rotation_point(79, 0.22)
    levels[0].add_rotation_point(80, 0.3)

    # Level shape changes
    levels[0].add_shape_change_point(48, 4)

    # Level obstacles
    rand_rot = random.randint(0,5)
    time = 2

    levels[0].add_bar_point(time, rand_rot, 4, 20)
    levels[0].add_bar_point(time, (1 + rand_rot) % 6, 4, 20)
    levels[0].add_bar_point(time, (2 + rand_rot) % 6, 4, 20)
    levels[0].add_bar_point(time, (3 + rand_rot) % 6, 4, 20)
    levels[0].add_bar_point(time, (4 + rand_rot) % 6, 4, 20)

    time = 4

    levels[0].add_bar_point(time, rand_rot, 4, 20)
    levels[0].add_bar_point(time, (1 + rand_rot) % 6, 4, 20)
    levels[0].add_bar_point(time, (5 + rand_rot) % 6, 4, 20)
    levels[0].add_bar_point(time, (3 + rand_rot) % 6, 4, 20)
    levels[0].add_bar_point(time, (4 + rand_rot) % 6, 4, 20)

    time = 6

    levels[0].add_bar_point(time, rand_rot, 4, 20)
    levels[0].add_bar_point(time, (1 + rand_rot) % 6, 4, 20)
    levels[0].add_bar_point(time, (2 + rand_rot) % 6, 4, 20)
    levels[0].add_bar_point(time, (3 + rand_rot) % 6, 4, 20)
    levels[0].add_bar_point(time, (4 + rand_rot) % 6, 4, 20)

    time = 8

    levels[0].add_bar_point(time, rand_rot, 4, 20)
    levels[0].add_bar_point(time, (1 + rand_rot) % 6, 4, 20)
    levels[0].add_bar_point(time, (5 + rand_rot) % 6, 4, 20)
    levels[0].add_bar_point(time, (3 + rand_rot) % 6, 4, 20)
    levels[0].add_bar_point(time, (4 + rand_rot) % 6, 4, 20)

    time = 10

    levels[0].add_bar_point(time, rand_rot, 4, 20)
    levels[0].add_bar_point(time, (1 + rand_rot) % 6, 4, 20)
    levels[0].add_bar_point(time, (2 + rand_rot) % 6, 4, 20)
    levels[0].add_bar_point(time, (3 + rand_rot) % 6, 4, 20)
    levels[0].add_bar_point(time, (4 + rand_rot) % 6, 4, 20)

    rand_rot = random.randint(0, 5)
    time = 14

    levels[0].add_bar_point(time, rand_rot, 4, 20)
    levels[0].add_bar_point(time, (2 + rand_rot) % 6, 4, 20)
    levels[0].add_bar_point(time, (4 + rand_rot) % 6, 4, 20)

    time = 15

    levels[0].add_bar_point(time, (1 + rand_rot) % 6, 4, 20)
    levels[0].add_bar_point(time, (3 + rand_rot) % 6, 4, 20)
    levels[0].add_bar_point(time, (5 + rand_rot) % 6, 4, 20)

    time = 16

    levels[0].add_bar_point(time, rand_rot, 4, 20)
    levels[0].add_bar_point(time, (2 + rand_rot) % 6, 4, 20)
    levels[0].add_bar_point(time, (4 + rand_rot) % 6, 4, 20)

    time = 17

    levels[0].add_bar_point(time, (1 + rand_rot) % 6, 4, 20)
    levels[0].add_bar_point(time, (3 + rand_rot) % 6, 4, 20)
    levels[0].add_bar_point(time, (5 + rand_rot) % 6, 4, 20)

    rand_rot = random.randint(0, 5)
    time = 18

    levels[0].add_bar_point(time, (1 + rand_rot) % 6, 3, 20)
    levels[0].add_bar_point(time, (2 + rand_rot) % 6, 3, 20)
    levels[0].add_bar_point(time, (3 + rand_rot) % 6, 3, 20)
    levels[0].add_bar_point(time, (5 + rand_rot) % 6, 3, 20)

    rand_rot = random.randint(0, 5)
    time = 20

    levels[0].add_bar_point(time, (1 + rand_rot) % 6, 3, 20)
    levels[0].add_bar_point(time, (2 + rand_rot) % 6, 3, 20)
    levels[0].add_bar_point(time, (3 + rand_rot) % 6, 3, 20)
    levels[0].add_bar_point(time, (5 + rand_rot) % 6, 3, 20)

    rand_rot = random.randint(0, 5)
    time = 22

    levels[0].add_bar_point(time, (1 + rand_rot) % 6, 3, 20)
    levels[0].add_bar_point(time, (2 + rand_rot) % 6, 3, 20)
    levels[0].add_bar_point(time, (3 + rand_rot) % 6, 3, 20)
    levels[0].add_bar_point(time, (5 + rand_rot) % 6, 3, 20)

    rand_rot = random.randint(0, 5)
    time = 24

    levels[0].add_bar_point(time, (1 + rand_rot) % 6, 3, 20)
    levels[0].add_bar_point(time, (2 + rand_rot) % 6, 3, 20)
    levels[0].add_bar_point(time, (3 + rand_rot) % 6, 3, 20)
    levels[0].add_bar_point(time, (5 + rand_rot) % 6, 3, 20)

    rand_rot = random.randint(0, 5)
    time = 26

    levels[0].add_bar_point(time, (1 + rand_rot) % 6, 3, 20)
    levels[0].add_bar_point(time, (2 + rand_rot) % 6, 3, 20)
    levels[0].add_bar_point(time, (3 + rand_rot) % 6, 3, 20)
    levels[0].add_bar_point(time, (5 + rand_rot) % 6, 3, 20)

    rand_rot = random.randint(0, 5)
    time = 32

    levels[0].add_bar_point(time, (1 + rand_rot) % 6, 8, 20)
    levels[0].add_bar_point(time, (2 + rand_rot) % 6, 8, 20)

    rand_rot = random.randint(0, 5)
    time = 36

    levels[0].add_bar_point(time, (1 + rand_rot) % 6, 8, 20)
    levels[0].add_bar_point(time, (3 + rand_rot) % 6, 8, 20)
    levels[0].add_bar_point(time, (5 + rand_rot) % 6, 8, 20)

    rand_rot = random.randint(0, 5)
    time = 40

    levels[0].add_bar_point(time, (1 + rand_rot) % 6, 8, 20)
    levels[0].add_bar_point(time, (4 + rand_rot) % 6, 8, 20)

    time = 41

    levels[0].add_bar_point(time, (2 + rand_rot) % 6, 8, 20)
    levels[0].add_bar_point(time, (5 + rand_rot) % 6, 8, 20)

    time = 42

    levels[0].add_bar_point(time, (3 + rand_rot) % 6, 8, 20)
    levels[0].add_bar_point(time, (6 + rand_rot) % 6, 8, 20)

    time = 43

    levels[0].add_bar_point(time, (1 + rand_rot) % 6, 8, 20)
    levels[0].add_bar_point(time, (4 + rand_rot) % 6, 8, 20)

    time = 44

    levels[0].add_bar_point(time, (2 + rand_rot) % 6, 8, 20)
    levels[0].add_bar_point(time, (5 + rand_rot) % 6, 8, 20)

    time = 45

    levels[0].add_bar_point(time, (3 + rand_rot) % 6, 8, 20)
    levels[0].add_bar_point(time, (6 + rand_rot) % 6, 8, 20)

    time = 46

    levels[0].add_bar_point(time, (1 + rand_rot) % 6, 8, 20)
    levels[0].add_bar_point(time, (4 + rand_rot) % 6, 8, 20)

    time = 50

    levels[0].add_bar_point(time, (1 + rand_rot) % 4, 4, 100)
    levels[0].add_bar_point(time, (3 + rand_rot) % 4, 4, 100)

    time = 52

    levels[0].add_bar_point(time, (2 + rand_rot) % 4, 4, 100)
    levels[0].add_bar_point(time, (4 + rand_rot) % 4, 4, 100)

    time = 55

    levels[0].add_bar_point(time, (1 + rand_rot) % 4, 6, 25)
    levels[0].add_bar_point(time, (3 + rand_rot) % 4, 6, 25)

    time = 56

    levels[0].add_bar_point(time, (2 + rand_rot) % 4, 6, 25)
    levels[0].add_bar_point(time, (4 + rand_rot) % 4, 6, 25)

    time = 57

    levels[0].add_bar_point(time, (1 + rand_rot) % 4, 6, 25)
    levels[0].add_bar_point(time, (3 + rand_rot) % 4, 6, 25)

    time = 58

    levels[0].add_bar_point(time, (2 + rand_rot) % 4, 6, 25)
    levels[0].add_bar_point(time, (4 + rand_rot) % 4, 6, 25)

    time = 59

    levels[0].add_bar_point(time, (1 + rand_rot) % 4, 6, 25)
    levels[0].add_bar_point(time, (3 + rand_rot) % 4, 6, 25)

    time = 60

    levels[0].add_bar_point(time, (2 + rand_rot) % 4, 6, 25)
    levels[0].add_bar_point(time, (4 + rand_rot) % 4, 6, 25)

    time = 61

    levels[0].add_bar_point(time, (1 + rand_rot) % 4, 6, 25)
    levels[0].add_bar_point(time, (3 + rand_rot) % 4, 6, 25)

    time = 62

    levels[0].add_bar_point(time, (2 + rand_rot) % 4, 6, 25)
    levels[0].add_bar_point(time, (4 + rand_rot) % 4, 6, 25)

    rand_rot = random.randint(0,3)
    levels[0].add_bar_point(64, (0 + rand_rot) % 4, 6, 100)
    levels[0].add_bar_point(64.5, (1 + rand_rot) % 4, 6, 100)
    levels[0].add_bar_point(65, (2 + rand_rot) % 4, 6, 100)
    levels[0].add_bar_point(65.5, (3 + rand_rot) % 4, 6, 100)
    levels[0].add_bar_point(66, (0 + rand_rot) % 4, 6, 100)
    levels[0].add_bar_point(66.5, (1 + rand_rot) % 4, 6, 100)
    levels[0].add_bar_point(67, (2 + rand_rot) % 4, 6, 100)
    levels[0].add_bar_point(67.5, (3 + rand_rot) % 4, 6, 100)

    rand_rot = random.randint(0, 3)
    time = 69
    levels[0].add_bar_point(time, (0 + rand_rot) % 4, 6, 30)
    levels[0].add_bar_point(time, (1 + rand_rot) % 4, 6, 30)
    levels[0].add_bar_point(time, (2 + rand_rot) % 4, 6, 30)

    rand_rot = random.randint(0, 3)
    time = 71
    levels[0].add_bar_point(time, (0 + rand_rot) % 4, 6, 30)
    levels[0].add_bar_point(time, (1 + rand_rot) % 4, 6, 30)
    levels[0].add_bar_point(time, (2 + rand_rot) % 4, 6, 30)

    rand_rot = random.randint(0, 3)
    time = 73
    levels[0].add_bar_point(time, (0 + rand_rot) % 4, 6, 30)
    levels[0].add_bar_point(time, (1 + rand_rot) % 4, 6, 30)
    levels[0].add_bar_point(time, (2 + rand_rot) % 4, 6, 30)

    rand_rot = random.randint(0, 3)
    time = 75
    levels[0].add_bar_point(time, (0 + rand_rot) % 4, 6, 30)
    levels[0].add_bar_point(time, (1 + rand_rot) % 4, 6, 30)
    levels[0].add_bar_point(time, (2 + rand_rot) % 4, 6, 30)

    # LEVEL 2
    # Obstacles
    rand_rot = random.randint(0, 4)
    time = 2

    levels[1].add_bar_point(time, rand_rot, 8, 25)
    levels[1].add_bar_point(time, (rand_rot+1)%5, 8, 25)
    levels[1].add_bar_point(time, (rand_rot+2)%5, 8, 25)

    rand_rot = random.randint(0, 4)
    time = 4

    levels[1].add_bar_point(time, rand_rot, 8, 25)
    levels[1].add_bar_point(time, (rand_rot + 1) % 5, 8, 25)
    levels[1].add_bar_point(time, (rand_rot + 2) % 5, 8, 25)

    rand_rot = random.randint(0, 4)
    time = 6

    levels[1].add_bar_point(time, rand_rot, 8, 25)
    levels[1].add_bar_point(time, (rand_rot + 1) % 5, 8, 25)
    levels[1].add_bar_point(time, (rand_rot + 2) % 5, 8, 25)

    rand_rot = random.randint(0, 4)
    time = 8

    levels[1].add_bar_point(time, rand_rot, 6, 25)
    levels[1].add_bar_point(time, (rand_rot + 1) % 5, 6, 25)
    levels[1].add_bar_point(time, (rand_rot + 2) % 5, 6, 25)

    rand_rot = random.randint(0, 4)
    time = 10

    levels[1].add_bar_point(time, rand_rot, 6, 25)
    levels[1].add_bar_point(time, (rand_rot + 1) % 5, 6, 25)
    levels[1].add_bar_point(time, (rand_rot + 2) % 5, 6, 25)

    rand_rot = random.randint(0, 4)
    time = 12

    levels[1].add_bar_point(time, rand_rot, 6, 25)
    levels[1].add_bar_point(time, (rand_rot + 1) % 5, 6, 25)
    levels[1].add_bar_point(time, (rand_rot + 2) % 5, 6, 25)

    rand_rot = random.randint(0, 4)
    time = 14

    levels[1].add_bar_point(time, rand_rot, 6, 25)
    levels[1].add_bar_point(time, (rand_rot + 1) % 5, 6, 25)
    levels[1].add_bar_point(time, (rand_rot + 2) % 5, 6, 25)

    rand_rot = random.randint(0, 4)
    time = 16

    levels[1].add_bar_point(time, rand_rot, 4, 40)
    levels[1].add_bar_point(time, (rand_rot + 1) % 5, 4, 40)
    levels[1].add_bar_point(time, (rand_rot + 2) % 5, 4, 40)
    levels[1].add_bar_point(time, (rand_rot + 3) % 5, 4, 40)

    time = 17

    levels[1].add_bar_point(time, rand_rot, 4, 40)
    levels[1].add_bar_point(time, (rand_rot + 1) % 5, 4, 40)
    levels[1].add_bar_point(time, (rand_rot + 2) % 5, 4, 40)
    levels[1].add_bar_point(time, (rand_rot + 3) % 5, 4, 40)

    rand_rot = random.randint(0, 4)
    time = 19

    levels[1].add_bar_point(time, rand_rot, 4, 40)
    levels[1].add_bar_point(time, (rand_rot + 1) % 5, 4, 40)
    levels[1].add_bar_point(time, (rand_rot + 2) % 5, 4, 40)
    levels[1].add_bar_point(time, (rand_rot + 3) % 5, 4, 40)

    time = 20

    levels[1].add_bar_point(time, rand_rot, 4, 40)
    levels[1].add_bar_point(time, (rand_rot + 1) % 5, 4, 40)
    levels[1].add_bar_point(time, (rand_rot + 2) % 5, 4, 40)
    levels[1].add_bar_point(time, (rand_rot + 3) % 5, 4, 40)

    rand_rot = random.randint(0, 4)
    time = 22

    levels[1].add_bar_point(time, rand_rot, 4, 40)
    levels[1].add_bar_point(time, (rand_rot + 1) % 5, 4, 40)
    levels[1].add_bar_point(time, (rand_rot + 2) % 5, 4, 40)
    levels[1].add_bar_point(time, (rand_rot + 3) % 5, 4, 40)

    time = 23

    levels[1].add_bar_point(time, rand_rot, 4, 40)
    levels[1].add_bar_point(time, (rand_rot + 1) % 5, 4, 40)
    levels[1].add_bar_point(time, (rand_rot + 2) % 5, 4, 40)
    levels[1].add_bar_point(time, (rand_rot + 3) % 5, 4, 40)

    rand_rot = random.randint(0, 4)
    time = 25

    levels[1].add_bar_point(time, rand_rot, 4, 40)
    levels[1].add_bar_point(time, (rand_rot + 1) % 5, 4, 40)
    levels[1].add_bar_point(time, (rand_rot + 2) % 5, 4, 40)
    levels[1].add_bar_point(time, (rand_rot + 3) % 5, 4, 40)

    time = 26

    levels[1].add_bar_point(time, rand_rot, 4, 40)
    levels[1].add_bar_point(time, (rand_rot + 1) % 5, 4, 40)
    levels[1].add_bar_point(time, (rand_rot + 2) % 5, 4, 40)
    levels[1].add_bar_point(time, (rand_rot + 3) % 5, 4, 40)

    rand_rot = random.randint(0, 2)
    time = 32
    levels[1].add_bar_point(time, rand_rot, 10, 50)

    rand_rot = random.randint(0, 2)
    time = 33
    levels[1].add_bar_point(time, rand_rot, 10, 50)

    rand_rot = random.randint(0, 2)
    time = 34
    levels[1].add_bar_point(time, rand_rot, 10, 50)

    rand_rot = random.randint(0, 2)
    time = 35
    levels[1].add_bar_point(time, rand_rot, 10, 50)

    rand_rot = random.randint(0, 2)
    time = 36
    levels[1].add_bar_point(time, rand_rot, 10, 50)

    rand_rot = random.randint(0, 2)
    time = 37
    levels[1].add_bar_point(time, rand_rot, 10, 50)

    rand_rot = random.randint(0, 2)
    time = 38
    levels[1].add_bar_point(time, rand_rot, 10, 50)

    rand_rot = random.randint(0, 2)
    time = 39
    levels[1].add_bar_point(time, rand_rot, 10, 50)

    rand_rot = random.randint(0, 2)
    time = 40
    levels[1].add_bar_point(time, rand_rot, 10, 50)

    rand_rot = random.randint(0, 2)
    time = 41
    levels[1].add_bar_point(time, rand_rot, 10, 50)

    rand_rot = random.randint(0, 2)
    time = 42
    levels[1].add_bar_point(time, rand_rot, 10, 50)

    rand_rot = random.randint(0, 2)
    time = 43
    levels[1].add_bar_point(time, rand_rot, 10, 50)

    time = 45
    levels[1].add_bar_point(time, 0, 2, 50)
    levels[1].add_bar_point(time, 1, 2, 50)
    levels[1].add_bar_point(time, 2, 2, 50)

    time = 56
    rand_rot = random.randint(0, 5)
    levels[1].add_bar_point(time, (rand_rot+0)%6, 6, 50)
    levels[1].add_bar_point(time, (rand_rot+2)%6, 6, 50)
    levels[1].add_bar_point(time, (rand_rot+4)%6, 6, 50)

    time = 58
    rand_rot = random.randint(0, 5)
    levels[1].add_bar_point(time, (rand_rot + 0) % 6, 6, 50)
    levels[1].add_bar_point(time, (rand_rot + 2) % 6, 6, 50)
    levels[1].add_bar_point(time, (rand_rot + 4) % 6, 6, 50)

    time = 60
    rand_rot = random.randint(0, 5)
    levels[1].add_bar_point(time, (rand_rot + 0) % 6, 6, 50)
    levels[1].add_bar_point(time, (rand_rot + 2) % 6, 6, 50)
    levels[1].add_bar_point(time, (rand_rot + 4) % 6, 6, 50)

    time = 62
    rand_rot = random.randint(0, 5)
    levels[1].add_bar_point(time, (rand_rot + 0) % 6, 6, 50)
    levels[1].add_bar_point(time, (rand_rot + 2) % 6, 6, 50)
    levels[1].add_bar_point(time, (rand_rot + 4) % 6, 6, 50)

    time = 66
    rand_rot = random.randint(0, 5)
    levels[1].add_bar_point(time, (rand_rot + 0) % 6, 4, 500)
    levels[1].add_bar_point(time, (rand_rot + 3) % 6, 4, 500)
    levels[1].add_bar_point(time, (rand_rot + 1) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 4) % 6, 4, 25)
    levels[1].add_bar_point(time+1, (rand_rot + 2) % 6, 4, 25)
    levels[1].add_bar_point(time+1, (rand_rot + 5) % 6, 4, 25)

    time = 68
    levels[1].add_bar_point(time, (rand_rot + 1) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 4) % 6, 4, 25)
    levels[1].add_bar_point(time + 1, (rand_rot + 2) % 6, 4, 25)
    levels[1].add_bar_point(time + 1, (rand_rot + 5) % 6, 4, 25)

    time = 73
    rand_rot = random.randint(0, 5)
    levels[1].add_bar_point(time, (rand_rot + 0) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 3) % 6, 4, 25)
    levels[1].add_bar_point(time+1, (rand_rot + 1) % 6, 4, 25)
    levels[1].add_bar_point(time+1, (rand_rot + 4) % 6, 4, 25)
    levels[1].add_bar_point(time+2, (rand_rot + 2) % 6, 4, 25)
    levels[1].add_bar_point(time+2, (rand_rot + 5) % 6, 4, 25)
    levels[1].add_bar_point(time+3, (rand_rot + 3) % 6, 4, 25)
    levels[1].add_bar_point(time+3, (rand_rot + 0) % 6, 4, 25)
    levels[1].add_bar_point(time+4, (rand_rot + 4) % 6, 4, 25)
    levels[1].add_bar_point(time+4, (rand_rot + 1) % 6, 4, 25)
    levels[1].add_bar_point(time+5, (rand_rot + 5) % 6, 4, 25)
    levels[1].add_bar_point(time+5, (rand_rot + 2) % 6, 4, 25)

    time = 80
    rand_rot = random.randint(0, 5)
    levels[1].add_bar_point(time, (rand_rot + 0) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 1) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 2) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 3) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 4) % 6, 4, 25)

    time = 81
    rand_rot = rand_rot + 1
    levels[1].add_bar_point(time, (rand_rot + 0) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 1) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 2) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 3) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 4) % 6, 4, 25)

    time = 82
    rand_rot = rand_rot + 1
    levels[1].add_bar_point(time, (rand_rot + 0) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 1) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 2) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 3) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 4) % 6, 4, 25)

    time = 83
    rand_rot = rand_rot + 1
    levels[1].add_bar_point(time, (rand_rot + 0) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 1) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 2) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 3) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 4) % 6, 4, 25)

    time = 84
    rand_rot = rand_rot + 1
    levels[1].add_bar_point(time, (rand_rot + 0) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 1) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 2) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 3) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 4) % 6, 4, 25)

    time = 85
    rand_rot = rand_rot + 1
    levels[1].add_bar_point(time, (rand_rot + 0) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 1) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 2) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 3) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 4) % 6, 4, 25)

    time = 87
    rand_rot = random.randint(0, 5)
    levels[1].add_bar_point(time, (rand_rot + 0) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 1) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 2) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 3) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 4) % 6, 4, 25)

    time = 90
    levels[1].add_bar_point(time, (rand_rot + 0) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 1) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 5) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 3) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 4) % 6, 4, 25)

    time = 93
    levels[1].add_bar_point(time, (rand_rot + 0) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 1) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 2) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 3) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 4) % 6, 4, 25)

    time = 96
    levels[1].add_bar_point(time, (rand_rot + 0) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 1) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 5) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 3) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 4) % 6, 4, 25)

    time = 99
    rand_rot = random.randint(0, 5)
    levels[1].add_bar_point(time, (rand_rot + 0) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 1) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 2) % 6, 4, 25)

    time = 103
    rand_rot = random.randint(0, 5)
    levels[1].add_bar_point(time, (rand_rot + 0) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 1) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 2) % 6, 4, 25)

    time = 107
    rand_rot = random.randint(0, 5)
    levels[1].add_bar_point(time, (rand_rot + 0) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 1) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 2) % 6, 4, 25)

    time = 111
    rand_rot = random.randint(0, 5)
    levels[1].add_bar_point(time, (rand_rot + 0) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 1) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 2) % 6, 4, 25)

    time = 115
    rand_rot = random.randint(0, 5)
    levels[1].add_bar_point(time, (rand_rot + 0) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 1) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 2) % 6, 4, 25)

    time = 119
    rand_rot = random.randint(0, 5)
    levels[1].add_bar_point(time, (rand_rot + 0) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 1) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 2) % 6, 4, 25)

    time = 123
    rand_rot = random.randint(0, 5)
    levels[1].add_bar_point(time, (rand_rot + 0) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 1) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 2) % 6, 4, 25)

    time = 127
    rand_rot = random.randint(0, 5)
    levels[1].add_bar_point(time, (rand_rot + 0) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 1) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 2) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 4) % 6, 4, 25)

    time = 130
    rand_rot = random.randint(0, 5)
    levels[1].add_bar_point(time, (rand_rot + 0) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 1) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 2) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 4) % 6, 4, 25)

    time = 133
    rand_rot = random.randint(0, 5)
    levels[1].add_bar_point(time, (rand_rot + 0) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 1) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 2) % 6, 4, 25)
    levels[1].add_bar_point(time, (rand_rot + 4) % 6, 4, 25)

    # Level rotations
    levels[1].add_rotation_point(4, 0.01)
    levels[1].add_rotation_point(8, -0.01)
    levels[1].add_rotation_point(12, 0.01)
    levels[1].add_rotation_point(16, -0.03)
    levels[1].add_rotation_point(20, -0.06)
    levels[1].add_rotation_point(24, -0.03)
    levels[1].add_rotation_point(28, 0.09)
    levels[1].add_rotation_point(32, 0.03)
    levels[1].add_rotation_point(36, -0.03)
    levels[1].add_rotation_point(40, 0.03)
    levels[1].add_rotation_point(44, -0.06)
    levels[1].add_rotation_point(48, 0)
    levels[1].add_rotation_point(52, -0.06)
    levels[1].add_rotation_point(56, 0)
    levels[1].add_rotation_point(60, -0.06)
    levels[1].add_rotation_point(64, 0.04)
    levels[1].add_rotation_point(72, -0.01)
    levels[1].add_rotation_point(76, -0.06)
    levels[1].add_rotation_point(78, 0.04)
    levels[1].add_rotation_point(82, -0.04)
    levels[1].add_rotation_point(90, 0.01)
    levels[1].add_rotation_point(96, 0.06)
    levels[1].add_rotation_point(98, -0.04)
    levels[1].add_rotation_point(110, 0.06)
    levels[1].add_rotation_point(127, 0)
    levels[1].add_rotation_point(128, 0.06)
    levels[1].add_rotation_point(135, 0)
    levels[1].add_rotation_point(136, -0.06)
    levels[1].add_rotation_point(138, 0.24)

    # Level shape changes
    levels[1].add_shape_change_point(28, 3)
    levels[1].add_shape_change_point(47, 6)

    # LEVEL 3
    # Rotation points
    levels[2].add_rotation_point(16, -0.01)
    levels[2].add_rotation_point(18, -0.06)
    levels[2].add_rotation_point(20, 0.01)
    levels[2].add_rotation_point(22, 0.06)
    levels[2].add_rotation_point(24, -0.01)
    levels[2].add_rotation_point(28, 0.01)
    levels[2].add_rotation_point(32, -0.08)
    levels[2].add_rotation_point(48, 0.08)
    levels[2].add_rotation_point(64, -0.08)
    levels[2].add_rotation_point(76, -0.01)
    levels[2].add_rotation_point(80, -0.06)
    levels[2].add_rotation_point(96, 0.01)
    levels[2].add_rotation_point(98, 0.03)
    levels[2].add_rotation_point(99, 0.05)
    levels[2].add_rotation_point(100, 0.07)
    levels[2].add_rotation_point(104, 0)
    levels[2].add_rotation_point(105, 0.08)
    levels[2].add_rotation_point(107, 0)
    levels[2].add_rotation_point(108, 0.08)
    levels[2].add_rotation_point(112, -0.06)
    levels[2].add_rotation_point(120, 0.06)
    levels[2].add_rotation_point(128, -0.06)
    levels[2].add_rotation_point(136, -0.01)
    levels[2].add_rotation_point(144, 0.04)
    levels[2].add_rotation_point(152, -0.04)
    levels[2].add_rotation_point(160, 0.04)
    levels[2].add_rotation_point(168, -0.04)
    levels[2].add_rotation_point(176, 0.04)
    levels[2].add_rotation_point(184, -0.04)
    levels[2].add_rotation_point(192, 0.04)
    levels[2].add_rotation_point(200, -0.04)

    # Obstacles
    time = 1
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time, (rand_rot + 0) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 1, (rand_rot + 0) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 2, (rand_rot + 0) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 3, (rand_rot + 0) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 4, (rand_rot + 0) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 5, (rand_rot + 0) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 6, (rand_rot + 0) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 7, (rand_rot + 0) % 6, 4, 25)
    time = 9
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time, (rand_rot + 0) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 1, (rand_rot + 0) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 2, (rand_rot + 0) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 3, (rand_rot + 0) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 4, (rand_rot + 0) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 5, (rand_rot + 0) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 6, (rand_rot + 0) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 7, (rand_rot + 0) % 6, 4, 25)

    time = 17
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time, (rand_rot + 0) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 1, (rand_rot + 0) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 2, (rand_rot + 0) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 3, (rand_rot + 0) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 4, (rand_rot + 0) % 6, 4, 25)

    time = 26
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time, (rand_rot + 3) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 1) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 2) % 6, 6, 25)

    time = 28
    levels[2].add_bar_point(time, (rand_rot + 0) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 1) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 2) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 3) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 4) % 6, 6, 25)
    time = 29
    rand_rot = rand_rot + 1
    levels[2].add_bar_point(time, (rand_rot + 0) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 1) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 2) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 3) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 4) % 6, 6, 25)
    time = 30
    rand_rot = rand_rot + 1
    levels[2].add_bar_point(time, (rand_rot + 0) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 1) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 2) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 3) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 4) % 6, 6, 25)
    time = 31
    rand_rot = rand_rot + 1
    levels[2].add_bar_point(time, (rand_rot + 0) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 1) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 2) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 3) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 4) % 6, 6, 25)
    time = 32
    rand_rot = rand_rot + 1
    levels[2].add_bar_point(time, (rand_rot + 0) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 1) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 2) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 3) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 4) % 6, 6, 25)
    time = 33
    rand_rot = rand_rot + 1
    levels[2].add_bar_point(time, (rand_rot + 0) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 1) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 2) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 3) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 4) % 6, 6, 25)
    time = 34
    rand_rot = rand_rot + 1
    levels[2].add_bar_point(time, (rand_rot + 0) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 1) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 2) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 3) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 4) % 6, 6, 25)
    time = 35
    rand_rot = rand_rot + 1
    levels[2].add_bar_point(time, (rand_rot + 0) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 1) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 2) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 3) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 4) % 6, 6, 25)
    time = 36
    rand_rot = rand_rot + 1
    levels[2].add_bar_point(time, (rand_rot + 0) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 1) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 2) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 3) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 4) % 6, 6, 25)
    time = 37
    rand_rot = rand_rot + 1
    levels[2].add_bar_point(time, (rand_rot + 0) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 1) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 2) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 3) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 4) % 6, 6, 25)
    time = 38
    rand_rot = rand_rot + 1
    levels[2].add_bar_point(time, (rand_rot + 0) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 1) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 2) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 3) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 4) % 6, 6, 25)
    time = 39
    rand_rot = rand_rot + 1
    levels[2].add_bar_point(time, (rand_rot + 0) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 1) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 2) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 3) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 4) % 6, 6, 25)
    time = 40
    rand_rot = rand_rot + 1
    levels[2].add_bar_point(time, (rand_rot + 0) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 1) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 2) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 3) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 4) % 6, 6, 25)
    time = 41
    rand_rot = rand_rot + 1
    levels[2].add_bar_point(time, (rand_rot + 0) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 1) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 2) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 3) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 4) % 6, 6, 25)
    time = 42
    rand_rot = rand_rot + 1
    levels[2].add_bar_point(time, (rand_rot + 0) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 1) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 2) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 3) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 4) % 6, 6, 25)
    time = 43
    rand_rot = rand_rot + 1
    levels[2].add_bar_point(time, (rand_rot + 0) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 1) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 2) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 3) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 4) % 6, 6, 25)
    time = 44
    rand_rot = rand_rot + 1
    levels[2].add_bar_point(time, (rand_rot + 0) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 1) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 2) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 3) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 4) % 6, 6, 25)

    time = 48
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time, (rand_rot + 0) % 6, 8, 25)
    time = 50
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time, (rand_rot + 0) % 6, 8, 25)
    time = 52
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time, (rand_rot + 0) % 6, 8, 25)
    time = 54
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time, (rand_rot + 0) % 6, 8, 25)
    time = 56
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time, (rand_rot + 0) % 6, 8, 25)
    time = 58
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time, (rand_rot + 0) % 6, 8, 25)
    time = 60
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time, (rand_rot + 0) % 6, 8, 25)
    time = 62
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time, (rand_rot + 0) % 6, 8, 25)

    time = 64
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time, (rand_rot + 0) % 6, 4, 25)
    levels[2].add_bar_point(time, (rand_rot + 1) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 1, (rand_rot + 0) % 6, 4, 25)
    levels[2].add_bar_point(time + 1, (rand_rot + 1) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 2, (rand_rot + 0) % 6, 4, 25)
    levels[2].add_bar_point(time + 2, (rand_rot + 1) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 3, (rand_rot + 0) % 6, 4, 25)
    levels[2].add_bar_point(time + 3, (rand_rot + 1) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 4, (rand_rot + 0) % 6, 4, 25)
    levels[2].add_bar_point(time + 4, (rand_rot + 1) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 5, (rand_rot + 0) % 6, 4, 25)
    levels[2].add_bar_point(time + 5, (rand_rot + 1) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 6, (rand_rot + 0) % 6, 4, 25)
    levels[2].add_bar_point(time + 6, (rand_rot + 1) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 7, (rand_rot + 0) % 6, 4, 25)
    levels[2].add_bar_point(time + 7, (rand_rot + 1) % 6, 4, 25)

    time = 72
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time, (rand_rot + 0) % 6, 4, 25)
    levels[2].add_bar_point(time, (rand_rot + 3) % 6, 4, 25)
    levels[2].add_bar_point(time+1, (rand_rot + 1) % 6, 4, 25)
    levels[2].add_bar_point(time+1, (rand_rot + 4) % 6, 4, 25)
    levels[2].add_bar_point(time+2, (rand_rot + 2) % 6, 4, 25)
    levels[2].add_bar_point(time+2, (rand_rot + 5) % 6, 4, 25)
    time = 75
    levels[2].add_bar_point(time, (rand_rot + 0) % 6, 4, 25)
    levels[2].add_bar_point(time, (rand_rot + 3) % 6, 4, 25)
    levels[2].add_bar_point(time + 1, (rand_rot + 1) % 6, 4, 25)
    levels[2].add_bar_point(time + 1, (rand_rot + 4) % 6, 4, 25)
    levels[2].add_bar_point(time + 2, (rand_rot + 2) % 6, 4, 25)
    levels[2].add_bar_point(time + 2, (rand_rot + 5) % 6, 4, 25)
    time = 78
    levels[2].add_bar_point(time, (rand_rot + 0) % 6, 4, 25)
    levels[2].add_bar_point(time, (rand_rot + 3) % 6, 4, 25)
    levels[2].add_bar_point(time + 1, (rand_rot + 1) % 6, 4, 25)
    levels[2].add_bar_point(time + 1, (rand_rot + 4) % 6, 4, 25)
    levels[2].add_bar_point(time + 2, (rand_rot + 2) % 6, 4, 25)
    levels[2].add_bar_point(time + 2, (rand_rot + 5) % 6, 4, 25)
    time = 81
    levels[2].add_bar_point(time, (rand_rot + 0) % 6, 4, 25)
    levels[2].add_bar_point(time, (rand_rot + 3) % 6, 4, 25)
    levels[2].add_bar_point(time + 1, (rand_rot + 1) % 6, 4, 25)
    levels[2].add_bar_point(time + 1, (rand_rot + 4) % 6, 4, 25)
    levels[2].add_bar_point(time + 2, (rand_rot + 2) % 6, 4, 25)
    levels[2].add_bar_point(time + 2, (rand_rot + 5) % 6, 4, 25)

    time = 86
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time, (rand_rot + 3) % 6, 6, 25)
    levels[2].add_bar_point(time+.5, (rand_rot + 2) % 6, 6, 25)
    levels[2].add_bar_point(time+.5, (rand_rot + 3) % 6, 6, 25)
    levels[2].add_bar_point(time+.5, (rand_rot + 4) % 6, 6, 25)
    levels[2].add_bar_point(time + 1, (rand_rot + 1) % 6, 6, 25)
    levels[2].add_bar_point(time + 1, (rand_rot + 2) % 6, 6, 25)
    levels[2].add_bar_point(time + 1, (rand_rot + 3) % 6, 6, 25)
    levels[2].add_bar_point(time + 1, (rand_rot + 4) % 6, 6, 25)
    levels[2].add_bar_point(time + 1, (rand_rot + 5) % 6, 6, 25)

    time = 90
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time, (rand_rot + 3) % 6, 6, 25)
    levels[2].add_bar_point(time + .5, (rand_rot + 2) % 6, 6, 25)
    levels[2].add_bar_point(time + .5, (rand_rot + 3) % 6, 6, 25)
    levels[2].add_bar_point(time + .5, (rand_rot + 4) % 6, 6, 25)
    levels[2].add_bar_point(time + 1, (rand_rot + 1) % 6, 6, 25)
    levels[2].add_bar_point(time + 1, (rand_rot + 2) % 6, 6, 25)
    levels[2].add_bar_point(time + 1, (rand_rot + 3) % 6, 6, 25)
    levels[2].add_bar_point(time + 1, (rand_rot + 4) % 6, 6, 25)
    levels[2].add_bar_point(time + 1, (rand_rot + 5) % 6, 6, 25)

    time = 94
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time, (rand_rot + 3) % 6, 6, 25)
    levels[2].add_bar_point(time + .5, (rand_rot + 2) % 6, 6, 25)
    levels[2].add_bar_point(time + .5, (rand_rot + 3) % 6, 6, 25)
    levels[2].add_bar_point(time + .5, (rand_rot + 4) % 6, 6, 25)
    levels[2].add_bar_point(time + 1, (rand_rot + 1) % 6, 6, 25)
    levels[2].add_bar_point(time + 1, (rand_rot + 2) % 6, 6, 25)
    levels[2].add_bar_point(time + 1, (rand_rot + 3) % 6, 6, 25)
    levels[2].add_bar_point(time + 1, (rand_rot + 4) % 6, 6, 25)
    levels[2].add_bar_point(time + 1, (rand_rot + 5) % 6, 6, 25)

    time = 98
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time, (rand_rot + 3) % 6, 6, 25)
    levels[2].add_bar_point(time + .5, (rand_rot + 2) % 6, 6, 25)
    levels[2].add_bar_point(time + .5, (rand_rot + 3) % 6, 6, 25)
    levels[2].add_bar_point(time + .5, (rand_rot + 4) % 6, 6, 25)
    levels[2].add_bar_point(time + 1, (rand_rot + 1) % 6, 6, 25)
    levels[2].add_bar_point(time + 1, (rand_rot + 2) % 6, 6, 25)
    levels[2].add_bar_point(time + 1, (rand_rot + 3) % 6, 6, 25)
    levels[2].add_bar_point(time + 1, (rand_rot + 4) % 6, 6, 25)
    levels[2].add_bar_point(time + 1, (rand_rot + 5) % 6, 6, 25)

    time = 102
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time, (rand_rot + 3) % 6, 6, 25)
    levels[2].add_bar_point(time + .5, (rand_rot + 2) % 6, 6, 25)
    levels[2].add_bar_point(time + .5, (rand_rot + 3) % 6, 6, 25)
    levels[2].add_bar_point(time + .5, (rand_rot + 4) % 6, 6, 25)
    levels[2].add_bar_point(time + 1, (rand_rot + 1) % 6, 6, 25)
    levels[2].add_bar_point(time + 1, (rand_rot + 2) % 6, 6, 25)
    levels[2].add_bar_point(time + 1, (rand_rot + 3) % 6, 6, 25)
    levels[2].add_bar_point(time + 1, (rand_rot + 4) % 6, 6, 25)
    levels[2].add_bar_point(time + 1, (rand_rot + 5) % 6, 6, 25)

    time = 106
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time, (rand_rot + 3) % 6, 6, 25)
    levels[2].add_bar_point(time + .5, (rand_rot + 2) % 6, 6, 25)
    levels[2].add_bar_point(time + .5, (rand_rot + 3) % 6, 6, 25)
    levels[2].add_bar_point(time + .5, (rand_rot + 4) % 6, 6, 25)
    levels[2].add_bar_point(time + 1, (rand_rot + 1) % 6, 6, 25)
    levels[2].add_bar_point(time + 1, (rand_rot + 2) % 6, 6, 25)
    levels[2].add_bar_point(time + 1, (rand_rot + 3) % 6, 6, 25)
    levels[2].add_bar_point(time + 1, (rand_rot + 4) % 6, 6, 25)
    levels[2].add_bar_point(time + 1, (rand_rot + 5) % 6, 6, 25)

    time = 110
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time, (rand_rot + 3) % 6, 6, 25)
    levels[2].add_bar_point(time + .5, (rand_rot + 2) % 6, 6, 25)
    levels[2].add_bar_point(time + .5, (rand_rot + 3) % 6, 6, 25)
    levels[2].add_bar_point(time + .5, (rand_rot + 4) % 6, 6, 25)
    levels[2].add_bar_point(time + 1, (rand_rot + 1) % 6, 6, 25)
    levels[2].add_bar_point(time + 1, (rand_rot + 2) % 6, 6, 25)
    levels[2].add_bar_point(time + 1, (rand_rot + 3) % 6, 6, 25)
    levels[2].add_bar_point(time + 1, (rand_rot + 4) % 6, 6, 25)
    levels[2].add_bar_point(time + 1, (rand_rot + 5) % 6, 6, 25)

    time = 114
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time, (rand_rot + 3) % 6, 6, 25)
    levels[2].add_bar_point(time + .5, (rand_rot + 2) % 6, 6, 25)
    levels[2].add_bar_point(time + .5, (rand_rot + 3) % 6, 6, 25)
    levels[2].add_bar_point(time + .5, (rand_rot + 4) % 6, 6, 25)
    levels[2].add_bar_point(time + 1, (rand_rot + 1) % 6, 6, 25)
    levels[2].add_bar_point(time + 1, (rand_rot + 2) % 6, 6, 25)
    levels[2].add_bar_point(time + 1, (rand_rot + 3) % 6, 6, 25)
    levels[2].add_bar_point(time + 1, (rand_rot + 4) % 6, 6, 25)
    levels[2].add_bar_point(time + 1, (rand_rot + 5) % 6, 6, 25)

    time = 118
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time, (rand_rot + 0) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 1, (rand_rot + 0) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 2, (rand_rot + 0) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 3, (rand_rot + 0) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 4, (rand_rot + 0) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 5, (rand_rot + 0) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 6, (rand_rot + 0) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 7, (rand_rot + 0) % 6, 4, 25)

    time = 126
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time, (rand_rot + 0) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 1, (rand_rot + 0) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 2, (rand_rot + 0) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 3, (rand_rot + 0) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 4, (rand_rot + 0) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 5, (rand_rot + 0) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 6, (rand_rot + 0) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 7, (rand_rot + 0) % 6, 4, 25)

    time = 134
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time, (rand_rot + 0) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 1, (rand_rot + 0) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 2, (rand_rot + 0) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 3, (rand_rot + 0) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 4, (rand_rot + 0) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 5, (rand_rot + 0) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 6, (rand_rot + 0) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 7, (rand_rot + 0) % 6, 4, 25)

    time = 142
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time, (rand_rot + 0) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 1, (rand_rot + 0) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 2, (rand_rot + 0) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 3, (rand_rot + 0) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 4, (rand_rot + 0) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 5, (rand_rot + 0) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 6, (rand_rot + 0) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 7, (rand_rot + 0) % 6, 4, 25)

    time = 154
    levels[2].add_bar_point(time, (rand_rot + 0) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 1) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 2) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 3) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 4) % 6, 6, 25)
    time = 155
    rand_rot = rand_rot + 1
    levels[2].add_bar_point(time, (rand_rot + 0) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 1) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 2) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 3) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 4) % 6, 6, 25)
    time = 156
    rand_rot = rand_rot - 1
    levels[2].add_bar_point(time, (rand_rot + 0) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 1) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 2) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 3) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 4) % 6, 6, 25)
    time = 157
    rand_rot = rand_rot + 1
    levels[2].add_bar_point(time, (rand_rot + 0) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 1) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 2) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 3) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 4) % 6, 6, 25)
    time = 158
    rand_rot = rand_rot + 1
    levels[2].add_bar_point(time, (rand_rot + 0) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 1) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 2) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 3) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 4) % 6, 6, 25)
    time = 159
    rand_rot = rand_rot - 1
    levels[2].add_bar_point(time, (rand_rot + 0) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 1) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 2) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 3) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 4) % 6, 6, 25)
    time = 160
    rand_rot = rand_rot + 1
    levels[2].add_bar_point(time, (rand_rot + 0) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 1) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 2) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 3) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 4) % 6, 6, 25)
    time = 161
    rand_rot = rand_rot - 1
    levels[2].add_bar_point(time, (rand_rot + 0) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 1) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 2) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 3) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 4) % 6, 6, 25)
    time = 162
    rand_rot = rand_rot - 1
    levels[2].add_bar_point(time, (rand_rot + 0) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 1) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 2) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 3) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 4) % 6, 6, 25)
    time = 163
    rand_rot = rand_rot + 1
    levels[2].add_bar_point(time, (rand_rot + 0) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 1) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 2) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 3) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 4) % 6, 6, 25)
    time = 164
    rand_rot = rand_rot - 1
    levels[2].add_bar_point(time, (rand_rot + 0) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 1) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 2) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 3) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 4) % 6, 6, 25)
    time = 165
    rand_rot = rand_rot + 1
    levels[2].add_bar_point(time, (rand_rot + 0) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 1) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 2) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 3) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 4) % 6, 6, 25)
    time = 166
    rand_rot = rand_rot + 1
    levels[2].add_bar_point(time, (rand_rot + 0) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 1) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 2) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 3) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 4) % 6, 6, 25)
    time = 167
    rand_rot = rand_rot - 1
    levels[2].add_bar_point(time, (rand_rot + 0) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 1) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 2) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 3) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 4) % 6, 6, 25)
    time = 168
    rand_rot = rand_rot + 1
    levels[2].add_bar_point(time, (rand_rot + 0) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 1) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 2) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 3) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 4) % 6, 6, 25)
    time = 169
    rand_rot = rand_rot - 1
    levels[2].add_bar_point(time, (rand_rot + 0) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 1) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 2) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 3) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 4) % 6, 6, 25)
    time = 170
    rand_rot = rand_rot - 1
    levels[2].add_bar_point(time, (rand_rot + 0) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 1) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 2) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 3) % 6, 6, 25)
    levels[2].add_bar_point(time, (rand_rot + 4) % 6, 6, 25)

    time = 174
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time, (rand_rot + 0) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 1, (rand_rot + 0) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 2, (rand_rot + 0) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 3, (rand_rot + 0) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 4, (rand_rot + 0) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 5, (rand_rot + 0) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 6, (rand_rot + 0) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 7, (rand_rot + 0) % 6, 4, 25)
    time = 182
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time, (rand_rot + 0) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 1, (rand_rot + 0) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 2, (rand_rot + 0) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 3, (rand_rot + 0) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 4, (rand_rot + 0) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 5, (rand_rot + 0) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 6, (rand_rot + 0) % 6, 4, 25)
    rand_rot = random.randint(0, 5)
    levels[2].add_bar_point(time + 7, (rand_rot + 0) % 6, 4, 25)

reload_patterns()