import pygame
import GameMath
import math
import abc
import Settings
import Colors


# La clase Scene se encarga de administrar una escena del juego, cada escena es un momento con diferente dinamica, como
# la pantalla de inicio, la de opciones o el la pantalla de juego.
class Scene:
    currentScene = None


    def __init__(self, screen):
        self.gameObjects = []
        self.screen = screen

        Scene.currentScene = self

    def add_gameobject(self, gameObject):
        self.gameObjects.append(gameObject)
        return gameObject

    def update(self):
        # Update internal elements
        Camera.update_camera()

        # Update GameObjects
        for gameObject in self.gameObjects:
            if gameObject.enabled:
                if gameObject.should_remove:
                    self.gameObjects.remove(gameObject)
                    continue

                gameObject.update()

                if isinstance(gameObject, Drawable) and gameObject.shouldDraw:
                    gameObject.graphic_update_routine()
                    gameObject.draw_on_screen(self.screen)

                elif isinstance(gameObject, GameText) and gameObject.shouldDraw:
                    gameObject.draw_on_screen(self.screen)

        # Draw GUI elements last
        for gameObject in self.gameObjects:
            if gameObject.enabled:
                if gameObject.should_remove:
                    self.gameObjects.remove(gameObject)
                    continue

                if isinstance(gameObject, GUIFigure) and gameObject.shouldDraw:
                    gameObject.draw_on_screen(self.screen)

                elif isinstance(gameObject, GUIText) and gameObject.shouldDraw:
                    gameObject.draw_on_screen(self.screen)


# La camara controla las transformaciones a mayor escala en los GameObjects, cambiando sus propiedades todos los
# objetos presentes en la escena seran transformados.
class Camera:
    pan = (0, 0)
    rotation = 0
    zoom = 1
    angular_speed = 0
    target_zoom = 1

    @staticmethod
    def rotate_from_center(p):
        centerX = -Settings.SCREEN_CENTER[0] - Camera.pan[0]
        centerY = -Settings.SCREEN_CENTER[1] - Camera.pan[1]

        angle = Camera.rotation

        x = centerX * math.cos(angle) - centerX + centerY * math.sin(angle) + p[0] * math.cos(angle) + \
            p[1] * math.sin(angle)
        y = -centerX * math.sin(angle) + centerY * math.cos(angle) - centerY - p[0] * math.sin(angle) + \
            p[1] * math.cos(angle)
        return (x, y)

    @staticmethod
    def scale_from_center(p):
        local_point = (p[0] - Settings.SCREEN_CENTER[0], p[1] - Settings.SCREEN_CENTER[1])
        zoomed_local_point = (local_point[0] * Camera.zoom, local_point[1] * Camera.zoom)
        return (
            zoomed_local_point[0] + Settings.SCREEN_CENTER[0], zoomed_local_point[1] + Settings.SCREEN_CENTER[1])

    @staticmethod
    def update_camera():
        Camera.rotation += Camera.angular_speed
        Camera.zoom = GameMath.lerp(Camera.zoom, Camera.target_zoom, 0.2)


# Cada objeto que se agregue a una escena es un GameObject, estos poseen su comportamiento propio que se
# ajusta mediante su funcion update.
class GameObject:
    def __init__(self):
        self.enabled = True
        self.should_remove = False

    @abc.abstractmethod
    def update(self):
        "Updates the current game object"

    def remove(self):
        self.should_remove = True


# Derivado de GameObjects
# Si su flag shoulDraw es True se dibujara en la pantalla.
# Cada Drawable posee sus propios valores de posicion, rotacion y escala para mostrarse en pantalla.
class Drawable(GameObject):
    def __init__(self, x, y, rotation, vertices, color):
        GameObject.__init__(self)

        self.x = x
        self.y = y
        self.rotation = rotation
        self.scale = 1
        self.vertices = vertices
        self.color = color

        self.shouldDraw = True

    def graphic_update_routine(self):
        self.y = self.y%(2*math.pi)

    def draw_on_screen(self, surface):
        pygame.draw.polygon(surface, Colors.currentPalette[self.color], self.get_window_vertices())

    def get_world_vertices(self):
        world_verts = []

        for v in self.vertices:
            s_x = v[0] * self.scale
            s_y = v[1] * self.scale
            scaled_vert = (s_x,s_y)

            r_x = scaled_vert[0] * math.cos(self.rotation - self.y) + scaled_vert[1] * math.sin(self.rotation - self.y)
            r_y = - scaled_vert[0] * math.sin(self.rotation - self.y) + scaled_vert[1] * math.cos(self.rotation - self.y)


            cart_pos = GameMath.cil2cart(self.x, self.y)
            panned_x = r_x + cart_pos[0]
            panned_y = r_y + cart_pos[1]

            world_verts.append((panned_x, panned_y))

        return world_verts

    def get_camera_vertices(self):
        camera_verts = []

        for v in self.get_world_vertices():
            world_pos_vert = (v[0]+Camera.pan[0], v[1]+Camera.pan[1])
            camera_rotated_vert = Camera.rotate_from_center(world_pos_vert)
            camera_zoomed_vert = Camera.scale_from_center(camera_rotated_vert)
            camera_verts.append(camera_zoomed_vert)

        return camera_verts

    def get_window_vertices(self):
        window_verts = []

        for v in self.get_camera_vertices():
            normalized_vert = (GameMath.inverse_lerp(0, Settings.SCREEN_WIDTH, v[0]), GameMath.inverse_lerp(0, Settings.SCREEN_HEIGHT, v[1]))
            window_verts.append((GameMath.no_clamp_lerp(0,Settings.WINDOW_WIDTH, normalized_vert[0]), GameMath.no_clamp_lerp(0,Settings.WINDOW_HEIGHT, normalized_vert[1])))

        return window_verts


class GameText(GameObject):
    def __init__(self, x, y, size, text, color):
        self.x = x
        self.y = y
        self.size = size
        self.text = text
        self.color = color
        self.shouldDraw = True

        GameObject.__init__(self)

    def draw_on_screen(self, screen):
        myFont = pygame.font.Font('fonts/sun.ttf', self.size)
        textsurface = myFont.render(self.text, False, Colors.currentPalette[self.color])

        surf_pos = self.get_window_pos()

        screen.blit(textsurface, (surf_pos[0], surf_pos[1]))

    def get_world_pos(self):
        return GameMath.cil2cart(self.x, self.y)

    def get_camera_pos(self):
        world_pos = self.get_world_pos()

        panned_pos = (world_pos[0] + Camera.pan[0], world_pos[1] + Camera.pan[1])
        camera_rotated_pos = Camera.rotate_from_center(panned_pos)
        camera_zoomed_pos = Camera.scale_from_center(camera_rotated_pos)

        return camera_zoomed_pos

    def get_window_pos(self):
        camera_pos = self.get_camera_pos()

        normalized_pos = (GameMath.inverse_lerp(0, Settings.SCREEN_WIDTH, camera_pos[0]), GameMath.inverse_lerp(0, Settings.SCREEN_HEIGHT, camera_pos[1]))
        return (GameMath.no_clamp_lerp(0,Settings.WINDOW_WIDTH, normalized_pos[0]), GameMath.no_clamp_lerp(0,Settings.WINDOW_HEIGHT, normalized_pos[1]))


class GUIText(GameObject):
    def __init__(self, x, y, rotation, size, text,color):
        self.x = x
        self.y = y
        self.rotation = rotation
        self.size = size
        self.text = text
        self.color = color
        self.shouldDraw = True
        self.independent_color = False

        GameObject.__init__(self)

    def draw_on_screen(self, screen):
        if self.independent_color:
            color = self.color
        else:
            color = Colors.currentPalette[self.color]

        myFont = pygame.font.Font('fonts/sun.ttf', self.size)
        textsurface = myFont.render(self.text, False, color)

        surf_pos = self.get_window_pos()

        screen.blit(pygame.transform.rotate(textsurface, self.rotation), (surf_pos[0], surf_pos[1]))

    def get_window_pos(self):
        normalized_pos = (GameMath.inverse_lerp(0, Settings.SCREEN_WIDTH, self.x),
                          GameMath.inverse_lerp(0, Settings.SCREEN_HEIGHT, self.y))

        return (GameMath.no_clamp_lerp(0, Settings.WINDOW_WIDTH, normalized_pos[0]),
                GameMath.no_clamp_lerp(0, Settings.WINDOW_HEIGHT, normalized_pos[1]))


class GUIFigure(GameObject):
    def __init__(self, x, y, verts, color):
        GameObject.__init__(self)

        self.x = x
        self.y = y
        self.verts  = verts
        self.color = color
        self.shouldDraw = True
        self.independent_color = True

    def draw_on_screen(self, surface):
        if self.independent_color:
            color = self.color
        else:
            color = Colors.currentPalette[self.color]

        pygame.draw.polygon(surface, color, self.get_window_vertices())

    def get_window_vertices(self):
        verts = []

        for v in self.verts:
            verts.append((v[0]+self.x, v[1]+self.y))

        return verts