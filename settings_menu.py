import pygame as pg
import sys

from objects import SettingsMenu
from main_game_snake import main
from settings import (
    screen,
    bg,
    EASY_SETTINGS,
    MEDIUM_SETTINGS,
    HARD_SETTINGS,
)


def settings_menu():
    """Меню настроек."""
    settings_menu = SettingsMenu()
    while True:
        screen.blit(bg, (0, 0))

        mouse_pos = pg.mouse.get_pos()

        draw_rect = settings_menu.draw(mouse_pos)

        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                if draw_rect[0].collidepoint(mouse_pos):
                    main(EASY_SETTINGS["SPEED"], EASY_SETTINGS["COUNT_STONE"])
                elif draw_rect[1].collidepoint(mouse_pos):
                    main(
                        MEDIUM_SETTINGS["SPEED"],
                        MEDIUM_SETTINGS["COUNT_STONE"],
                    )
                elif draw_rect[2].collidepoint(mouse_pos):
                    main(HARD_SETTINGS["SPEED"], HARD_SETTINGS["COUNT_STONE"])
                elif draw_rect[3].collidepoint(mouse_pos):
                    return
