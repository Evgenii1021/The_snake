"""
Модуль, содержащий классы для всех игровых объектов в игре 'Змейка'.

Классы включают базовый класс GameObject и
специфические классы для солдата, танка, крови и змейки.

Классы:

- `GameObject`: базовый класс для всех игровых объектов.
  Содержит методы для отрисовки и установки случайного
  положения объекта на игровом поле.

- `Soldier`: класс, представляющий солдата. Унаследован от
  GameObject. Содержит методы для установки случайного
  положения и отрисовки солдата.

- `Tank`: класс, представляющий танк. Унаследован от
  GameObject. Содержит методы для установки случайного
  положения танка и отрисовки его на экране. Может содержать
  несколько экземпляров, в зависимости от параметра
  count_stone.

- `Blood`: класс, представляющий кровь. Унаследован от
  GameObject. Содержит методы для отрисовки крови на экране.

- `Snake`: класс, представляющий змейку. Унаследован от
  GameObject. Содержит методы для управления движением
  змейки, отрисовки ее частей (головы, тела и хвоста) и
  сброса состояния змейки.

"""

import pygame as pg
from random import choice, randrange

from settings import (
    DEFAULT_COUNT_TANK,
    DEFAULT_POSITION,
    BOARD_BACKGROUND_COLOR,
    SIZE_TANK_HEIGHT,
    SIZE_TANK_WIDTH,
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
    """Базовый класс для всех объектов игры.

    Этот класс реализует общие методы для всех игровых
    объектов, включая отрисовку и установку случайного
    положения.

    Attributes:
        position (tuple): Текущая позиция объекта.
        images: Изображение объекта.
    """

    def __init__(
        self, position=DEFAULT_POSITION, images=BOARD_BACKGROUND_COLOR
    ):
        """Инициализация базового класса.

        Args:
            position (tuple): Начальная позиция объекта.
            images: Изображение для отрисовки объекта.
        """
        self.position = position
        self.images = images

    def draw(self):
        """Метод отрисовки базового класса.

        Raises:
            NotImplementedError: Если метод не переопределен в
            дочернем классе.
        """
        raise NotImplementedError(
            "The draw() method must be"
            f"overridden in a subclass {self.__class__.__name__}."
        )

    def draw_cell(self, screen, position, images):
        """Метод для отрисовки одной ячейки.

        Args:
            screen: Экран, на котором будет отрисована ячейка.
            position (tuple): Позиция, где будет отрисована ячейка.
            images: Изображение, которое будет отрисовано.
        """
        screen.blit(images, position)

    def randomize_position(
        self,
        screen_width,
        screen_height,
        object_width,
        object_height,
        occupied_positions=None,
    ):
        """Метод для установки случайного положения объекта.

        Args:
            screen_width (int): Ширина экрана.
            screen_height (int): Высота экрана.
            object_width (int): Ширина объекта.
            object_height (int): Высота объекта.
            occupied_positions (list): Список уже занятых позиций.

        Returns:
            tuple: Случайная позиция для объекта.
        """
        if occupied_positions is None:
            occupied_positions = []

        while True:
            random_position = (
                randrange(0, screen_width - object_width, object_width),
                randrange(0, screen_height - object_height, object_height),
            )
            if random_position not in occupied_positions:
                return random_position


class Soldier(GameObject):
    """Класс солдата.

    Унаследован от GameObject. Этот класс отвечает за
    создание и отрисовку солдата на игровом поле.

    Attributes:
        position (tuple): Текущая позиция солдата.
        images: Изображение солдата.
    """

    def __init__(self, occupied_positions=None, images=soldier_image):
        """Инициализация дочернего класса солдата.

        Args:
            occupied_positions (list): Позиции, занятые другими
            объектами.
            images: Изображение для отрисовки солдата.
        """
        super().__init__(images=images)
        if occupied_positions is None:
            occupied_positions = []
        self.randomize_positions(occupied_positions)

    def randomize_positions(self, occupied_positions):
        """Метод для установки случайного положения солдата.

        Args:
            occupied_positions (list): Список занятых позиций.
        """
        self.position = self.randomize_position(
            SCREEN_WIDTH,
            SCREEN_HEIGHT,
            GRID_SIZE_SOLDIER,
            GRID_SIZE_SOLDIER,
            occupied_positions,
        )

    def draw(self):
        """Метод отрисовки солдата."""
        self.draw_cell(screen, images=self.images, position=self.position)


class Tank(GameObject):
    """Класс танка.

    Унаследован от GameObject. Этот класс отвечает за
    создание и отрисовку танка на игровом поле.

    Attributes:
        positions (list): Список позиций танков.
        occupied_positions (list): Список занятых позиций.
        count_stone (int): Количество танков.
    """

    def __init__(
        self,
        count_stone=DEFAULT_COUNT_TANK,
        occupied_positions=None,
        images=None,
    ):
        """Инициализация дочернего класса танка.

        Args:
            count_stone (int): Количество танков для создания.
            occupied_positions (list): Позиции, занятые другими
            объектами.
            images: Изображение для отрисовки танка.
        """
        if images is None:
            images = tank_image
        super().__init__(images=images)
        if occupied_positions is None:
            occupied_positions = []
        self.occupied_positions = []
        self.count_stone = count_stone
        self.randomize_positions(occupied_positions)

    def randomize_positions(self, occupied_positions):
        """Метод для установки случайного положения танка.

        Args:
            occupied_positions (list): Список занятых позиций.
        """
        self.positions = []
        self.occupied_positions = []
        for _ in range(self.count_stone):

            self.position = self.randomize_position(
                SCREEN_WIDTH,
                SCREEN_HEIGHT,
                SIZE_TANK_WIDTH,
                SIZE_TANK_HEIGHT,
                occupied_positions + self.occupied_positions,
            )
            self.positions.append(self.position)
            self.occupied_positions.append(self.position)

    def draw(self, position):
        """Метод отрисовки танка.

        Args:
            position (tuple): Позиция для отрисовки танка.
        """
        self.draw_cell(screen, images=self.images, position=position)


class Blood(GameObject):
    """Класс крови.

    Унаследован от GameObject. Этот класс отвечает за
    создание и отрисовку крови на игровом поле.

    Attributes:
        positions (list): Список позиций крови.
    """

    def __init__(
        self,
        images=blood_image,
    ):
        """Инициализация дочернего класса крови.

        Args:
            images: Изображение для отрисовки крови.
        """
        super().__init__(images=images)
        self.positions = []

    def draw(self, position=None):
        """Метод отрисовки крови.

        Args:
            position (tuple): Позиция для отрисовки крови.
        """
        if position is not None:
            self.positions.append(position)
        for posit in self.positions:
            screen.blit(self.images, posit)


class Snake(GameObject):
    """Класс змейки.

    Унаследован от GameObject. Этот класс отвечает за
    управление змейкой, её движением и отрисовкой.

    Attributes:
        positions (list): Список позиций частей змейки.
        length (int): Длина змейки.
        direction (tuple): Текующее направление движения.
        last (tuple): Позиция последнего сегмента.
    """

    def __init__(self, images=snake_body_image):
        """Инициализация дочернего класса змейки.

        Args:
            images: Изображение для отрисовки частей змейки.
        """
        super().__init__(images=images)
        self.reset()

    def update_direction(self, next_direction):
        """Метод обновления направления движения змейки.

        Args:
            next_direction (tuple): Новое направление движения.
        """
        self.direction = next_direction

    def get_head_position(self):
        """Метод получения положения головы змейки.

        Returns:
            tuple: Позиция головы змейки.
        """
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
        """Метод поворота головы змейки.

        Args:
            images: Изображение головы змейки.

        Returns:
            Surface: Повернутое изображение головы.
        """
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

        if len(self.positions) > 1:
            for i in range(1, self.length):
                current_pos = self.positions[i]
                prev_pos = self.positions[i - 1]
                next_pos = (
                    self.last
                    if i + 1 >= len(self.positions)
                    else self.positions[i + 1]
                )

                segment_image = self.get_segment_image(
                    current_pos, prev_pos, next_pos
                )
                self.draw_cell(screen, current_pos, segment_image)

    def get_segment_image(self, current_pos, prev_pos, next_pos):
        """Возвращает правильное изображение для сегмента тела змеи.

        Args:
            current_pos (tuple): Текущая позиция сегмента.
            prev_pos (tuple): Позиция предыдущего сегмента.
            next_pos (tuple): Позиция следующего сегмента.

        Returns:
            Surface: Изображение сегмента.
        """
        if current_pos[0] == prev_pos[0]:
            return self.get_vertical_segment_image(
                current_pos, prev_pos, next_pos
            )
        else:
            return self.get_horizontal_segment_image(
                current_pos, prev_pos, next_pos
            )

    def get_vertical_segment_image(self, current_pos, prev_pos, next_pos):
        """Возвращает изображение для сегмента при вертикальном движении.

        Args:
            current_pos (tuple): Текущая позиция сегмента.
            prev_pos (tuple): Позиция предыдущего сегмента.
            next_pos (tuple): Позиция следующего сегмента.

        Returns:
            Surface: Изображение сегмента.
        """
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
        """Возвращает изображение для сегмента при горизонтальном движении.

        Args:
            current_pos (tuple): Текущая позиция сегмента.
            prev_pos (tuple): Позиция предыдущего сегмента.
            next_pos (tuple): Позиция следующего сегмента.

        Returns:
            Surface: Изображение сегмента.
        """
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
