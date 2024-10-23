import pygame as pg
from random import choice, randrange

from settings import (
    DEFAULT_COUNT_TANK,
    DEFAULT_POSITION,
    BOARD_BACKGROUND_COLOR,
    soldier_image,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    GRID_SIZE_SNAKE,
    GRID_SIZE_SOLDIER,
    screen,
    snake_body_image,
    snake_head_image,
    snake_tail_image,
    corner_image,
    tank_image,
    blood_image,
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
        screen.blit(images, position)


class Soldier(GameObject):
    """Класс солдата."""

    def __init__(self, occupied_positions=None, images=soldier_image):
        """Инициализация дочернего класса солдата."""
        super().__init__(images=images)
        if occupied_positions is None:
            occupied_positions = []
        self.randomize_position(occupied_positions)

    def randomize_position(self, occupied_positions):
        """Метод для установки случайного положения солдата."""
        random_positions = (
            randrange(0, SCREEN_WIDTH, GRID_SIZE_SOLDIER),
            randrange(0, SCREEN_HEIGHT, GRID_SIZE_SOLDIER),
        )
        self.position = (
            random_positions
            if random_positions not in occupied_positions
            else self.randomize_position(occupied_positions)
        )

    def draw(self):
        """Метод отрисовки солдата."""
        self.draw_cell(screen, images=self.images, position=self.position)


class Tank(GameObject):
    """Класс танка."""

    def __init__(
        self,
        count_stone=DEFAULT_COUNT_TANK,
        occupied_positions=None,
        images=None,
    ):
        """Инициализация дочернего класса камня."""
        if images is None:
            images = tank_image
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
                randrange(0, SCREEN_WIDTH, 10),
                randrange(0, SCREEN_HEIGHT, 10),
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

        head_x = (head_x + dx * GRID_SIZE_SNAKE) % SCREEN_WIDTH
        head_y = (head_y + dy * GRID_SIZE_SNAKE) % SCREEN_HEIGHT

        new_position = (head_x, head_y)
        self.positions.insert(0, new_position)

        self.last = (
            self.positions.pop()
            if len(self.positions) > self.length
            else self.last
        )

    def rotate(self, images):
        """Метод поворота головы змейки."""
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
            self.draw_tail()

<<<<<<< HEAD
        if len(self.positions) > 1:
=======
        if self.length > 1:
>>>>>>> refs/remotes/origin/version-2.0
            for i in range(1, self.length):
                current_pos = self.positions[i]
                prev_pos = self.positions[i - 1]
                next_pos = (
                    self.last
                    if i + 1 >= len(self.positions)
                    else self.positions[i + 1]
                )

<<<<<<< HEAD
=======
                print(current_pos, prev_pos, next_pos)

>>>>>>> refs/remotes/origin/version-2.0
                segment_image = self.get_segment_image(
                    current_pos, prev_pos, next_pos
                )
                self.draw_cell(screen, current_pos, segment_image)

<<<<<<< HEAD
    def get_segment_image(self, current_pos, prev_pos, next_pos):
        """Возвращает правильное изображение для сегмента тела змеи."""
        if current_pos[0] == prev_pos[0]:
            return self.get_vertical_segment_image(
                current_pos, prev_pos, next_pos
            )
        else:
=======
        # if self.length > 1:
        #     for i in range(1, self.length):
        #         current_pos = self.positions[i]
        #         prev_pos = self.positions[i - 1]
        #         next_pos = (
        #             self.last if i + 1 >= self.length else self.positions[i + 1]
        #         )

        #         if next_pos:
        #             if current_pos[0] == prev_pos[0]:
        #                 if current_pos[1] < prev_pos[1]:
        #                     if next_pos[0] > current_pos[0]:
        #                         segment_image = pg.transform.rotate(
        #                             corner_image, 270
        #                         )
        #                     elif next_pos[0] < current_pos[0]:
        #                         segment_image = pg.transform.rotate(
        #                             corner_image, 180
        #                         )
        #                     else:
        #                         segment_image = self.images
        #                 else:
        #                     if next_pos[0] > current_pos[0]:
        #                         segment_image = pg.transform.rotate(
        #                             corner_image, 0
        #                         )
        #                     elif next_pos[0] < current_pos[0]:
        #                         segment_image = pg.transform.rotate(
        #                             corner_image, 90
        #                         )
        #                     else:
        #                         segment_image = self.images
        #             else:
        #                 if current_pos[0] > prev_pos[0]:
        #                     if next_pos[1] > current_pos[1]:
        #                         segment_image = pg.transform.rotate(
        #                             corner_image, 180
        #                         )
        #                     elif next_pos[1] < current_pos[1]:
        #                         segment_image = pg.transform.rotate(
        #                             corner_image, 90
        #                         )
        #                     else:
        #                         segment_image = self.images
        #                 else:
        #                     if next_pos[1] > current_pos[1]:
        #                         segment_image = pg.transform.rotate(
        #                             corner_image, 270
        #                         )
        #                     elif next_pos[1] < current_pos[1]:
        #                         segment_image = pg.transform.rotate(
        #                             corner_image, 0
        #                         )
        #                     else:
        #                         segment_image = self.images

        #             self.draw_cell(screen, current_pos, segment_image)

    def get_segment_image(self, current_pos, prev_pos, next_pos):
        """Возвращает правильное изображение для сегмента тела змеи."""
        if current_pos[0] == prev_pos[0]:  # Движение по вертикали
            return self.get_vertical_segment_image(
                current_pos, prev_pos, next_pos
            )
        else:  # Движение по горизонтали
>>>>>>> refs/remotes/origin/version-2.0
            return self.get_horizontal_segment_image(
                current_pos, prev_pos, next_pos
            )

<<<<<<< HEAD
    def get_vertical_segment_image(self, current_pos, prev_pos, next_pos):
        """Возвращает изображение для сегмента при вертикальном движении."""
        if next_pos is None:
            return self.images

        if current_pos[1] < prev_pos[1]:
            if next_pos[0] > current_pos[0]:
                return pg.transform.rotate(corner_image, 270)
            elif next_pos[0] < current_pos[0]:
                return pg.transform.rotate(corner_image, 180)
            else:
                return self.images
        else:
            if next_pos[0] > current_pos[0]:
                return pg.transform.rotate(corner_image, 0)
            elif next_pos[0] < current_pos[0]:
                return pg.transform.rotate(corner_image, 90)
            else:
                return self.images

    def get_horizontal_segment_image(self, current_pos, prev_pos, next_pos):
        """Возвращает изображение для сегмента при горизонтальном движении."""
        if current_pos[0] > prev_pos[0]:
            if next_pos[1] > current_pos[1]:
                return pg.transform.rotate(corner_image, 180)
            elif next_pos[1] < current_pos[1]:
                return pg.transform.rotate(corner_image, 90)
            else:
                return self.images
        else:
            if next_pos[1] > current_pos[1]:
                return pg.transform.rotate(corner_image, 270)
            elif next_pos[1] < current_pos[1]:
                return pg.transform.rotate(corner_image, 0)
            else:
=======
    def get_horizontal_segment_image(self, current_pos, prev_pos, next_pos):
        """Возвращает изображение для сегмента при горизонтальном движении."""
        if current_pos[0] > prev_pos[0]:  # Вправо
            if next_pos[1] > current_pos[1]:  # Поворот вниз
                return pg.transform.rotate(corner_image, 180)
            elif next_pos[1] < current_pos[1]:  # Поворот вверх
                return pg.transform.rotate(corner_image, 90)
            else:  # Прямой участок
                return self.images
        else:  # Влево
            if next_pos[1] > current_pos[1]:  # Поворот вниз
                return pg.transform.rotate(corner_image, 270)
            elif next_pos[1] < current_pos[1]:  # Поворот вверх
                return pg.transform.rotate(corner_image, 0)
            else:  # Прямой участок
>>>>>>> refs/remotes/origin/version-2.0
                return self.images

    def draw_tail(self):
        """Метод отрисовки хвоста змейки."""
        if len(self.positions) == 1:
            self.draw_cell(screen, self.last, self.rotate(snake_tail_image))
        else:
            prev_segment_pos = self.positions[-1]
            if self.last[0] == prev_segment_pos[0]:
                if self.last[1] < prev_segment_pos[1]:
                    segment_image = pg.transform.rotate(snake_tail_image, 0)
                else:
                    segment_image = pg.transform.rotate(snake_tail_image, 180)
            else:
                if self.last[0] < prev_segment_pos[0]:
                    segment_image = pg.transform.rotate(snake_tail_image, 90)
                else:
                    segment_image = pg.transform.rotate(snake_tail_image, 270)

            self.draw_cell(screen, self.last, segment_image)

    def reset(self):
        """Метод сброса змейки."""
        self.positions = [self.position]
        self.length = 1
        self.direction = choice([LEFT, RIGHT, UP, DOWN])
        self.last = None
        screen.fill(BOARD_BACKGROUND_COLOR)
