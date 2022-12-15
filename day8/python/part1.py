"""Day 8 of Advent of Code"""

from typing import Tuple

from numpy import array, where, sum as ndarray_sum
from numpy._typing import NDArray


def parse_input(input_prompt: str) -> NDArray:
    "Create an array from the input prompt"
    Grid = []
    for line in input_prompt:
        Grid.append(list(map(int, list(line))))
    return array(Grid)


def visible_row(grid: NDArray, idx: Tuple[int, int], right: bool = True) -> bool:
    """
    Return True if the tree at index is visible according the direction right or left.
    """
    row, col = idx

    tree = grid[idx]
    if right:
        extracted_row = grid[row, :col]
    else:
        extracted_row = grid[row, col + 1 :]

    for element in extracted_row:
        if element >= tree:
            return False
    return True


def visible_col(grid: NDArray, idx: Tuple[int, int], top: bool = True) -> bool:
    """
    Return True if the tree at index is visible according the direction top or down.
    """
    row, col = idx

    tree = grid[idx]
    if top:
        extracted_row = grid[:row, col]
    else:
        extracted_row = grid[row + 1 :, col]

    for element in extracted_row:
        if element >= tree:
            return False
    return True


def visible(grid: NDArray, idx: Tuple[int, int]) -> bool:
    if (
        idx[0] == 0
        or idx[0] == (grid.shape[0] - 1)
        or idx[1] == 0
        or idx[1] == (grid.shape[1] - 1)
    ):
        return True
    visible_right = visible_row(grid, idx, True)
    visible_left = visible_row(grid, idx, False)
    visible_top = visible_col(grid, idx, True)
    visible_down = visible_col(grid, idx, False)
    return visible_right or visible_left or visible_top or visible_down


if __name__ == "__main__":
    with open(file="day8/ressources/input.txt", encoding="utf-8") as f:
        INPUT_PROMPT = "".join(f.readlines()).split("\n")
    grid = parse_input(INPUT_PROMPT)
    ROW, COL = grid.shape

    truth_grid = []
    for i in range(ROW):
        truth_grid_row = []
        for j in range(COL):
            truth_grid_row.append(visible(grid, (i, j)))
        truth_grid.append(truth_grid_row)
    print(ndarray_sum(where(array(truth_grid), 1, 0)))
