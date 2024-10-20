import sys

import pygame as pg

from settings import (
    SPEED,
    clock,
    screen,
    bg,
    BLACK,
    GREEN,
    SOFT_CYAN,
    RED,
    font,
    WHITE,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    HOVER_COLOR,
    COUNT_STONE,
    UP,
    DOWN,
    LEFT,
    RIGHT,
    blood_image,
)


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
