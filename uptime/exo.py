from argparse import ArgumentParser
from random import choice

import matplotlib.pyplot as plt
import numpy as np

WATER_POINT_TYPE = 'WATER'
EARTH_POINT_TYPE = 'EARTH'
POINT_TYPES = [
    WATER_POINT_TYPE,
    EARTH_POINT_TYPE,
]

DEFAULT_WATER_COLOR = [30, 144, 255]
DEFAULT_EARTH_COLOR = [105, 105, 105]
DEFAULT_COLORS = {
    WATER_POINT_TYPE: DEFAULT_WATER_COLOR,  # blue
    EARTH_POINT_TYPE: DEFAULT_EARTH_COLOR,  # dark grey
}


class Map:

    def __init__(self, height, width):
        _map = []
        for y in range(height):
            row = []
            for x in range(width):
                row.append(self._generate_point_type())
            _map.append(row)
        self._map = _map

    @staticmethod
    def _generate_point_type():
        return choice(POINT_TYPES)

    @staticmethod
    def _generate_random_color():
        color = None
        while color is None or color in [DEFAULT_WATER_COLOR, DEFAULT_EARTH_COLOR]:
            color = [choice(range(256)) for x in range(3)]
        return color

    def generate_colored(self):
        colored_map = []
        for row in self._map:
            colored_row = []
            for point in row:
                colored_row.append(DEFAULT_COLORS.get(point))
            colored_map.append(colored_row)
        return self.print_new_colors(colored_map)

    def print_new_colors(self, grid):
        def dfs(i, j, c):
            if grid[i][j] == DEFAULT_WATER_COLOR or grid[i][j] != DEFAULT_EARTH_COLOR:
                return

            grid[i][j] = c

            if i > 0:
                dfs(i - 1, j, c)
            if i < len(grid) - 1:
                dfs(i + 1, j, c)
            if j > 0:
                dfs(i, j - 1, c)
            if j < len(grid[0]) - 1:
                dfs(i, j + 1, c)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == DEFAULT_EARTH_COLOR:
                    dfs(i, j, self._generate_random_color())

        return grid

    def plot(self):
        ar = np.array(self.generate_colored())
        manager = plt.get_current_fig_manager()
        manager.full_screen_toggle()
        plt.imshow(ar)
        plt.show()


if __name__ == '__main__':
    ap = ArgumentParser()
    ap.add_argument("-H", "--height", required=False, default=30, type=int)
    ap.add_argument("-W", "--width", required=False, default=30, type=int)
    dimensions = ap.parse_args()
    my_map = Map(dimensions.height, dimensions.width)
    my_map.plot()
