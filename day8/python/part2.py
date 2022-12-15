"""Day 8 of Advent of Code"""

from typing import Tuple

from numpy import array
from numpy._typing import NDArray


def parse_input(input_prompt: str) -> NDArray:
    "Create an array from the input prompt"
    Grid = []
    for line in input_prompt:
        Grid.append(list(map(int, list(line))))
    return array(Grid)


def visible_row(grid: NDArray, idx: Tuple[int, int], right: bool = True) -> int:
    """
    Return True if the tree at index is visible according the direction right or left.
    """
    row, col = idx

    if right:
        extracted_row = grid[row, col + 1 :]
    else:
        extracted_row = grid[row, :col][::-1]

    current_max = grid[idx]
    distance = 0
    for element in extracted_row:
        if element < current_max:
            distance += 1
        else:
            return distance + 1
    return distance


def visible_col(grid: NDArray, idx: Tuple[int, int], top: bool = True) -> int:
    """
    Return True if the tree at index is visible according the direction top or down.
    """
    row, col = idx

    if top:
        extracted_row = grid[:row, col][::-1]
    else:
        extracted_row = grid[row + 1 :, col]

    current_max = grid[idx]
    distance = 0
    for element in extracted_row:
        if element < current_max:
            distance += 1
        else:
            return distance + 1
    return distance


def visible(grid: NDArray, idx: Tuple[int, int]) -> int:
    row, col = idx
    visible_right = 0 if idx[0] == 0 else visible_row(grid, idx, True)
    visible_left = 0 if idx[0] == (grid.shape[0] - 1) else visible_row(grid, idx, False)
    visible_top = 0 if idx[1] == 0 else visible_col(grid, idx, True)
    visible_down = 0 if idx[1] == (grid.shape[0] - 1) else visible_col(grid, idx, False)
    return visible_top * visible_left * visible_right * visible_down


if __name__ == "__main__":
    with open(file="day8/ressources/input.txt", encoding="utf-8") as f:
        INPUT_PROMPT = "".join(f.readlines()).split("\n")
    grid = parse_input(INPUT_PROMPT)
    ROW, COL = grid.shape

    print(visible(grid, (1, 2)), visible(grid, (3, 2)))

    distance_grid = []
    for i in range(ROW):
        distance_grid_row = []
        for j in range(COL):
            distance_grid_row.append(visible(grid, (i, j)))
        distance_grid.append(distance_grid_row)
    print(array(distance_grid))
    print(array(distance_grid).max())
