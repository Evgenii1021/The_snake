"""
Модуль с настройками и константами для игры 'Змейка'.

Содержит определения размеров экрана, размеров игровых объектов и
различные константы, необходимые для работы игры.

Константы:
- SCREEN_WIDTH, SCREEN_HEIGHT: размеры окна игры.
- GRID_SIZE_SNAKE: размер клетки для змейки.
- GRID_SIZE_SOLDIER: размер клетки для солдата.
- SIZE_TANK_WIDTH, SIZE_TANK_HEIGHT: размеры танка.
- GRID_WIDTH, GRID_HEIGHT: размеры игрового поля в клетках.
- DEFAULT_POSITION: начальная позиция змейки на экране.

Направления движения:
- UP, DOWN, LEFT, RIGHT: кортежи, определяющие направления движения.

Цвета:
- WHITE: цвет белый в RGB формате.
- BOARD_BACKGROUND_COLOR: цвет фона игрового поля.

Загрузка изображений:
- Изображения для различных объектов игры (змейка, солдаты, танки, кнопки меню)
  загружаются и изменяются по размеру для корректного отображения.

Настройки сложности:
- EASY_SETTINGS, MEDIUM_SETTINGS, HARD_SETTINGS: словари с параметрами
  скорости и количества препятствий для каждого уровня сложности.

DEFAULT_SPEED и DEFAULT_COUNT_TANK: значения по умолчанию для
  скорости игры и количества танков.

clock: объект для контроля времени и частоты обновления кадров в игре.
"""

import pygame as pg

SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE_SNAKE = 20
GRID_SIZE_SOLDIER = 40
SIZE_TANK_HEIGHT = 40
SIZE_TANK_WIDTH = 60
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE_SNAKE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE_SNAKE
DEFAULT_POSITION = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

WHITE = (255, 255, 255)

BOARD_BACKGROUND_COLOR = WHITE

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

pg.display.set_caption("Змейка")

bg = pg.image.load("img/bg.jpg")
bg = pg.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))

snake_head_image = pg.image.load("img/HEAD.png")
snake_head_image = pg.transform.scale(
    snake_head_image, (GRID_SIZE_SNAKE, GRID_SIZE_SNAKE)
)

snake_body_image = pg.image.load("img/BODY.png")
snake_body_image = pg.transform.scale(
    snake_body_image, (GRID_SIZE_SNAKE, GRID_SIZE_SNAKE)
)

snake_tail_image = pg.image.load("img/TAIL.png")
snake_tail_image = pg.transform.scale(
    snake_tail_image, (GRID_SIZE_SNAKE, GRID_SIZE_SNAKE)
)

corner_image = pg.image.load("img/CORNER.png")
corner_image = pg.transform.scale(
    corner_image, (GRID_SIZE_SNAKE, GRID_SIZE_SNAKE)
)

soldier_image = pg.image.load("img/soldier2.png")
soldier_image = pg.transform.scale(
    soldier_image, (GRID_SIZE_SOLDIER, GRID_SIZE_SOLDIER)
)
blood_image = pg.image.load("img/blood.png")
blood_image = pg.transform.scale(blood_image, (40, 40))

tank_image = pg.image.load("img/tank.png")
tank_image = pg.transform.scale(tank_image,
                                (SIZE_TANK_WIDTH, SIZE_TANK_HEIGHT))

play_image = pg.image.load("img/but/PLAY.png")
play_image = pg.transform.scale(play_image, (154, 66))

settings_image = pg.image.load("img/but/SETTINGS.png")
settings_image = pg.transform.scale(settings_image, (154, 66))

settings_image_all = pg.image.load("img/but/SETTINGS.png")
settings_image_all = pg.transform.scale(settings_image, (193, 83))

exit_image = pg.image.load("img/but/EXIT.png")
exit_image = pg.transform.scale(exit_image, (154, 66))

play_image_hover = pg.image.load("img/but/PLAY_HOVER.png")
play_image_hover = pg.transform.scale(play_image_hover, (154, 66))

settings_image_hover = pg.image.load("img/but/SETTINGS_HOVER.png")
settings_image_hover = pg.transform.scale(settings_image_hover, (154, 66))

exit_image_hover = pg.image.load("img/but/EXIT_HOVER.png")
exit_image_hover = pg.transform.scale(exit_image_hover, (154, 66))

back_image = pg.image.load("img/but/BACK.png")
back_image = pg.transform.scale(back_image, (154, 66))

back_image_hover = pg.image.load("img/but/BACK_HOVER.png")
back_image_hover = pg.transform.scale(back_image_hover, (154, 66))

menu_image = pg.image.load("img/but/MENU.png")
menu_image = pg.transform.scale(menu_image, (76, 32))

menu_image_hover = pg.image.load("img/but/MENU_HOVER.png")
menu_image_hover = pg.transform.scale(menu_image_hover, (76, 32))

easy_image = pg.image.load("img/but/EASY.png")
easy_image = pg.transform.scale(easy_image, (154, 66))

easy_image_hover = pg.image.load("img/but/EASY_HOVER.png")
easy_image_hover = pg.transform.scale(easy_image_hover, (154, 66))

middle_image = pg.image.load("img/but/MIDDLE.png")
middle_image = pg.transform.scale(middle_image, (154, 66))

middle_image_hover = pg.image.load("img/but/MIDDLE_HOVER.png")
middle_image_hover = pg.transform.scale(middle_image_hover, (154, 66))

hard_image = pg.image.load("img/but/HARD.png")
hard_image = pg.transform.scale(hard_image, (154, 66))

hard_image_hover = pg.image.load("img/but/HARD_HOVER.png")
hard_image_hover = pg.transform.scale(hard_image_hover, (154, 66))


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
DEFAULT_COUNT_TANK = MEDIUM_SETTINGS["COUNT_STONE"]

clock = pg.time.Clock()
