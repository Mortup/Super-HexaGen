from GameStructure import GameObject
from GameStructure import Drawable
from GameStructure import Camera
from GameStructure import GameText
from GameStructure import GUIFigure
from GameObjects import GameManager
import Colors
import GameMath
import Settings
import math
import pygame
import sys


class MenuManager(GameObject):
    selectingLevels = False
    showingCredits = False
    should_load_menu = False

    level_to_load = -1

    def __init__(self):
        self.currentTarget = 0
        self.level_to_play = 0

        self.previous_left = False
        self.previous_right = False
        self.previous_up = False
        self.previous_down = False
        self.last_enter = True

        GameObject.__init__(self)

        self.switch_fx = pygame.mixer.Sound('audio/click.wav')
        self.sweep_fx = pygame.mixer.Sound('audio/sweep.wav')

    def update(self):
        if not MenuManager.showingCredits and not MenuManager.selectingLevels:
            if (pygame.key.get_pressed()[pygame.K_RIGHT] or pygame.key.get_pressed()[pygame.K_DOWN]) and not self.previous_right and not self.previous_down:
                self.switch_fx.play()

                if self.currentTarget == 2:
                    Camera.rotation = -2 * math.pi / 6 + math.pi / 6
                self.currentTarget += 1

            if (pygame.key.get_pressed()[pygame.K_LEFT] or pygame.key.get_pressed()[pygame.K_UP]) and not self.previous_left and not self.previous_up:
                self.switch_fx.play()

                if self.currentTarget == 0:
                    Camera.rotation = 8 * math.pi / 6
                self.currentTarget -= 1


        if pygame.key.get_pressed()[pygame.K_RETURN] and not self.last_enter:
            if self.currentTarget == 0 and not MenuManager.selectingLevels: # Play
                MenuManager.selectingLevels = True
                LevelPointer.current_level = 0
                self.sweep_fx.play()
            elif self.currentTarget == 1 and not MenuManager.showingCredits: # Credits
                MenuManager.showingCredits = True
                self.sweep_fx.play()
            elif self.currentTarget == 2: # Exit
                self.sweep_fx.play()
                pygame.quit()
                sys.exit(0)
            elif self.currentTarget == 0 and MenuManager.selectingLevels: # Confirm level selection
                MenuManager.level_to_load = LevelPointer.current_level
                self.sweep_fx.play()

        if pygame.key.get_pressed()[pygame.K_BACKSPACE]:
            if MenuManager.selectingLevels or MenuManager.showingCredits:
                self.sweep_fx.play()

            MenuManager.selectingLevels = False
            MenuManager.showingCredits = False

        self.currentTarget = self.currentTarget%3
        self.level_to_play = self.level_to_play%3

        self.previous_left = pygame.key.get_pressed()[pygame.K_LEFT]
        self.previous_right = pygame.key.get_pressed()[pygame.K_RIGHT]
        self.previous_up = pygame.key.get_pressed()[pygame.K_UP]
        self.previous_down = pygame.key.get_pressed()[pygame.K_DOWN]
        self.last_enter = pygame.key.get_pressed()[pygame.K_RETURN]

        Camera.rotation = GameMath.lerp(Camera.rotation, self.currentTarget*math.pi/3 + math.pi/6, 0.15)
        Colors.currentPalette = GameMath.palette_lerp(Colors.currentPalette, Colors.menuPalettes[self.currentTarget], 0.15)

class MenuHexagon(Drawable):

    def __init__(self, inner):
        color = 3

        if inner:
            color = 2

        Drawable.__init__(self, 0, 0, 0, self.get_initial_verts(), color)

        if inner:
            self.scale = 0.8

    def get_initial_verts(self):
        verts = []
        for i in range(6):
            verts.append(GameMath.cil2cart_local(Settings.MENU_HEXAGON_RADIUS,i*math.pi*2/6))

        return verts

class PlayText(GameText):
    def __init__(self):
        GameText.__init__(self, 480, math.pi / 6, 40, "Play", 3)

    def update(self):
        if MenuManager.selectingLevels and self.x - 150 > 3:
            self.x = GameMath.lerp(self.x, 150, 0.1)
        elif (not MenuManager.selectingLevels) and 480 - self.x > 3:
            self.x = GameMath.lerp(self.x, 480, 0.1)

class CreditsText(GameText):
    def __init__(self):
        GameText.__init__(self, 460, 3 * math.pi / 6, 40, "Credits", 3)

    def update(self):
        left_pos = 150
        right_pos = 460

        if MenuManager.showingCredits and self.x - left_pos > 3:
            self.x = GameMath.lerp(self.x, left_pos, 0.1)
        elif (not MenuManager.showingCredits) and right_pos - self.x > 3:
            self.x = GameMath.lerp(self.x, right_pos, 0.1)

        self.shouldDraw = not MenuManager.selectingLevels


class CreditsContent(GameText):
    def __init__(self, line):
        if line == 0:
            text = "Game made by Mortup (Gonzalo Uribe)"
            self.left_pos = 400
            pos_y = 2.8 * math.pi / 6
        if line == 1:
            text = "Only for educational purposes"
            self.left_pos = 450
            pos_y = 3 * math.pi / 6
        if line == 2:
            text = "Inspired by Terry Cavanagh's 'Super Hexagon'"
            self.left_pos = 330
            pos_y = 3.2 * math.pi / 6

        self.right_pos = 800
        GameText.__init__(self, self.right_pos, pos_y, 25, text, 3)

    def update(self):
        if MenuManager.showingCredits and self.x - self.left_pos > 3:
            self.x = GameMath.lerp(self.x, self.left_pos, 0.1)
        elif (not MenuManager.showingCredits) and self.right_pos - self.x > 3:
            self.x = GameMath.lerp(self.x, self.right_pos, 0.1)

        self.shouldDraw = not MenuManager.selectingLevels

class HideIfSelectingText(GameText):
    def __init__(self, x, y, size, text, color):
        GameText.__init__(self, x, y, size, text, color)

    def update(self):
        self.shouldDraw = not MenuManager.selectingLevels


class LevelText(GameText):
    def __init__(self, index):
        if index == 0:
            text = "HARD"
            self.left_pos = 455
            pos_y = 0.8 * math.pi / 6
        if index == 1:
            text = "VERY HARD"
            self.left_pos = 450
            pos_y = 1 * math.pi / 6
        if index == 2:
            text = "IMPOSSIBLE"
            self.left_pos = 455
            pos_y = 1.2 * math.pi / 6

        if GameManager.levels_completed[index] == 1:
            text = text + " [COMPLETED]"

        self.right_pos = 800
        GameText.__init__(self, self.right_pos, pos_y, 25, text, 3)

    def update(self):
        if MenuManager.selectingLevels and self.x - self.left_pos > 3:
            self.x = GameMath.lerp(self.x, self.left_pos, 0.1)
        elif (not MenuManager.selectingLevels) and self.right_pos - self.x > 3:
            self.x = GameMath.lerp(self.x, self.right_pos, 0.1)

class LevelPointer(GUIFigure):
    current_level = 0

    def __init__(self):
        GUIFigure.__init__(self,830,296,[(0,0),(-20,10),(-20,-10)], 3)
        self.independent_color = False

        self.last_down = False
        self.last_up = False

    def update(self):
        self.shouldDraw = MenuManager.selectingLevels

        if pygame.key.get_pressed()[pygame.K_DOWN] and not self.last_down:
            LevelPointer.current_level += 1
        if pygame.key.get_pressed()[pygame.K_UP] and not self.last_up:
            LevelPointer.current_level -= 1

        LevelPointer.current_level = LevelPointer.current_level%3

        self.last_down = pygame.key.get_pressed()[pygame.K_DOWN]
        self.last_up = pygame.key.get_pressed()[pygame.K_UP]


        self.y = LevelPointer.current_level * 73 + 296


class WinScreenLogic(GameObject):
    def __init__(self):
        GameObject.__init__(self)

    def update(self):
        if pygame.key.get_pressed()[pygame.K_RETURN]:
            MenuManager.should_load_menu = True
