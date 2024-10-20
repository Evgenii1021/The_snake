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

from main_function_game import update_positions
from objects import Apple, Snake, Stone, Blood
from settings import (
    DOWN,
    LEFT,
    RIGHT,
    SPEED,
    UP,
    clock,
    screen,
    bg,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    COUNT_STONE,
    settings_image,
    play_image,
    exit_image,
    play_image_hover,
    settings_image_hover,
    exit_image_hover,
    settings_image_all,
    easy_image,
    easy_image_hover,
    middle_image,
    middle_image_hover,
    hard_image,
    hard_image_hover,
    back_image,
    back_image_hover,
    menu_image,
    menu_image_hover,
)


def main_menu():
    """Главное меню игры."""
    while True:
        screen.blit(bg, (0, 0))

        mouse_pos = pg.mouse.get_pos()

        play_rect = screen.blit(
            play_image,
            (SCREEN_WIDTH // 2 - (154 / 2), SCREEN_HEIGHT // 2 - 110),
        )

        settings_rect = screen.blit(
            settings_image,
            (SCREEN_WIDTH // 2 - (154 / 2), SCREEN_HEIGHT // 2 - 40),
        )

        exit_rect = screen.blit(
            exit_image,
            (SCREEN_WIDTH // 2 - (154 / 2), SCREEN_HEIGHT // 2 + 30),
        )

        if play_rect.collidepoint(mouse_pos):
            screen.blit(
                play_image_hover,
                (SCREEN_WIDTH // 2 - (154 / 2), SCREEN_HEIGHT // 2 - 110),
            )
        elif settings_rect.collidepoint(mouse_pos):
            screen.blit(
                settings_image_hover,
                (SCREEN_WIDTH // 2 - (154 / 2), SCREEN_HEIGHT // 2 - 40),
            )
        elif exit_rect.collidepoint(mouse_pos):
            screen.blit(
                exit_image_hover,
                (SCREEN_WIDTH // 2 - (154 / 2), SCREEN_HEIGHT // 2 + 30),
            )

        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                if play_rect.collidepoint(mouse_pos):
                    main()
                elif settings_rect.collidepoint(mouse_pos):
                    settings_menu()
                elif exit_rect.collidepoint(mouse_pos):
                    pg.quit()
                    sys.exit()


def settings_menu():
    """Меню настроек."""
    while True:
        screen.blit(bg, (0, 0))

        mouse_pos = pg.mouse.get_pos()

        screen.blit(
            settings_image_all,
            (SCREEN_WIDTH // 2 - (193 / 2), SCREEN_HEIGHT // 5 - 60),
        )

        easy_rect = screen.blit(
            easy_image,
            (SCREEN_WIDTH // 2 - (154 / 2), SCREEN_HEIGHT // 2 - 90),
        )

        middle_rect = screen.blit(
            middle_image,
            (SCREEN_WIDTH // 2 - (154 / 2), SCREEN_HEIGHT // 2 - 20),
        )
        hard_rect = screen.blit(
            hard_image,
            (SCREEN_WIDTH // 2 - (154 / 2), SCREEN_HEIGHT // 2 + 50),
        )

        back_rect = screen.blit(
            back_image,
            (SCREEN_WIDTH // 2 - (154 / 2), SCREEN_HEIGHT // 2 + 140),
        )

        if easy_rect.collidepoint(mouse_pos):
            screen.blit(
                easy_image_hover,
                (SCREEN_WIDTH // 2 - (154 / 2), SCREEN_HEIGHT // 2 - 90),
            )
        elif middle_rect.collidepoint(mouse_pos):
            screen.blit(
                middle_image_hover,
                (SCREEN_WIDTH // 2 - (154 / 2), SCREEN_HEIGHT // 2 - 20),
            )
        elif hard_rect.collidepoint(mouse_pos):
            screen.blit(
                hard_image_hover,
                (SCREEN_WIDTH // 2 - (154 / 2), SCREEN_HEIGHT // 2 + 50),
            )
        elif back_rect.collidepoint(mouse_pos):
            screen.blit(
                back_image_hover,
                (SCREEN_WIDTH // 2 - (154 / 2), SCREEN_HEIGHT // 2 + 140),
            )
        global SPEED
        global COUNT_STONE

        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                if easy_rect.collidepoint(mouse_pos):
                    SPEED = 15
                    COUNT_STONE = 2
                elif middle_rect.collidepoint(mouse_pos):
                    SPEED = 20
                    COUNT_STONE = 3
                elif hard_rect.collidepoint(mouse_pos):
                    SPEED = 25
                    COUNT_STONE = 4
                elif back_rect.collidepoint(mouse_pos):
                    main_menu()


def handle_keys_main(game_object, menu_rect, mouse_pos):
    """Функция обработки нажатий клавиш."""

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_UP and game_object.direction != DOWN:
                game_object.update_direction(UP)
            elif event.key == pg.K_DOWN and game_object.direction != UP:
                game_object.update_direction(DOWN)
            elif event.key == pg.K_LEFT and game_object.direction != RIGHT:
                game_object.update_direction(LEFT)
            elif event.key == pg.K_RIGHT and game_object.direction != LEFT:
                game_object.update_direction(RIGHT)
            elif event.key == pg.K_ESCAPE:
                pg.quit()
                sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            if menu_rect.collidepoint(mouse_pos):
                main_menu()


def main():
    """Основная функция."""
    snake = Snake()
    stone = Stone(occupied_positions=snake.position)
    apple = Apple(snake.positions + stone.positions)
    blood = Blood()

    while True:
        clock.tick(SPEED)
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

        handle_keys_main(snake, menu_rect, mouse_pos)

        update_positions(snake, apple, stone, blood)

        snake.move()
        apple.draw()
        blood.draw()

        for position in stone.positions:
            stone.draw(position=position)
        snake.draw()
        pg.display.update()


if __name__ == "__main__":
    main_menu()
