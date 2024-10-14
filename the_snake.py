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

    def __init__(self, position=DEFAULT_POSITION, body_color=BOARD_BACKGROUND_COLOR):
        """Инициализация базового класса."""
        self.position = position
        self.body_color = body_color

    def draw(self):
        """Метод отрисовки базового класса."""
        raise NotImplementedError("The draw() method must be overridden in a subclass.")


class Apple(GameObject):
    """Класса яблока."""

    def __init__(self):
        """Инициализация дочернего класса яблока."""
        super().__init__()
        self.body_color = APPLE_COLOR
        self.randomize_position()

    def randomize_position(self):
        """Метод для установки случайного положения яблока."""
        self.position = (
            randrange(0, SCREEN_WIDTH, GRID_SIZE),
            randrange(0, SCREEN_HEIGHT, GRID_SIZE),
        )

    def draw(self):
        """Метод отрисовки яблока."""
        rect = pg.Rect(self.position, (GRID_SIZE, GRID_SIZE))
        pg.draw.rect(screen, self.body_color, rect)
        pg.draw.rect(screen, BORDER_COLOR, rect, 1)


class Snake(GameObject):
    """Класс змейки."""

    def __init__(self):
        """Инициализация дочернего класса змейки."""
        super().__init__()
        self.positions = [
            self.position,
        ]
        self.body_color = SNAKE_COLOR
        self.length = 1
        self.direction = RIGHT
        self.next_direction = None
        self.last = None

    def update_direction(self):
        """Метод обновления направления движения змейки."""
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None

    def get_head_position(self):
        """Метод получения положения головы змейки."""
        return self.positions[0]

    def move(self):
        """Метод движения змейки."""
        head_x, head_y = self.get_head_position()

        self.positions.insert(0, self.positions[0])

        if self.direction == RIGHT:
            self.positions[0] = (head_x + GRID_SIZE, head_y)
        elif self.direction == LEFT:
            self.positions[0] = (head_x - GRID_SIZE, head_y)
        elif self.direction == UP:
            self.positions[0] = (head_x, head_y - GRID_SIZE)
        elif self.direction == DOWN:
            self.positions[0] = (head_x, head_y + GRID_SIZE)

        if self.positions[0][0] >= SCREEN_WIDTH:
            self.positions[0] = (0, self.positions[0][1])
        elif self.positions[0][0] < 0:
            self.positions[0] = (SCREEN_WIDTH - GRID_SIZE, self.positions[0][1])
        elif self.positions[0][1] < 0:
            self.positions[0] = (self.positions[0][0], SCREEN_HEIGHT - GRID_SIZE)
        elif self.positions[0][1] >= SCREEN_HEIGHT:
            self.positions[0] = (self.positions[0][0], 0)

        if len(self.positions) > self.length + 1:
            self.positions.pop()

    def draw(self):
        """Метод отрисовки змейки."""
        for position in self.positions[:-1]:
            rect = pg.Rect(position, (GRID_SIZE, GRID_SIZE))
            pg.draw.rect(screen, self.body_color, rect)
            pg.draw.rect(screen, BORDER_COLOR, rect, 1)

        head_rect = pg.Rect(self.positions[0], (GRID_SIZE, GRID_SIZE))
        pg.draw.rect(screen, self.body_color, head_rect)
        pg.draw.rect(screen, BORDER_COLOR, head_rect, 1)

        if self.last:
            last_rect = pg.Rect(self.last, (GRID_SIZE, GRID_SIZE))
            pg.draw.rect(screen, BOARD_BACKGROUND_COLOR, last_rect)

    def reset(self):
        """Метод сброса змейки."""
        self.positions = [self.position]
        self.length = 1
        self.direction = choice([LEFT, RIGHT, UP, DOWN])


def handle_keys(game_object):
    """Функция обработки нажатий клавиш."""
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            raise SystemExit
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_UP and game_object.direction != DOWN:
                game_object.next_direction = UP
            elif event.key == pg.K_DOWN and game_object.direction != UP:
                game_object.next_direction = DOWN
            elif event.key == pg.K_LEFT and game_object.direction != RIGHT:
                game_object.next_direction = LEFT
            elif event.key == pg.K_RIGHT and game_object.direction != LEFT:
                game_object.next_direction = RIGHT


def main():
    """Основная функция."""
    pg.init()

    snake = Snake()
    apple = Apple()

    while True:
        clock.tick(SPEED)

        handle_keys(snake)
        snake.update_direction()
        snake.move()
        if apple.position in snake.positions:
            apple.randomize_position()
            snake.length += 1

        if snake.positions[0] in snake.positions[1:]:
            snake.reset()

        snake.draw()
        apple.draw()
        pg.display.update()
        screen.fill(BOARD_BACKGROUND_COLOR)


if __name__ == "__main__":
    main()
