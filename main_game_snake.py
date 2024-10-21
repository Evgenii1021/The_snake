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
    tank = Tank(count_stone=count_stone, occupied_positions=snake.position)
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
