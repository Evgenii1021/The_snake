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

import pygame as pg

from main_function_game import handle_keys, update_positions
from objects import Apple, Snake, Stone
from settings import SPEED, clock, screen, bg


def main():
    """Основная функция."""
    pg.init()

    snake = Snake()
    stone = Stone(occupied_positions=snake.position)
    apple = Apple(snake.positions + stone.positions)

    while True:
        clock.tick(SPEED)
        screen.blit(bg, (0, 0))

        handle_keys(snake)

        update_positions(snake, apple, stone)
        snake.move()

        apple.draw()
        for position in stone.positions:
            stone.draw(position=position)
        snake.draw()
        pg.display.update()


if __name__ == "__main__":
    main()
