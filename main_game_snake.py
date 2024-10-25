"""
Модуль для реализации основной логики игры 'Змейка'.

Содержит функцию `main`, которая инициализирует игру и управляет
основным игровым циклом, включая движение змейки, танков и солдат,
обработку событий и отрисовку объектов.

Основные компоненты:
- `Snake`, `Tank`, `Soldier`, `Blood`: классы, представляющие
  игровые объекты.
- `MainGameMenu`: класс для отображения основного игрового меню.
- `handle_keys_main`: функция для обработки нажатий клавиш
  и взаимодействия с меню.
- `update_positions`: функция для обновления позиций объектов на экране.

Параметры функции `main`:
- `speed`: скорость игры, определяющая частоту обновления кадров.
- `count_stone`: количество танков на поле.

Логика игры:
1. Инициализация Pygame и создание игровых объектов.
2. Основной игровой цикл, который:
   - Обновляет экран с заданной скоростью.
   - Обрабатывает события клавиатуры.
   - Обновляет позиции змейки, солдата и танков.
   - Отрисовывает все игровые объекты на экране.
   - Проверяет условия окончания игры и возвращает в меню, если нужно.
"""

import pygame as pg

from objects import MainGameMenu
from main_function_game import handle_keys_main, update_positions
from objects import Soldier, Snake, Tank, Blood
from settings import (
    clock,
    screen,
    bg,
)


def main(speed, count_stone):
    """Основная функция."""
    pg.init()

    snake = Snake()
    tank = Tank(count_stone=count_stone, occupied_positions=snake.positions)
    soldier = Soldier(snake.positions + tank.positions)
    blood = Blood()
    main_game_menu = MainGameMenu()

    while True:
        clock.tick(speed)
        screen.blit(bg, (0, 0))
        mouse_pos = pg.mouse.get_pos()

        draw_rect = main_game_menu.draw(mouse_pos)

        result = handle_keys_main(snake, draw_rect, mouse_pos)

        if result is False:
            return

        update_positions(snake, soldier, tank, blood)

        snake.move()
        soldier.draw()
        blood.draw()

        for position in tank.positions:
            tank.draw(position=position)
        snake.draw()
        pg.display.update()
