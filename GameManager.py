from GameStructure import GameObject
import Settings
import pygame
import Levels
import MusicManager

class GameManager(GameObject):
    currentLevelIndex = -1

    levelCurrentSides = 6
    levelNextSides = 6
    sideChangePercent = 0

    last_beat = 0;

    is_game_over = False
    should_load_win = False

    levels_completed = [0,0,0]

    def __init__(self):
        GameObject.__init__(self)

    def update(self):
        if GameManager.levelCurrentSides != GameManager.levelNextSides: GameManager.sideChangePercent += Settings.TRANSITIONS_SPEED

        if GameManager.sideChangePercent > 1:
            GameManager.sideChangePercent = 0
            GameManager.levelCurrentSides = GameManager.levelNextSides

        if (pygame.key.get_pressed()[pygame.K_3]):
            GameManager.levelNextSides = 3
        if (pygame.key.get_pressed()[pygame.K_4]):
            GameManager.levelNextSides = 4
        if (pygame.key.get_pressed()[pygame.K_5]):
            GameManager.levelNextSides = 5
        if (pygame.key.get_pressed()[pygame.K_6]):
            GameManager.levelNextSides = 6

        # Check win condition
        if Levels.levels[GameManager.currentLevelIndex].bars_to_win * MusicManager.crotchet <= MusicManager.get_song_position():
            GameManager.should_load_win = True
            GameManager.levels_completed[GameManager.currentLevelIndex] = 1

    @staticmethod
    def game_over():
        GameManager.is_game_over = True