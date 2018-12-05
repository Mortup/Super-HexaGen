from JuiceManager import *
from GameObjects import *
from Menu_Objects import *
import Settings
from GameManager import GameManager

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
screen = pygame.display.set_mode((Settings.WINDOW_WIDTH, Settings.WINDOW_HEIGHT))
done = False

clock = pygame.time.Clock()

clock.tick(3)


def load_main_menu(screen):
    scene = Scene(screen)

    GameManager.levelCurrentSides = 6
    GameManager.levelNextSides = 6

    scene.add_gameobject(MenuManager())

    scene.add_gameobject(BackgroundBar(5))
    scene.add_gameobject(BackgroundBar(4))
    scene.add_gameobject(BackgroundBar(3))
    scene.add_gameobject(BackgroundBar(2))
    scene.add_gameobject(BackgroundBar(1))
    scene.add_gameobject(BackgroundBar(0))

    scene.add_gameobject(MenuHexagon(False))
    scene.add_gameobject(MenuHexagon(True))

    scene.add_gameobject(PlayText())
    scene.add_gameobject(CreditsText())
    scene.add_gameobject(CreditsContent(0))
    scene.add_gameobject(CreditsContent(1))
    scene.add_gameobject(CreditsContent(2))
    scene.add_gameobject(LevelText(0))
    scene.add_gameobject(LevelText(1))
    scene.add_gameobject(LevelText(2))
    scene.add_gameobject(LevelPointer())
    scene.add_gameobject(HideIfSelectingText(480, 5 * math.pi / 6, 40, "Exit", 3))
    scene.add_gameobject(GUIText(450,50,0,60,"Super HexaGon", 3))
    scene.add_gameobject(GUIText(620, 460, 0, 20, "Made by Mortup (Gonzalo Uribe)", 3))
    scene.add_gameobject(GUIText(80, 200, 0, 20, "ENTER", 3))
    scene.add_gameobject(GUIText(75, 220, 0, 20, "to select", 3))
    scene.add_gameobject(GUIText(40, 265, 0, 15, "BACKSPACE to go back", 3))
    scene.add_gameobject(GUIText(10, 460, 0, 20, Settings.CURRENT_VER, 3))

    Camera.pan = (-Settings.SCREEN_WIDTH/2 * (0.75), 0)
    Camera.angular_speed = 0
    Camera.rotation = math.pi/6

    return scene

def load_game_scene(screen, index):
    scene = Scene(screen)

    GameManager.currentLevelIndex = index
    Levels.reload_patterns()

    # Add managers
    scene.add_gameobject(GameManager())
    scene.add_gameobject(CameraManager())
    scene.add_gameobject(PaletteManager())
    scene.add_gameobject(SpawnManager())
    scene.add_gameobject(ShapeManager())

    # Add actors
    scene.add_gameobject(BackgroundBar(5))
    scene.add_gameobject(BackgroundBar(4))
    scene.add_gameobject(BackgroundBar(3))
    scene.add_gameobject(BackgroundBar(2))
    scene.add_gameobject(BackgroundBar(1))
    scene.add_gameobject(BackgroundBar(0))
    scene.add_gameobject(Player())
    scene.add_gameobject(CenterPolygon(False))
    scene.add_gameobject(CenterPolygon(True))

    # Add UI Elements
    scene.add_gameobject(TimerBackground())
    scene.add_gameobject(TimerUI())

    Camera.zoom = 1
    Camera.pan = (0,0)
    MusicManager.play(GameManager.currentLevelIndex)

    GameManager.is_game_over = False
    Obstacle.current_obstacles = []

    return scene


def load_win_screen(screen):
    pygame.mixer.music.fadeout(2500)
    scene = Scene(screen)

    bg = scene.add_gameobject(GUIFigure(0,0,[(0,0),(0,Settings.WINDOW_HEIGHT),(Settings.WINDOW_WIDTH,Settings.WINDOW_HEIGHT),(Settings.WINDOW_WIDTH,0)], 0))
    bg.independent_color = False

    scene.add_gameobject(GUIText(130,100,0,100,"Level Complete", 3))
    scene.add_gameobject(GUIText(230, 250, 0, 40, "Press ENTER to continue", 3))
    scene.add_gameobject(WinScreenLogic())

    return scene


def load_death_screen(screen):
    scene = Scene(screen)

    pygame.mixer.music.fadeout(500)

    bg = scene.add_gameobject(GUIFigure(0,0,[(0,0),(0,Settings.WINDOW_HEIGHT),(Settings.WINDOW_WIDTH,Settings.WINDOW_HEIGHT),(Settings.WINDOW_WIDTH,0)], 0))
    bg.independent_color = False

    scene.add_gameobject(GUIText(235,100,0,100,"You Failed", 3))
    scene.add_gameobject(GUIText(290, 250, 0, 40, "Press R to try again", 3))
    scene.add_gameobject(GUIText(180, 280, 0, 40, "Press ENTER to go to the main menu", 3))
    scene.add_gameobject(WinScreenLogic())

    return scene

current_scene = load_main_menu(screen)

last_pressed_r = 0
while not done:
    # Close with the pygame event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Close when the player hits esc
    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
        done = True

    if (pygame.key.get_pressed()[pygame.K_r] and last_pressed_r == 0):
        current_scene = load_game_scene(screen, GameManager.currentLevelIndex)

    if (GameManager.is_game_over):
        current_scene = load_death_screen(screen)
        GameManager.is_game_over = False

    if not MenuManager.level_to_load == -1:
        index = MenuManager.level_to_load
        MenuManager.level_to_load = -1
        current_scene = load_game_scene(screen, index)

    if MenuManager.should_load_menu:
        current_scene = load_main_menu(screen)
        MenuManager.should_load_menu = False

    if GameManager.should_load_win:
        current_scene = load_win_screen(screen)
        GameManager.should_load_win = False

    last_pressed_r = pygame.key.get_pressed()[pygame.K_r]

    screen.fill((0,0,0))
    current_scene.update()

    pygame.display.flip()
    clock.tick(Settings.FPS)