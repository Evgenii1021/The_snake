import pygame as pg
from random import choice, randrange

from settings import (
    DEFAULT_POSITION,
    BOARD_BACKGROUND_COLOR,
    apple_image,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    GRID_SIZE,
    screen,
    snake_body_image,
    snake_head_image,
    snake_tail_image,
    corner_image,
    stone_image,
    LEFT,
    RIGHT,
    UP,
    DOWN,
    COUNT_STONE,
)


def draw_cell(self, screen, position, images):
    """Метод для отрисовки одной ячейки."""
    screen.blit(images, position)
