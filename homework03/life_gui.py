import pygame
from life import GameOfLife
from pygame.locals import *
from ui import UI


class GUI(UI):
    def __init__(self, life: GameOfLife, cell_size: int = 10, speed: int = 10) -> None:
        super().__init__(life)

        self.width = self.life.cols * cell_size
        self.height = self.life.rows * cell_size
        self.cell_size = cell_size

        # Устанавливаем размер окна
        self.screen_size = (self.width, self.height)
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)

        # Вычисляем количество ячеек по вертикали и горизонтали
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        # Скорость протекания игры
        self.speed = speed

    def draw_lines(self) -> None:
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (0, y), (self.width, y))

    def draw_grid(self) -> None:
        for i in range(len(self.life.curr_generation)):
            for j in range(len(self.life.curr_generation[i])):
                if self.life.curr_generation[i][j] == 1:
                    pygame.draw.rect(
                        self.screen,
                        pygame.Color("green"),
                        (j * self.cell_size, i * self.cell_size, self.cell_size, self.cell_size),
                    )
                else:
                    pygame.draw.rect(
                        self.screen,
                        pygame.Color("white"),
                        (j * self.cell_size, i * self.cell_size, self.cell_size, self.cell_size),
                    )

    def run(self) -> None:
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption("Game of Life")
        self.screen.fill(pygame.Color("white"))
        running = True
        pause = False
        while running:
            self.draw_grid()
            self.draw_lines()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    (col, row) = pygame.mouse.get_pos()
                    x = row // self.cell_size
                    y = col // self.cell_size
                    if self.life.curr_generation[x][y]:
                        self.life.curr_generation[x][y] = 0
                    else:
                        self.life.curr_generation[x][y] = 1
                    self.draw_grid()
                    self.draw_lines()
                    clock.tick(self.speed)
                    pygame.display.flip()
                    continue
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if pause:
                            pause = False
                        else:
                            pause = True
            if pause:
                continue

            self.life.step()

            clock.tick(self.speed)
        pygame.quit()


if __name__ == "__main__":
    game = GameOfLife(size=(48, 64))
    app = GUI(game)
    app.run()
