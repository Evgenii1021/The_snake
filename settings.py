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

BOARD_BACKGROUND_COLOR = WHITE
BORDER_COLOR = SOFT_CYAN
APPLE_COLOR = RED
SNAKE_COLOR = GREEN

SPEED = 15

COUNT_STONE = 3

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

# font = pg.font.Font("arial", 24)


clock = pg.time.Clock()
