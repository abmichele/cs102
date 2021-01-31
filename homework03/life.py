import pathlib
import random
import typing as tp

import pygame
from pygame.locals import *
from copy import deepcopy
from itertools import product

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


class GameOfLife:
    def __init__(
        self,
        size: tp.Tuple[int, int],
        randomize: bool = True,
        max_generations: float = float("inf"),
    ) -> None:
        # Размер клеточного поля
        self.rows, self.cols = size
        # Предыдущее поколение клеток
        self.prev_generation = self.create_grid()
        # Текущее поколение клеток
        self.curr_generation = self.create_grid(randomize=randomize)
        # Максимальное число поколений
        self.max_generations = max_generations
        # Текущее число поколений
        self.generations = 1

    def create_grid(self, randomize: bool = False) -> Grid:
        self.grid = [[0] * self.cols for i in range(self.rows)]
        if randomize:
            for i in range(self.rows):
                for j in range(self.cols):
                    self.grid[i][j] = random.randint(0, 1)
        return self.grid

    def get_neighbours(self, cell: Cell) -> Cells:
        neighbours = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                m = cell[0] + i
                n = cell[1] + j
                if 0 <= n < self.cols and 0 <= m < self.rows and (i, j) != (0, 0):
                    neighbours.append(self.curr_generation[m][n])
        return neighbours

    def get_next_generation(self) -> Grid:
        m = deepcopy(self.curr_generation)
        for i in range(self.rows):
            for j in range(self.cols):
                if sum(self.get_neighbours((i, j))) < 2 or sum(self.get_neighbours((i, j))) > 3:
                    m[i][j] = 0
                elif sum(self.get_neighbours((i, j))) == 3:
                    m[i][j] = 1
        return m

    def step(self) -> None:
        """
        Выполнить один шаг игры.
        """
        self.prev_generation = deepcopy(self.curr_generation)
        self.curr_generation = self.get_next_generation()
        self.generations += 1

    @property
    def is_max_generations_exceeded(self) -> bool:
        """
        Не превысило ли текущее число поколений максимально допустимое.
        """
        return self.generations >= self.max_generations

    @property
    def is_changing(self) -> bool:
        """
        Изменилось ли состояние клеток с предыдущего шага.
        """
        return not self.curr_generation == self.prev_generation

    @staticmethod
    def from_file(filename: pathlib.Path) -> "GameOfLife":
        """
        Прочитать состояние клеток из указанного файла.
        """
        rows = 0
        grid = []
        f = open(filename, "r")
        for line in f:
            row = [int(i) for i in line if i != "\n"]
            grid.append(row)
            rows += 1
        cols = len(row)
        start_from_file = GameOfLife((rows, cols), False)
        # start_from_file.prev_generation = GameOfLife.create_grid(start_from_file)
        start_from_file.curr_generation = grid
        f.close()

        return start_from_file

    def save(self, filename: pathlib.Path) -> None:
        """
        Сохранить текущее состояние клеток в указанный файл.
        """
        file = open(filename, "w")
        for i in range(len(self.curr_generation)):
            file.write(str(self.curr_generation[i]) + "/n")
        file.close()
