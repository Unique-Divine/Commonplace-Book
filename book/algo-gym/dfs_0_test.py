from typing import List, Tuple, Set, Iterable

import pytest

Image = List[List[int]]


def fill_img(
    image: Image,
    new_color: int,
    start_pixel: Tuple[int, int],
) -> Image:
    """Fills the start pixel and all neighbors of the same color with the new
    color.
    """

    max_row: int = len(image)
    max_c = 0 if max_row == 0 else len(image[0])
    # Columns cannot exist if there aren't rows

    x, y = start_pixel
    if not (0 <= x < max_row and 0 <= y < max_c):
        # start pixel {start_pixel} is outside the image or invalid"
        return image

    start_color = image[x][y]
    if start_color == new_color:
        return image

    Point = Tuple[int, int]
    visited_pixels: Set[Point] = set()

    def dfs_fill(row: int, col: int):
        """Depth first search N, S, E, W directions inside the image and fill
        them with the new color IFF the pixel has the start color."""
        # Stop conditions
        # Check if row or col are invalid
        # Check if point is visited
        #
        if (
            (row < 0 or row >= max_row)  # row outside image
            or (col < 0 or col >= max_c)  # col outside image
            or (row, col) in visited_pixels  # row processed already
            or image[row][col] != start_color  # row falls outside criteria for
            # new color. Point must be start_color
        ):
            return

        # rewrite to new color
        image[row][col] = new_color
        visited_pixels.add((row, col))

        # dfs N, S, W, E
        dfs_fill(row - 1, col)
        dfs_fill(row + 1, col)
        dfs_fill(row, col - 1)
        dfs_fill(row, col + 1)

    dfs_fill(x, y)
    return image


TEST_CASES: Iterable[Tuple[str, Image, Image]] = (
    (
        "Small connected region of 1s",
        [[1, 1, 1], [1, 1, 0], [1, 0, 1]],
        [[2, 2, 2], [2, 2, 0], [2, 0, 1]],
    ),
    (
        "Fill follows a winding 1-path",
        [[1, 0, 0, 0], [1, 1, 0, 0], [0, 1, 1, 1], [0, 0, 0, 1]],
        [[2, 0, 0, 0], [2, 2, 0, 0], [0, 2, 2, 2], [0, 0, 0, 2]],
    ),
    (
        "0 is surrounded by 1s; fill from the center",
        [[1, 1, 1], [1, 0, 1], [1, 1, 1]],
        [[2, 2, 2], [2, 0, 2], [2, 2, 2]],
    ),
    (
        "Diagonals are not connected in 4-directional DFS",
        [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
        [[2, 0, 0], [0, 1, 0], [0, 0, 1]],
    ),
    ("Empty image", [], []),
    (
        "Already filled",
        [[2, 2, 2], [2, 2, 0], [2, 0, 1]],
        [[2, 2, 2], [2, 2, 0], [2, 0, 1]],
    ),
)


@pytest.mark.parametrize(
    "test_name, image, expected",
    TEST_CASES,
    ids=lambda val: val if isinstance(val, str) else None,
)
def test_fill_img(test_name: str, image: Image, expected: Image):
    result = fill_img(image, 2, (0, 0))
    assert result == expected
