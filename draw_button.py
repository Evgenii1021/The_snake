from settings import (
    screen,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
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
)


def draw_main_menu(mouse_pos):
    """Функция отрисовки кнопок основного меню."""
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
    return play_rect, settings_rect, exit_rect


def draw_settings_menu(mouse_pos):
    """Функция отрисовки кнопок меню настройки."""
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
    return easy_rect, middle_rect, hard_rect, back_rect
