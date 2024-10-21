import pygame as pg
import sys

from main_function_game import handle_keys_main, update_positions
from objects import Soldier, Snake, Stone, Blood
from settings import (
    clock,
    screen,
    bg,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    menu_image,
    menu_image_hover,
)


def main(speed, count_stone):
    """Основная функция."""
    pg.init()

    snake = Snake()
    stone = Stone(count_stone=count_stone, occupied_positions=snake.position)
    soldier = Soldier(snake.positions + stone.positions)
    blood = Blood()

    while True:
        clock.tick(speed)
        screen.blit(bg, (0, 0))
        mouse_pos = pg.mouse.get_pos()

        menu_rect = screen.blit(
            menu_image,
            (SCREEN_WIDTH - 76, SCREEN_HEIGHT - 32),
        )
        if menu_rect.collidepoint(mouse_pos):
            screen.blit(
                menu_image_hover,
                (SCREEN_WIDTH - 76, SCREEN_HEIGHT - 32),
            )

        result = handle_keys_main(snake, menu_rect, mouse_pos)

        if result is False:
            return

        update_positions(snake, soldier, stone, blood)

        snake.move()
        soldier.draw()
        blood.draw()

        for position in stone.positions:
            stone.draw(position=position)
        snake.draw()
        pg.display.update()
