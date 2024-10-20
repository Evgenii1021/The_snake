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
    blood_image,
    LEFT,
    RIGHT,
    UP,
    DOWN,
    COUNT_STONE,
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
        screen.blit(images, position)


class Apple(GameObject):
    """Класс яблока."""

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


class Stone(GameObject):
    """Класс камня."""

    def __init__(
        self,
        count_stone=COUNT_STONE,
        occupied_positions=None,
        images=stone_image,
    ):
        """Инициализация дочернего класса камня."""
        super().__init__(images=images)
        self.positions = []
        if occupied_positions is None:
            occupied_positions = []
        self.count_stone = count_stone
        self.randomize_position(occupied_positions)

    def randomize_position(self, occupied_positions):
        """Метод для установки случайного положения камня."""
        self.positions = []
        for _ in range(self.count_stone):
            random_positions = (
                randrange(0, SCREEN_WIDTH, GRID_SIZE),
                randrange(0, SCREEN_HEIGHT, GRID_SIZE),
            )
            self.position = (
                random_positions
                if random_positions not in occupied_positions
                else self.randomize_position(occupied_positions)
            )
            self.positions.append(self.position)

    def draw(self, position):
        """Метод отрисовки камня."""
        self.draw_cell(screen, images=self.images, position=position)


class Blood(GameObject):
    """Класс крови."""

    def __init__(
        self,
        images=blood_image,
    ):
        """Инициализация дочернего класса крови."""
        super().__init__(images=images)
        self.positions = []

    def draw(self, position=None):
        """Метод отрисовки крови."""
        if position is not None:
            self.positions.append(position)
        for posit in self.positions:
            screen.blit(self.images, posit)


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

    def rotate(self, images):
        """Метод поворота головы и хвоста змейки."""
        if self.direction == UP:
            rotated_image_head = pg.transform.rotate(images, 180)
        elif self.direction == DOWN:
            rotated_image_head = images
        elif self.direction == LEFT:
            rotated_image_head = pg.transform.rotate(images, 270)
        elif self.direction == RIGHT:
            rotated_image_head = pg.transform.rotate(images, 90)

        return rotated_image_head

    def draw(self):
        """Метод отрисовки змейки."""
        self.draw_cell(
            screen, self.get_head_position(), self.rotate(snake_head_image)
        )

        if self.last:
            self.draw_cell(screen, self.last, self.rotate(snake_tail_image))

        if self.length > 1:
            for i in range(1, self.length):
                current_pos = self.positions[i]
                prev_pos = self.positions[i - 1]
                next_pos = (
                    self.last if i + 1 >= self.length else self.positions[i + 1]
                )

                if next_pos:
                    if current_pos[0] == prev_pos[0]:
                        if current_pos[1] < prev_pos[1]:
                            if next_pos[0] > current_pos[0]:
                                segment_image = pg.transform.rotate(
                                    corner_image, 270
                                )
                            elif next_pos[0] < current_pos[0]:
                                segment_image = pg.transform.rotate(
                                    corner_image, 180
                                )
                            else:
                                segment_image = self.images
                        else:
                            if next_pos[0] > current_pos[0]:
                                segment_image = pg.transform.rotate(
                                    corner_image, 0
                                )
                            elif next_pos[0] < current_pos[0]:
                                segment_image = pg.transform.rotate(
                                    corner_image, 90
                                )
                            else:
                                segment_image = self.images
                    else:
                        if current_pos[0] > prev_pos[0]:
                            if next_pos[1] > current_pos[1]:
                                segment_image = pg.transform.rotate(
                                    corner_image, 180
                                )
                            elif next_pos[1] < current_pos[1]:
                                segment_image = pg.transform.rotate(
                                    corner_image, 90
                                )
                            else:
                                segment_image = self.images
                        else:
                            if next_pos[1] > current_pos[1]:
                                segment_image = pg.transform.rotate(
                                    corner_image, 270
                                )
                            elif next_pos[1] < current_pos[1]:
                                segment_image = pg.transform.rotate(
                                    corner_image, 0
                                )
                            else:
                                segment_image = self.images

                    self.draw_cell(screen, current_pos, segment_image)

    def reset(self):
        """Метод сброса змейки."""
        self.positions = [self.position]
        self.length = 1
        self.direction = choice([LEFT, RIGHT, UP, DOWN])
        self.last = None
        screen.fill(BOARD_BACKGROUND_COLOR)
