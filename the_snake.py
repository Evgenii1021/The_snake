"""
Модуль для реализации классической игры 'Змейка'.

Включает в себя:
- Базовый класс GameObject объектов игры.
- Дочерний класс Snake для управления движением и состоянием змейки.
- Дочерний класс Apple для создания яблока и управления его положением
  на игровом поле.
- Основной цикл игры с обработкой событий, отрисовкой объектов и
  логикой столкновений.

Использует библиотеку Pygame для графического отображения.
"""

from random import choice, randrange
import sys

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

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
SOFT_CYAN = (93, 216, 228)

BOARD_BACKGROUND_COLOR = BLACK
BORDER_COLOR = SOFT_CYAN
APPLE_COLOR = RED
SNAKE_COLOR = GREEN

SPEED = 20

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

pg.display.set_caption("Змейка")

clock = pg.time.Clock()


class GameObject:
    """Базовый класс для всех объектов игры."""

    def __init__(
        self, position=DEFAULT_POSITION, body_color=BOARD_BACKGROUND_COLOR
    ):
        """Инициализация базового класса."""
        self.position = position
        self.body_color = body_color

    def draw(self):
        """Метод отрисовки базового класса."""
        raise NotImplementedError(
            f"The draw() method must be"
            f"overridden in a subclass {self.__class__.__name__}."
        )

    def draw_cell(
        self, screen, position, body_color, border_color=BORDER_COLOR
    ):
        """Метод для отрисовки одной ячейки."""
        rect = pg.Rect(position, (GRID_SIZE, GRID_SIZE))
        pg.draw.rect(screen, body_color, rect)
        pg.draw.rect(screen, border_color, rect, 1)


class Apple(GameObject):
    """Класса яблока."""

    def __init__(self, occupied_positions, body_color=APPLE_COLOR):
        """Инициализация дочернего класса яблока."""
        super().__init__(body_color=body_color)
        self.occupied_positions = occupied_positions
        self.randomize_position(occupied_positions=self.occupied_positions)

    def randomize_position(self, occupied_positions):
        """Метод для установки случайного положения яблока."""
        random_positions = (
            randrange(0, SCREEN_WIDTH, GRID_SIZE),
            randrange(0, SCREEN_HEIGHT, GRID_SIZE),
        )
        self.position = (
            random_positions
            if random_positions not in occupied_positions
            else self.randomize_position(self.occupied_positions)
        )

    def draw(self):
        """Метод отрисовки яблока."""
        self.draw_cell(screen, self.position, APPLE_COLOR)


class Snake(GameObject):
    """Класс змейки."""

    def __init__(self, body_color=SNAKE_COLOR):
        """Инициализация дочернего класса змейки."""
        super().__init__(body_color=body_color)
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
        self.draw_cell(screen, self.get_head_position(), SNAKE_COLOR)

        if self.last:
            self.draw_cell(
                screen,
                self.last,
                BOARD_BACKGROUND_COLOR,
                BOARD_BACKGROUND_COLOR,
            )

    def reset(self):
        """Метод сброса змейки."""
        self.positions = [self.position]
        self.length = 1
        self.direction = choice([LEFT, RIGHT, UP, DOWN])
        self.last = None
        screen.fill(BOARD_BACKGROUND_COLOR)


def handle_keys(game_object):
    """Функция обработки нажатий клавиш."""
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_UP and game_object.direction != DOWN:
                game_object.update_direction(UP)
            elif event.key == pg.K_DOWN and game_object.direction != UP:
                game_object.update_direction(DOWN)
            elif event.key == pg.K_LEFT and game_object.direction != RIGHT:
                game_object.update_direction(LEFT)
            elif event.key == pg.K_RIGHT and game_object.direction != LEFT:
                game_object.update_direction(RIGHT)
            elif event.key == pg.K_ESCAPE:
                pg.quit()
                sys.exit()


def update_positions(game_object1, game_object2):
    """Функция обновления позиций змейки."""
    if game_object2.position in game_object1.positions:
        game_object2.randomize_position(
            occupied_positions=game_object1.positions
        )
        game_object1.length += 1
    elif game_object1.get_head_position() in game_object1.positions[4:]:
        game_object1.reset()


def main():
    """Основная функция."""
    pg.init()

    snake = Snake()
    apple = Apple(snake.positions)

    while True:
        clock.tick(SPEED)

        handle_keys(snake)
        snake.move()

        update_positions(snake, apple)

        snake.draw()
        apple.draw()
        pg.display.update()


if __name__ == "__main__":
    main()
