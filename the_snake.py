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
import sys

from draw_button import draw_main_menu
from main_game_snake import main
from settings_menu import settings_menu
from settings import (
    DEFAULT_COUNT_STONE,
    DEFAULT_SPEED,
    screen,
    bg,
)


def main_menu():
    """Главное меню игры."""
    while True:
        screen.blit(bg, (0, 0))

        mouse_pos = pg.mouse.get_pos()

        draw_rect = draw_main_menu(mouse_pos)

        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                if draw_rect[0].collidepoint(mouse_pos):
                    speed = DEFAULT_SPEED
                    count_stone = DEFAULT_COUNT_STONE
                    main(speed, count_stone)
                elif draw_rect[1].collidepoint(mouse_pos):
                    settings_menu()
                elif draw_rect[2].collidepoint(mouse_pos):
                    pg.quit()
                    sys.exit()


if __name__ == "__main__":
    main_menu()
