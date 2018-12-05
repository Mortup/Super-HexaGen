from GameStructure import *
from GameManager import GameManager
from GameObjects import Obstacle
import MusicManager
import GameMath
import Levels
import Settings

# Spawns the obstacles
class SpawnManager(GameObject):

    def __init__(self):
        GameObject.__init__(self)

    def update(self):
        while (True):
            if Levels.levels[GameManager.currentLevelIndex].bars_points.__len__() <= 0:
                break

            point = Levels.levels[GameManager.currentLevelIndex].bars_points[0]

            if point is None:
                break

            if point[0] * MusicManager.crotchet <= MusicManager.get_song_position():
                Scene.currentScene.add_gameobject(Obstacle(point[1],point[2],point[3]))
                Levels.levels[GameManager.currentLevelIndex].bars_points.pop(0)
            else:
                break


# Controls the 'flow' of the camera (rotation, zooms, etc.)
class CameraManager(GameObject):
    def __init__(self):
        GameObject.__init__(self)

        self.last_beat = 0
        self.current_rotation_point = self.get_rotation_point()

        Camera.angular_speed = Levels.levels[GameManager.currentLevelIndex].starting_rotation

    def update(self):

        if MusicManager.get_song_position() > self.last_beat + MusicManager.crotchet:
            self.last_beat += MusicManager.crotchet
            self.on_beat()

    # Called every beat
    def on_beat(self):
        if not self.current_rotation_point == None:

            if self.current_rotation_point[0] * MusicManager.crotchet <= MusicManager.get_song_position():
                Camera.angular_speed = self.current_rotation_point[1]
                self.current_rotation_point = self.get_rotation_point()

        Camera.zoom = Settings.JUICE_ZOOM

    def get_rotation_point(self):
        if Levels.levels[GameManager.currentLevelIndex].rotation_points.__len__() > 0:
            return Levels.levels[GameManager.currentLevelIndex].rotation_points.pop(0)


# Controls the game color schemes
class PaletteManager(GameObject):

    def __init__(self):
        GameObject.__init__(self)

        self.last_beat = 0
        self.last_changed_beat = 0
        self.beats_to_change = 2
        self.fading_in = True

    def update(self):
        self.update_colors()

        if (MusicManager.get_song_position() > self.last_beat + MusicManager.crotchet):
            self.last_beat += MusicManager.crotchet
            self.on_beat()

    def on_beat(self):
        if MusicManager.get_song_position() > self.last_changed_beat + MusicManager.crotchet * self.beats_to_change:
            self.fading_in = not self.fading_in
            self.last_changed_beat += MusicManager.crotchet * self.beats_to_change

    def update_colors(self):
        current_lerp_time = GameMath.inverse_lerp(self.last_changed_beat, self.last_changed_beat + MusicManager.crotchet * self.beats_to_change, MusicManager.get_song_position())

        p1 = Levels.levels[GameManager.currentLevelIndex].current_palettes[0]
        p2 = Levels.levels[GameManager.currentLevelIndex].current_palettes[1]

        if self.fading_in:
            Colors.currentPalette = GameMath.palette_lerp(p2, p1, current_lerp_time)
        else:
            Colors.currentPalette = GameMath.palette_lerp(p1, p2, current_lerp_time)


# Controls the current center shape of the level
class ShapeManager(GameObject):
    def __init__(self):
        GameObject.__init__(self)

        GameManager.levelCurrentSides = Levels.levels[GameManager.currentLevelIndex].starting_sides_number
        GameManager.levelNextSides = GameManager.levelCurrentSides
        GameManager.sideChangePercent = 0.0

    def update(self):
        while True:
            if Levels.levels[GameManager.currentLevelIndex].shape_change_points.__len__() <= 0:
                break

            point = Levels.levels[GameManager.currentLevelIndex].shape_change_points[0]

            if point is None:
                break

            if point[0] * MusicManager.crotchet <= MusicManager.get_song_position():
                GameManager.levelNextSides = point[1]
                Levels.levels[GameManager.currentLevelIndex].shape_change_points.pop(0)
            else:
                break