from GameStructure import GameObject
from GameStructure import Drawable
from GameStructure import GUIFigure
from GameStructure import GUIText
from GameManager import GameManager
from GameStructure import Camera
import Settings
import GameMath
import pygame
import math
import MusicManager
import NeuralInterface


# The player Drawable object
class Player(Drawable):
    current_speed = 0
    max_speed = 0.08
    acceleration = 0.03
    drag = 0.7
    max_movement_rotation = 50 * math.pi / 180

    def __init__(self):
        Drawable.__init__(self, 100, 3*math.pi/2, 0, [(-10, -10), (-10, 10), (9, 0)], 3)

    def update(self):
        self.move_with_network()
        self.move()
        self.set_rotation()
        self.check_collisions()

    def move_with_network(self):
        NeuralInterface.feed(Obstacle.current_obstacles, self.y)

    def move(self):
        # Modify current_speed
        is_moving = False
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            is_moving = True
            self.current_speed += self.acceleration

        if pygame.key.get_pressed()[pygame.K_LEFT]:
            is_moving = True
            self.current_speed -= self.acceleration

        if not is_moving:
            self.current_speed *= self.drag

        # Clamp speed
        if self.current_speed > self.max_speed: self.current_speed = self.max_speed
        if self.current_speed < -self.max_speed: self.current_speed = -self.max_speed

        # Check if can move there

        lback_mag = self.get_lback_pos()[0]
        rback_mag = self.get_rback_pos()[0]
        lback_angle = self.get_lback_pos()[1]
        rback_angle = self.get_rback_pos()[1]


        for obs in Obstacle.current_obstacles:
            if obs.is_on_angle(lback_angle + self.current_speed) and obs.get_max_magnitude(self.y) > lback_mag > obs.get_min_magnitude(self.y):
                self.current_speed = 0
                self.y = obs.vert_angle + (math.pi / GameManager.levelCurrentSides) + 0.07
            elif obs.is_on_angle(rback_angle + self.current_speed) and obs.get_max_magnitude(self.y) > rback_mag > obs.get_min_magnitude(self.y):
                self.current_speed = 0
                self.y = obs.vert_angle - (math.pi / GameManager.levelCurrentSides) - 0.07

        self.y += self.current_speed

    def set_rotation(self):
        # Extra movement rotation
        extra_rotation = -(self.current_speed / self.max_speed) * self.max_movement_rotation

        self.rotation = extra_rotation

    def check_collisions(self):
        head_mag = self.get_head_pos()[0]

        for obs in Obstacle.current_obstacles:
            if obs.is_on_angle(self.y) and obs.get_max_magnitude(self.y) > head_mag > obs.get_min_magnitude(self.y):
                GameManager.game_over()

    def get_head_pos(self):
        return (self.x + 9, self.y)

    def get_lback_pos(self):
        return (self.x - 10, self.y - 0.035)

    def get_rback_pos(self):
        # TODO: Fix width
        return (self.x - 10, self.y + 0.035)

# 6 BackgroundBars make the background.
class BackgroundBar(Drawable):
    def __init__(self, index):
        self.index = index  # Used to identify each background bar. Goes from 0 to 5.

        self.max_screen_size = max(Settings.SCREEN_HEIGHT, Settings.SCREEN_WIDTH)

        Drawable.__init__(self, 0, 0, 0, [], -1)
        self.set_vertices()

    def update(self):
        # Set the should_draw variable and if its true update/set the colors and vertices.
        if self.check_if_draw():
            self.setColor()
            self.set_vertices()

    def set_vertices(self):
        min_sides = min(GameManager.levelCurrentSides, GameManager.levelNextSides)

        start_delta_angle = (2 * math.pi / GameManager.levelCurrentSides)
        end_delta_angle = (2 * math.pi / GameManager.levelNextSides)

        current_delta_angle = GameMath.pow_lerp(start_delta_angle, end_delta_angle, GameManager.sideChangePercent,
                                                Settings.LERP_POW)

        vert1 = (0, 0)
        vert2 = GameMath.cil2cart_local(self.max_screen_size * 2, current_delta_angle * self.index)
        vert3 = GameMath.cil2cart_local(self.max_screen_size * 2, current_delta_angle * (self.index + 1))

        if GameManager.sideChangePercent != 0 and self.index >= min_sides:
            if GameManager.levelCurrentSides > GameManager.levelNextSides:
                vert2 = GameMath.cil2cart_local(self.max_screen_size * 2, start_delta_angle * self.index)
                vert3 = GameMath.cil2cart_local(self.max_screen_size * 2,
                                                GameMath.pow_lerp(start_delta_angle * (self.index + 1), 2 * math.pi,
                                                                  GameManager.sideChangePercent, Settings.LERP_POW))
            else:
                vert2 = GameMath.cil2cart_local(self.max_screen_size * 2, end_delta_angle * self.index)
                vert3 = GameMath.cil2cart_local(self.max_screen_size * 2,
                                                GameMath.pow_lerp(2 * math.pi, end_delta_angle * (self.index + 1),
                                                                  GameManager.sideChangePercent, Settings.LERP_POW))

        self.vertices = [vert1, vert2, vert3]

    def check_if_draw(self):
        if GameManager.levelCurrentSides > GameManager.levelNextSides:
            self.shouldDraw = self.index <= GameManager.levelCurrentSides - 1
        else:
            self.shouldDraw = self.index <= GameManager.levelNextSides - 1

        return self.shouldDraw

    def setColor(self):
        if GameManager.levelCurrentSides == 6:
            self.color = self.index%2
        elif GameManager.levelCurrentSides == 5:
            self.color = self.index % 2
            if self.index == 4: self.color = 2
        elif GameManager.levelCurrentSides == 4:
            self.color = self.index % 2
            if self.index == 4: self.color = 2
        else:
            self.color = self.index % 3
            if self.index == 3: self.color = 1


class CenterPolygon(Drawable):
    polygonSize = Settings.CENTER_POLYGON_RADIUS

    def __init__(self, inner):
        self.inner = inner

        if self.inner: color = 2
        else: color = 3

        Drawable.__init__(self, 0, 0, 0, self.get_polygon_vertices(4), color)

        if inner:
            self.scale = 0.8

    def update(self):
        if self.inner:
            self.scale = 0.8 * (((Camera.zoom - 1) * Settings.JUICE_CENTER_MULTIPLIER) + 1)
        else:
            self.scale = (((Camera.zoom - 1) * Settings.JUICE_CENTER_MULTIPLIER) + 1)

        self.vertices = self.get_lerped_vertices(GameManager.levelCurrentSides, GameManager.levelNextSides, GameManager.sideChangePercent)

    def get_polygon_vertices(self, sides):
        verts = []

        delta_angle = 2*math.pi/sides

        for i in range(sides):
            verts.append(GameMath.cil2cart_local(self.polygonSize, i*delta_angle))

        return verts

    def get_lerped_vertices(self, start_sides, end_sides, t):
        min_sides = min(start_sides, end_sides)
        power_to_lerp = Settings.LERP_POW

        verts = []
        start_delta_angle = 2 * math.pi / start_sides
        end_delta_angle = 2 * math.pi / end_sides

        current_delta_angle = GameMath.pow_lerp(start_delta_angle, end_delta_angle, t, power_to_lerp)

        for i in range(min_sides):
            verts.append(GameMath.cil2cart_local(self.polygonSize, i*current_delta_angle))

        for i in range(abs(start_sides-end_sides)):
            if start_sides > end_sides:
                extra_end_angle = 2 * math.pi
                extra_current_delta_angle = GameMath.pow_lerp(start_delta_angle * (i + min_sides), extra_end_angle, t, power_to_lerp)
                verts.append(GameMath.cil2cart_local(self.polygonSize, extra_current_delta_angle))
            else:
                extra_start_angle = 2 * math.pi
                extra_current_angle = GameMath.pow_lerp(extra_start_angle, end_delta_angle * (i+min_sides), t, power_to_lerp)
                verts.append(GameMath.cil2cart_local(self.polygonSize, extra_current_angle))

        return verts


class Obstacle(Drawable):
    current_obstacles = []

    def __init__(self, posIndex, speed, width):
        self.posIndex = posIndex
        self.speed = speed
        self.width = width

        Drawable.__init__(self, 0, 0, 0, [(0, 0), (0, 10), (10, 0)], 3)

        starting_pos = self.get_starting_pos()
        self.vert_mag =  starting_pos[0]
        self.vert_angle = starting_pos[1]

        self.set_verts()
        Obstacle.current_obstacles.append(self)

    def update(self):
        self.set_vert_position()
        self.set_verts()
        self.set_drawable()

        # Kill if it has reached center
        if self.vert_mag <= Settings.CENTER_POLYGON_RADIUS:
            self.remove()

    def get_starting_pos(self):
        max_screen_side = max(Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT)
        magnitude = max_screen_side * 0.6 + self.width/2

        angle = self.get_angle()

        return (magnitude, angle)

    def get_angle(self):
        angle = (self.posIndex + 0.5) * (math.pi * 2 / GameManager.levelCurrentSides)

        if GameManager.sideChangePercent != 0:
            min_sides = min(GameManager.levelCurrentSides, GameManager.levelNextSides)
            start_angle = (self.posIndex + 0.5) * (math.pi * 2 / GameManager.levelCurrentSides)
            end_angle = (self.posIndex + 0.5) * (math.pi * 2 / GameManager.levelNextSides)

            if self.posIndex >= min_sides:
                if min_sides == GameManager.levelNextSides:
                    end_angle = 2 * math.pi
                else:
                    start_angle = 2 * math.pi

            angle = GameMath.pow_lerp(start_angle, end_angle, GameManager.sideChangePercent, Settings.LERP_POW)

        return angle

    def set_drawable(self):
        if GameManager.sideChangePercent == 0:
            self.shouldDraw = self.posIndex < GameManager.levelCurrentSides
        else:
            max_sides = max(GameManager.levelCurrentSides, GameManager.levelNextSides)
            self.shouldDraw = self.posIndex < max_sides

    def set_vert_position(self):
        newMagnitude = self.vert_mag - self.speed * Settings.OBSTACLE_SPEED_MULTIPLIER

        self.vert_mag = newMagnitude
        self.vert_angle = self.get_angle()

    def set_verts(self):
        delta_angle = math.pi / GameManager.levelCurrentSides

        if GameManager.sideChangePercent != 0:
            min_sides = min(GameManager.levelCurrentSides,GameManager.levelNextSides)
            if self.posIndex < min_sides:
                delta_angle = GameMath.pow_lerp(math.pi / GameManager.levelCurrentSides, math.pi / GameManager.levelNextSides, GameManager.sideChangePercent, Settings.LERP_POW)
            else:
                if min_sides == GameManager.levelNextSides:
                    delta_angle = GameMath.pow_lerp(math.pi / GameManager.levelCurrentSides, 0, GameManager.sideChangePercent, Settings.LERP_POW)
                else:
                    delta_angle = GameMath.pow_lerp(0, math.pi / GameManager.levelNextSides, GameManager.sideChangePercent, Settings.LERP_POW)

        vert1 = GameMath.cil2cart_local(self.vert_mag - self.width / 2, self.vert_angle + delta_angle)
        vert2 = GameMath.cil2cart_local(self.vert_mag - self.width / 2, self.vert_angle - delta_angle)
        vert3 = GameMath.cil2cart_local(self.vert_mag + self.width / 2, self.vert_angle + delta_angle)
        vert4 = GameMath.cil2cart_local(self.vert_mag + self.width / 2, self.vert_angle - delta_angle)

        self.vertices = [vert1, vert2, vert4, vert3]

    def is_on_angle(self, angle):
        delta_angle = math.pi / GameManager.levelCurrentSides

        return self.vert_angle - delta_angle < angle < self.vert_angle + delta_angle

    def get_min_magnitude(self, angle):

        delta_angle = math.pi / GameManager.levelCurrentSides
        p1 = GameMath.cil2cart_local(self.vert_mag - self.width / 2, self.vert_angle - delta_angle)
        p2 = GameMath.cil2cart_local(self.vert_mag - self.width / 2, self.vert_angle + delta_angle)
        p3 = (0,0)
        p4 = (math.cos(angle),math.sin(angle))

        intersection = GameMath.intersection_between_lines(p1,p2,p3,p4)
        return GameMath.cart2cil_local(intersection[0], intersection[1])[0]

    def get_max_magnitude(self, angle):

        delta_angle = math.pi / GameManager.levelCurrentSides
        p1 = GameMath.cil2cart_local(self.vert_mag + self.width / 2, self.vert_angle - delta_angle)
        p2 = GameMath.cil2cart_local(self.vert_mag + self.width / 2, self.vert_angle + delta_angle)
        p3 = (0,0)
        p4 = (math.cos(angle),math.sin(angle))

        intersection = GameMath.intersection_between_lines(p1,p2,p3,p4)
        return GameMath.cart2cil_local(intersection[0], intersection[1])[0]


    def remove(self):
        Obstacle.current_obstacles.remove(self)

        GameObject.remove(self)

    # Collisions won't work when the sides number is changing.
    def get_bottom_left(self):
        delta_angle = math.pi / GameManager.levelCurrentSides

        return (self.vert_mag - self.width/2, self.vert_angle - delta_angle)

    # Collisions won't work when the sides number is changing.
    def get_upper_right(self):
        delta_angle = math.pi / GameManager.levelCurrentSides
        return (self.vert_mag + self.width/2, self.vert_angle + delta_angle)

class DebugTarget(Drawable):

    def __init__(self, target):
        self.target = target

        Drawable.__init__(self, target.x, target.y, target.rotation, [(-5, -5), (-5, 5), (5, 5), (5, -5)], 2)

    def update(self):
        if Obstacle.current_obstacles.__len__() < 0:
            return

        for obs in Obstacle.current_obstacles:
            if obs.is_on_angle(self.target.y):
                self.x = obs.get_max_magnitude(self.target.y)
                self.y = self.target.y
                self.rotation = self.target.rotation


class TimerUI(GUIText):
    def __init__(self):
        GUIText.__init__(self, Settings.SCREEN_WIDTH - 175, 10, 0, 30, "Time: ",(255,255,255))

        self.independent_color = True

    def update(self):
        time = MusicManager.get_song_position()/1000
        time = int((time * 100) + 0.5) / 100.0

        if (time < 0):
            time = 0.00

        self.text = "Time: " + str(time)


class TimerBackground(GUIFigure):
    def __init__(self):
        GUIFigure.__init__(self, Settings.SCREEN_WIDTH + 150, 0, [(0,0),(350,0),(350,60),(15,60),(0,45)], (0,0,0))
