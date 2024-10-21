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
    menu_image,
    menu_image_hover,
)


class Button:
    """Класс для создания кнопок меню."""

    def __init__(self, image, hover_image, position):
        """Инициализация кнопки."""
        self.image = image
        self.hover_image = hover_image
        self.position = position
        self.rect = self.image.get_rect(topleft=position)

    def draw(self, mouse_pos):
        """Отрисовка кнопки и проверка наведения курсора."""
        if self.rect.collidepoint(mouse_pos):
            screen.blit(self.hover_image, self.position)
        else:
            screen.blit(self.image, self.position)

    def get_rect(self):
        """Возвращает прямоугольник кнопки."""
        return self.rect


class MainMenu:
    """Класс для основного меню игры."""

    def __init__(self):
        """Инициализация основного меню и кнопок."""
        self.play_button = Button(
            play_image,
            play_image_hover,
            (SCREEN_WIDTH // 2 - (154 / 2), SCREEN_HEIGHT // 2 - 110),
        )
        self.settings_button = Button(
            settings_image,
            settings_image_hover,
            (SCREEN_WIDTH // 2 - (154 / 2), SCREEN_HEIGHT // 2 - 40),
        )
        self.exit_button = Button(
            exit_image,
            exit_image_hover,
            (SCREEN_WIDTH // 2 - (154 / 2), SCREEN_HEIGHT // 2 + 30),
        )

    def draw(self, mouse_pos):
        """Отрисовка кнопок основного меню и возврат их прямоугольников."""
        self.play_button.draw(mouse_pos)
        self.settings_button.draw(mouse_pos)
        self.exit_button.draw(mouse_pos)

        return (
            self.play_button.get_rect(),
            self.settings_button.get_rect(),
            self.exit_button.get_rect(),
        )


class SettingsMenu:
    """Класс для меню настроек игры."""

    def __init__(self):
        """Инициализация меню настроек и кнопок."""
        self.settings_image = settings_image_all
        self.easy_button = Button(
            easy_image,
            easy_image_hover,
            (SCREEN_WIDTH // 2 - (154 / 2), SCREEN_HEIGHT // 2 - 90),
        )
        self.middle_button = Button(
            middle_image,
            middle_image_hover,
            (SCREEN_WIDTH // 2 - (154 / 2), SCREEN_HEIGHT // 2 - 20),
        )
        self.hard_button = Button(
            hard_image,
            hard_image_hover,
            (SCREEN_WIDTH // 2 - (154 / 2), SCREEN_HEIGHT // 2 + 50),
        )
        self.back_button = Button(
            back_image,
            back_image_hover,
            (SCREEN_WIDTH // 2 - (154 / 2), SCREEN_HEIGHT // 2 + 140),
        )

    def draw(self, mouse_pos):
        """Отрисовка меню настроек и возврат прямоугольников кнопок."""
        screen.blit(
            self.settings_image,
            (SCREEN_WIDTH // 2 - (193 / 2), SCREEN_HEIGHT // 5 - 60),
        )

        self.easy_button.draw(mouse_pos)
        self.middle_button.draw(mouse_pos)
        self.hard_button.draw(mouse_pos)
        self.back_button.draw(mouse_pos)

        return (
            self.easy_button.get_rect(),
            self.middle_button.get_rect(),
            self.hard_button.get_rect(),
            self.back_button.get_rect(),
        )


class MainGameMenu:
    """Класс для основной игры."""

    def __init__(self):
        """Инициализация меню игры и кнопки меню."""
        self.menu_button = Button(
            menu_image,
            menu_image_hover,
            (SCREEN_WIDTH - 76, SCREEN_HEIGHT - 32),
        )

    def draw(self, mouse_pos):
        """Отрисовка кнопки меню в основной игре."""
        self.menu_button.draw(mouse_pos)
        return self.menu_button.get_rect()
