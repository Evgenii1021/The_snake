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
    LEFT,
    RIGHT,
    UP,
    DOWN,
)


class GameObject:
    """Базовый класс для всех объектов игры."""

    def __init__(
        self, position=DEFAULT_POSITION, images=BOARD_BACKGROUND_COLOR
    ):
        """Инициализация базового класса."""
        self.position = position
        self.images = images

    def draw(self):
        """Метод отрисовки базового класса."""
        raise NotImplementedError(
            "The draw() method must be"
            f"overridden in a subclass {self.__class__.__name__}."
        )

    def draw_cell(self, screen, position, images):
        """Метод для отрисовки одной ячейки."""
        # rect = pg.Rect(position, (GRID_SIZE, GRID_SIZE))
        # pg.draw.rect(screen, body_color, rect)
        # pg.draw.rect(screen, border_color, rect, 1)
        screen.blit(images, position)


class Apple(GameObject):
    """Класса яблока."""

    def __init__(self, occupied_positions=None, images=apple_image):
        """Инициализация дочернего класса яблока."""
        super().__init__(images=images)
        if occupied_positions is None:
            occupied_positions = []
        self.randomize_position(occupied_positions)

    def randomize_position(self, occupied_positions):
        """Метод для установки случайного положения яблока."""
        random_positions = (
            randrange(0, SCREEN_WIDTH, GRID_SIZE),
            randrange(0, SCREEN_HEIGHT, GRID_SIZE),
        )
        self.position = (
            random_positions
            if random_positions not in occupied_positions
            else self.randomize_position(occupied_positions)
        )

    def draw(self):
        """Метод отрисовки яблока."""
        self.draw_cell(screen, images=self.images, position=self.position)


class Snake(GameObject):
    """Класс змейки."""

    def __init__(self, images=snake_body_image):
        """Инициализация дочернего класса змейки."""
        super().__init__(images=images)
        self.reset()

    def update_direction(self, next_direction):
        """Метод обновления направления движения змейки."""
        self.direction = next_direction

    def get_head_position(self):
        """Метод получения положения головы змейки."""
        return self.positions[0]

    def move(self):
        """Метод движения змейки."""
        head_x, head_y = self.get_head_position()

        dx, dy = self.direction

        head_x = (head_x + dx * GRID_SIZE) % SCREEN_WIDTH
        head_y = (head_y + dy * GRID_SIZE) % SCREEN_HEIGHT

        new_position = (head_x, head_y)
        self.positions.insert(0, new_position)

        self.last = (
            self.positions.pop() if len(self.positions) > self.length else None
        )

    def draw(self):
        """Метод отрисовки змейки."""
        self.draw_cell(screen, self.get_head_position(), snake_head_image)

        if self.last:
            transparent_surface = pg.Surface((GRID_SIZE, GRID_SIZE))
            transparent_surface.set_alpha(0)
            screen.blit(transparent_surface, self.last)

        if self.length >= 2:
            for position in self.positions[1:]:
                self.draw_cell(screen, position, self.images)

    def reset(self):
        """Метод сброса змейки."""
        self.positions = [self.position]
        self.length = 1
        self.direction = choice([LEFT, RIGHT, UP, DOWN])
        self.last = None
        screen.fill(BOARD_BACKGROUND_COLOR)
