"""
Модуль для реализации игры 'Змейка'.

Использует библиотеку Pygame для графического отображения.

Основные компоненты:
- main_menu: функция для отображения главного меню с выбором
  режима игры, настройками и возможностью выхода.
- handle_quit_event: функция для обработки выхода из игры.
- main: основной игровой процесс, который инициализирует игровой
  цикл с установленной скоростью и количеством препятствий.
- settings_menu: меню настроек для изменения параметров игры.

Константы:
- DEFAULT_COUNT_TANK: стандартное количество препятствий на поле.
- DEFAULT_SPEED: стандартная скорость игры.
- screen: основное окно отображения игры.
- bg: фоновое изображение для главного меню.
"""

import pygame as pg
import sys

from objects import MainMenu
from main_function_game import handle_quit_event
from main_game_snake import main
from settings_menu import settings_menu
from settings import (
    DEFAULT_COUNT_TANK,
    DEFAULT_SPEED,
    screen,
    bg,
)


def main_menu():
    """Главное меню игры."""
    main_menu = MainMenu()

    while True:
        screen.blit(bg, (0, 0))

        mouse_pos = pg.mouse.get_pos()

        draw_rect = main_menu.draw(mouse_pos)

        pg.display.update()
        for event in pg.event.get():
            handle_quit_event(event)

            if event.type == pg.MOUSEBUTTONDOWN:
                if draw_rect[0].collidepoint(mouse_pos):
                    speed = DEFAULT_SPEED
                    count_stone = DEFAULT_COUNT_TANK
                    main(speed, count_stone)
                elif draw_rect[1].collidepoint(mouse_pos):
                    settings_menu()
                elif draw_rect[2].collidepoint(mouse_pos):
                    pg.quit()
                    sys.exit()


if __name__ == "__main__":
    main_menu()
