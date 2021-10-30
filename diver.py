from typing import List
from collections import deque


CAVE = 2147483647
WALL = -1
ENTRANCE = 0


def bfs_from_entrance(n_rows: int, n_cols: int, entrance_row: int, entrance_col: int, cave: List[List[int]]):
    layer = set()
    layer.add((entrance_row, entrance_col, 0))
    cave[entrance_row][entrance_col] = CAVE  # hax to get it started
    while True:
        next_layer = set()
        while len(layer) > 0:
            row, col, distance = layer.pop()
            if distance < cave[row][col]:  # found a better way to this spot
                cave[row][col] = distance  # update the cave grid
                if row > 0 and cave[row - 1][col] > 0 and (row - 1, col):  # on the grid, not a wall or entrance, haven't been there yet
                    next_layer.add((row - 1, col, distance + 1))
                if row + 1 < n_rows and cave[row + 1][col] > 0 and (row + 1, col):
                    next_layer.add((row + 1, col, distance + 1))
                if col > 0 and cave[row][col - 1] > 0 and (row, col - 1):
                    next_layer.add((row, col - 1, distance + 1))
                if col + 1 < n_cols and cave[row][col + 1] > 0 and (row, col + 1):
                    next_layer.add((row, col + 1, distance + 1))
        if len(next_layer) == 0:
            break
        layer = next_layer


if __name__ == "__main__":
    m = int(input())  # n_rows
    n = int(input())  # n_cols
    cave_grid = list()
    for _ in range(m):
        cave_grid.append(list(map(int, input().split())))
    for row_ in range(m):
        for col_ in range(n):
            if cave_grid[row_][col_] == ENTRANCE:
                bfs_from_entrance(m, n, row_, col_, cave_grid)
    # print the answer
    for row_list in cave_grid:
        print(" ".join(str(x) for x in row_list))
