from typing import List


def can_cross(n_rows: int, n_cols: int, city: List[List[bool]]) -> bool:
    layer = set()
    visited = set()
    for row in range(n_rows):
        if city[row][0]:
            layer.add((row, 0))
            visited.add((row, 0))
    while True:
        next_layer = set()
        for row, col in sorted(layer, key=lambda x: x[1], reverse=True):
            if row > 0 and city[row - 1][col] and (row - 1, col) not in visited:  # on the grid, not flooded, haven't been there yet
                next_layer.add((row - 1, col))
                visited.add((row - 1, col))
            if row + 1 < n_rows and city[row + 1][col] and (row + 1, col) not in visited:
                next_layer.add((row + 1, col))
                visited.add((row + 1, col))
            if col > 0 and city[row][col - 1] and (row, col - 1) not in visited:
                next_layer.add((row, col - 1))
                visited.add((row, col - 1))
            if col + 1 < n_cols and city[row][col + 1] and (row, col + 1) not in visited:
                if col + 1 == n_cols - 1:  # this step would make us win
                    return True
                next_layer.add((row, col + 1))
                visited.add((row, col + 1))
        if len(next_layer) == 0:
            break
        layer = next_layer
    return False


if __name__ == "__main__":
    m, n = map(int, input().split())  # m = n_rows
    city_grid = [[True for c in range(n)] for r in range(m)]
    for i in range(m * n):
        row_raw, col_raw = map(int, input().split())
        row_ = row_raw - 1
        col_ = col_raw - 1
        city_grid[row_][col_] = False  # flood the square
        if not can_cross(m, n, city_grid):
            print(i)
            exit(0)
    print(m * n)
