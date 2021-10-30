from typing import List, Tuple


def can_cross(n_rows: int, n_cols: int, city: List[List[bool]]) -> List[Tuple[int, int]]:
    layer = set()
    back_trace = dict()
    has_exit = False
    for row in range(n_rows):
        if city[row][-1]:
            has_exit = True
        if city[row][0]:
            layer.add((row, 0))
            back_trace[(row, 0)] = None
    if not has_exit:
        return None
    while True:
        next_layer = set()
        for row, col in sorted(layer, key=lambda x: x[1], reverse=True):
            if col + 1 < n_cols and city[row][col + 1] and (row, col + 1) not in back_trace:
                if col + 1 == n_cols - 1:  # this step would make us win
                    back_trace[(row, col + 1)] = (row, col)
                    # get the path
                    position = (row, col + 1)
                    to_return = list()
                    while position is not None:
                        to_return.append(position)
                        position = back_trace[position]
                    return to_return
                next_layer.add((row, col + 1))
                back_trace[(row, col + 1)] = (row, col)
            if row > 0 and city[row - 1][col] and (row - 1, col) not in back_trace:  # on the grid, not flooded, haven't been there yet
                next_layer.add((row - 1, col))
                back_trace[(row - 1, col)] = (row, col)
            if row + 1 < n_rows and city[row + 1][col] and (row + 1, col) not in back_trace:
                next_layer.add((row + 1, col))
                back_trace[(row + 1, col)] = (row, col)
            if col > 0 and city[row][col - 1] and (row, col - 1) not in back_trace:
                next_layer.add((row, col - 1))
                back_trace[(row, col - 1)] = (row, col)
        if len(next_layer) == 0:
            break
        layer = next_layer
    return None


if __name__ == "__main__":
    m, n = map(int, input().split())  # m = n_rows
    city_grid = [[True for c in range(n)] for r in range(m)]
    path = None
    for i in range(m * n):
        row_raw, col_raw = map(int, input().split())
        row_ = row_raw - 1
        col_ = col_raw - 1
        city_grid[row_][col_] = False  # flood the square
        if path is None or (row_, col_) in path:
            path = can_cross(m, n, city_grid)
            if path is None:
                print(i)
                exit(0)
    print(m * n)
