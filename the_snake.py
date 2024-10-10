from random import choice, randint

import pygame

# Константы для размеров поля и сетки:
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Направления движения:
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Цвет фона - черный:
BOARD_BACKGROUND_COLOR = (0, 0, 0)

# Цвет границы ячейки
BORDER_COLOR = (93, 216, 228)

# Цвет яблока
APPLE_COLOR = (255, 0, 0)

# Цвет змейки
SNAKE_COLOR = (0, 255, 0)

# Скорость движения змейки:
SPEED = 20

# Настройка игрового окна:
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

# Заголовок окна игрового поля:
pygame.display.set_caption("Змейка")

# Настройка времени:
clock = pygame.time.Clock()


# Тут опишите все классы игры.
class GameObject:
    """Базовый класс для всех объектов игры."""

    def __init__(self):
        self.position = ((SCREEN_WIDTH // 2), (SCREEN_HEIGHT // 2))
        self.body_color = None

    def draw(self):
        pass


class Apple(GameObject):
    """Класс яблока."""

    def __init__(self):
        super().__init__()
        self.body_color = APPLE_COLOR
        self.randomize_position()

    def randomize_position(self):
        self.position = (randint(0, SCREEN_WIDTH - 1), randint(0, SCREEN_HEIGHT - 1))

    def draw(self):
        rect = pygame.Rect(self.position, (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, rect)
        pygame.draw.rect(screen, BORDER_COLOR, rect, 1)


class Snake(GameObject):
    """Класс змейки."""

    def __init__(self):
        super().__init__()
        self.positions = [self.position]
        self.body_color = SNAKE_COLOR
        self.length = 1
        self.direction = UP
        self.next_direction = None
        self.last = None

    def update_direction(self):
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None

    def get_head_position(self):
        return self.positions[0]

    def move(self):
        head_x, head_y = self.get_head_position()

        if self.direction == RIGHT:
            self.positions[0] = (head_x + GRID_SIZE, head_y)
        elif self.direction == LEFT:
            self.positions[0] = (head_x - GRID_SIZE, head_y)
        elif self.direction == UP:
            self.positions[0] = (head_x, head_y - GRID_SIZE)
        elif self.direction == DOWN:
            self.positions[0] = (head_x, head_y + GRID_SIZE)

        if self.positions[0][0] >= SCREEN_WIDTH - GRID_SIZE:
            self.positions[0] = (0, self.positions[0][1])
        elif self.positions[0][0] < 0:
            self.positions[0] = (SCREEN_WIDTH - GRID_SIZE, self.positions[0][1])
        elif self.positions[0][1] < 0:
            self.positions[0] = (self.positions[0][0], SCREEN_HEIGHT - GRID_SIZE)
        elif self.positions[0][1] >= SCREEN_WIDTH - GRID_SIZE:
            self.positions[0] = (self.positions[0][0], 0)

        self.positions.insert(0, self.positions[0])

        if len(self.positions) > self.length:
            self.positions.pop()

    def draw(self):
        for position in self.positions[:-1]:
            rect = pygame.Rect(position, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, self.body_color, rect)
            pygame.draw.rect(screen, BORDER_COLOR, rect, 1)

        # Отрисовка головы змейки
        head_rect = pygame.Rect(self.positions[0], (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, head_rect)
        pygame.draw.rect(screen, BORDER_COLOR, head_rect, 1)

        # Затирание последнего сегмента
        if self.last:
            last_rect = pygame.Rect(self.last, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, BOARD_BACKGROUND_COLOR, last_rect)

    def reset(self):
        self.positions = [self.position]
        self.length = 1
        self.direction = choice(LEFT, RIGHT, UP, DOWN)


def handle_keys(game_object):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and game_object.direction != DOWN:
                game_object.next_direction = UP
            elif event.key == pygame.K_DOWN and game_object.direction != UP:
                game_object.next_direction = DOWN
            elif event.key == pygame.K_LEFT and game_object.direction != RIGHT:
                game_object.next_direction = LEFT
            elif event.key == pygame.K_RIGHT and game_object.direction != LEFT:
                game_object.next_direction = RIGHT


def main():
    # Инициализация PyGame:
    pygame.init()
    # Тут нужно создать экземпляры классов.
    snake = Snake()
    apple = Apple()

    while True:
        clock.tick(SPEED)

        # Тут опишите основную логику игры.
        handle_keys(snake)
        snake.update_direction()
        snake.move()

        if (
            apple.position[0] - GRID_SIZE
            <= snake.positions[0][0]
            <= apple.position[0] + GRID_SIZE
            and apple.position[1] - GRID_SIZE
            <= snake.positions[0][1]
            <= apple.position[1] + GRID_SIZE
        ):
            snake.length += 1
            snake.positions.insert(-1, apple.position)
            apple.randomize_position()

        pygame.display.update()
        screen.fill(BOARD_BACKGROUND_COLOR)
        snake.draw()
        apple.draw()
        pygame.display.flip()


if __name__ == "__main__":
    main()
