import pygame as pg
import sys

from settings import DOWN, LEFT, RIGHT, UP


def update_positions(game_object1, game_object2, game_object3, game_object4):
    """Функция обновления позиций змейки."""
    head_x, head_y = game_object1.get_head_position()
    soldier_x, soldier_y = game_object2.position
    if all(
        [
            soldier_x <= head_x <= soldier_x + 20,
            soldier_y <= head_y <= soldier_y + 20,
        ]
    ):
        game_object4.draw(game_object2.position)
        game_object2.randomize_position(
            occupied_positions=game_object1.positions + game_object3.positions
        )
        game_object1.length += 1
    elif any(
        [
            game_object1.get_head_position() in game_object1.positions[4:],
            any(
                all(
                    [
                        tank_x <= head_x <= tank_x + 60,
                        tank_y <= head_y <= tank_y + 30,
                    ]
                )
                for tank_x, tank_y in game_object3.positions
            ),
        ]
    ):
        game_object3.randomize_position(
            occupied_positions=game_object1.positions
        )
        game_object4.positions = []
        game_object1.reset()


def handle_quit_event(event):
    """Функция обработки события выхода из игры."""
    if event.type == pg.QUIT:
        pg.quit()
        sys.exit()


def handle_keydown_event(event, game_object):
    """Функция обработки нажатия клавиш для управления змейкой."""
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


def handle_mousebuttondown_event(event, menu_rect, mouse_pos):
    """Функция обработки нажатия мыши для взаимодействия с меню."""
    if event.type == pg.MOUSEBUTTONDOWN and menu_rect.collidepoint(mouse_pos):
        return False
    return True


def handle_keys_main(game_object, menu_rect, mouse_pos):
    """Функция обработки нажатий клавиш."""
    for event in pg.event.get():
        handle_quit_event(event)

        if event.type == pg.KEYDOWN:
            handle_keydown_event(event, game_object)

        if not handle_mousebuttondown_event(event, menu_rect, mouse_pos):
            return False

    return True
