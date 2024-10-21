import pygame as pg

SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE
DEFAULT_POSITION = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
SOFT_CYAN = (93, 216, 228)
HOVER_COLOR = (255, 255, 0)

BOARD_BACKGROUND_COLOR = WHITE
BORDER_COLOR = SOFT_CYAN
APPLE_COLOR = RED
SNAKE_COLOR = GREEN


screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

pg.display.set_caption("Змейка")

bg = pg.image.load("img/bg.jpg")
bg = pg.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))

snake_head_image = pg.image.load("img/HEAD.png")
snake_head_image = pg.transform.scale(snake_head_image, (GRID_SIZE, GRID_SIZE))

snake_body_image = pg.image.load("img/BODY.png")
snake_body_image = pg.transform.scale(snake_body_image, (GRID_SIZE, GRID_SIZE))

snake_tail_image = pg.image.load("img/TAIL.png")
snake_tail_image = pg.transform.scale(snake_tail_image, (GRID_SIZE, GRID_SIZE))

corner_image = pg.image.load("img/CORNER.png")
corner_image = pg.transform.scale(corner_image, (GRID_SIZE, GRID_SIZE))

apple_image = pg.image.load("img/apple.png")
apple_image = pg.transform.scale(apple_image, (GRID_SIZE, GRID_SIZE))

stone_image = pg.image.load("img/stone.png")
stone_image = pg.transform.scale(stone_image, (GRID_SIZE, GRID_SIZE))

play_image = pg.image.load("img/PLAY.png")
play_image = pg.transform.scale(play_image, (154, 66))

settings_image = pg.image.load("img/SETTINGS.png")
settings_image = pg.transform.scale(settings_image, (154, 66))

settings_image_all = pg.image.load("img/SETTINGS.png")
settings_image_all = pg.transform.scale(settings_image, (193, 83))

exit_image = pg.image.load("img/EXIT.png")
exit_image = pg.transform.scale(exit_image, (154, 66))

play_image_hover = pg.image.load("img/PLAY_HOVER.png")
play_image_hover = pg.transform.scale(play_image_hover, (154, 66))

settings_image_hover = pg.image.load("img/SETTINGS_HOVER.png")
settings_image_hover = pg.transform.scale(settings_image_hover, (154, 66))

exit_image_hover = pg.image.load("img/EXIT_HOVER.png")
exit_image_hover = pg.transform.scale(exit_image_hover, (154, 66))

back_image = pg.image.load("img/BACK.png")
back_image = pg.transform.scale(back_image, (154, 66))

back_image_hover = pg.image.load("img/BACK_HOVER.png")
back_image_hover = pg.transform.scale(back_image_hover, (154, 66))

menu_image = pg.image.load("img/MENU.png")
menu_image = pg.transform.scale(menu_image, (76, 32))

menu_image_hover = pg.image.load("img/MENU_HOVER.png")
menu_image_hover = pg.transform.scale(menu_image_hover, (76, 32))

easy_image = pg.image.load("img/EASY.png")
easy_image = pg.transform.scale(easy_image, (154, 66))

easy_image_hover = pg.image.load("img/EASY_HOVER.png")
easy_image_hover = pg.transform.scale(easy_image_hover, (154, 66))

middle_image = pg.image.load("img/MIDDLE.png")
middle_image = pg.transform.scale(middle_image, (154, 66))

middle_image_hover = pg.image.load("img/MIDDLE_HOVER.png")
middle_image_hover = pg.transform.scale(middle_image_hover, (154, 66))

hard_image = pg.image.load("img/HARD.png")
hard_image = pg.transform.scale(hard_image, (154, 66))

hard_image_hover = pg.image.load("img/HARD_HOVER.png")
hard_image_hover = pg.transform.scale(hard_image_hover, (154, 66))

blood_image = pg.image.load("img/blood.png")
blood_image = pg.transform.scale(blood_image, (40, 40))

EASY_SETTINGS = {
    "SPEED": 10,
    "COUNT_STONE": 3,
}

MEDIUM_SETTINGS = {
    "SPEED": 15,
    "COUNT_STONE": 5,
}

HARD_SETTINGS = {
    "SPEED": 20,
    "COUNT_STONE": 7,
}

DEFAULT_SPEED = MEDIUM_SETTINGS["SPEED"]
DEFAULT_COUNT_STONE = MEDIUM_SETTINGS["COUNT_STONE"]

clock = pg.time.Clock()
