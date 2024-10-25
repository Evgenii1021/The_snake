"""
Модуль для создания интерфейса меню игры.

Этот модуль содержит классы для управления основным меню игры,
меню настроек и меню игры. Он включает в себя функциональность
для создания и отображения кнопок, а также обработки наведения
курсора на кнопки.

Классы:
    - Button: Класс для создания кнопок меню.
    - MainMenu: Класс для основного меню игры, содержащий кнопки
      для начала игры, доступа к настройкам и выхода из игры.
    - SettingsMenu: Класс для меню настроек игры, позволяющий
      выбирать уровень сложности и возвращаться в основное меню.
    - MainGameMenu: Класс для меню игры, содержащий кнопку для
      возврата в основное меню.

Примечания:
    Этот модуль предполагает использование библиотеки Pygame для
    отрисовки графики и обработки событий.
"""


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
    """Класс для создания кнопок меню.

    Этот класс отвечает за инициализацию и отрисовку кнопок, а также
    проверку наведения курсора на кнопку.

    Attributes:
        image (Surface): Изображение кнопки.
        hover_image (Surface): Изображение кнопки при наведении.
        position (tuple): Позиция кнопки на экране.
        rect (Rect): Прямоугольник, охватывающий кнопку.
    """

    def __init__(self, image, hover_image, position):
        """Инициализация кнопки.

        Args:
            image (Surface): Изображение кнопки.
            hover_image (Surface): Изображение кнопки при наведении.
            position (tuple): Позиция кнопки на экране.
        """
        self.image = image
        self.hover_image = hover_image
        self.position = position
        self.rect = self.image.get_rect(topleft=position)

    def draw(self, mouse_pos):
        """Отрисовка кнопки и проверка наведения курсора.

        Args:
            mouse_pos (tuple): Позиция курсора мыши.
        """
        if self.rect.collidepoint(mouse_pos):
            screen.blit(self.hover_image, self.position)
        else:
            screen.blit(self.image, self.position)

    def get_rect(self):
        """Возвращает прямоугольник кнопки.

        Returns:
            Rect: Прямоугольник, охватывающий кнопку.
        """
        return self.rect


class MainMenu:
    """Класс для основного меню игры.

    Этот класс управляет основным меню и кнопками, включая
    создание и отрисовку кнопок.

    Attributes:
        play_button (Button): Кнопка для начала игры.
        settings_button (Button): Кнопка для настройки игры.
        exit_button (Button): Кнопка для выхода из игры.
    """

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
        """Отрисовка кнопок основного меню и возврат их прямоугольников.

        Args:
            mouse_pos (tuple): Позиция курсора мыши.

        Returns:
            tuple: Прямоугольники кнопок play, settings и exit.
        """
        self.play_button.draw(mouse_pos)
        self.settings_button.draw(mouse_pos)
        self.exit_button.draw(mouse_pos)

        return (
            self.play_button.get_rect(),
            self.settings_button.get_rect(),
            self.exit_button.get_rect(),
        )


class SettingsMenu:
    """Класс для меню настроек игры.

    Этот класс управляет меню настроек и кнопками, включая
    создание и отрисовку кнопок для выбора уровня сложности.

    Attributes:
        settings_image (Surface): Изображение фона меню настроек.
        easy_button (Button): Кнопка для выбора легкого уровня.
        middle_button (Button): Кнопка для выбора среднего уровня.
        hard_button (Button): Кнопка для выбора сложного уровня.
        back_button (Button): Кнопка для возврата в основное меню.
    """

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
        """Отрисовка меню настроек и возврат прямоугольников кнопок.

        Args:
            mouse_pos (tuple): Позиция курсора мыши.

        Returns:
            tuple: Прямоугольники кнопок easy, middle, hard и back.
        """
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
    """Класс для основной игры.

    Этот класс управляет меню игры и кнопкой для возврата в
    основное меню.

    Attributes:
        menu_button (Button): Кнопка для возврата в основное меню.
    """

    def __init__(self):
        """Инициализация меню игры и кнопки меню."""
        self.menu_button = Button(
            menu_image,
            menu_image_hover,
            (SCREEN_WIDTH - 76, SCREEN_HEIGHT - 32),
        )

    def draw(self, mouse_pos):
        """Отрисовка кнопки меню в основной игре.

        Args:
            mouse_pos (tuple): Позиция курсора мыши.

        Returns:
            Rect: Прямоугольник кнопки меню.
        """
        self.menu_button.draw(mouse_pos)
        return self.menu_button.get_rect()
