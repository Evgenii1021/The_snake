import pygame as pg
import sys

from settings import DOWN, LEFT, RIGHT, UP


def update_positions(game_object1, game_object2, game_object3, game_object4):
    """Функция обновления позиций змейки."""
    if game_object2.position in game_object1.positions:
        game_object4.draw(game_object2.position)
        game_object2.randomize_position(
            occupied_positions=game_object1.positions
        )
        game_object1.length += 1
    elif any(
        [
            game_object1.get_head_position() in game_object1.positions[4:],
            game_object1.get_head_position() in game_object3.positions,
        ]
    ):
        game_object3.randomize_position(
            occupied_positions=game_object1.positions
        )
        game_object1.reset()


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
                return False
