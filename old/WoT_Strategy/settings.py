from enum import IntEnum
from typing import TypedDict


# Typings
class CoordsDict(TypedDict):
    x: int
    y: int
    z: int


CoordsTuple = tuple[int, int, int]


class HexCode(IntEnum):
    EMPTY = 0
    BASE = -1
    OBSTACLE = -2

    def __str__(self):
        return str(self.value)


TYPE_ORDER = ("spg", "light_tank", "heavy_tank", "medium_tank", "at_spg")

NEIGHBOURS_OFFSETS = (
    (
        (0, -1, 1),
        (1, -1, 0),
        (1, 0, -1),
        (0, 1, -1),
        (-1, 1, 0),
        (-1, 0, 1),
    ),
    (
        (0, -2, 2),
        (1, -2, 1),
        (2, -2, 0),
        (2, -1, -1),
        (2, 0, -2),
        (1, 1, -2),
        (0, 2, -2),
        (-1, 2, -1),
        (-2, 2, 0),
        (-2, 1, 1),
        (-2, 0, 2),
        (-1, -1, 2),
    ),
    (
        (0, -3, 3),
        (1, -3, 2),
        (2, -3, 1),
        (3, -3, 0),
        (3, -2, -1),
        (3, -1, -2),
        (3, 0, -3),
        (2, 1, -3),
        (1, 2, -3),
        (0, 3, -3),
        (-1, 3, -2),
        (-2, 3, -1),
        (-3, 3, 0),
        (-3, 2, 1),
        (-3, 1, 2),
        (-3, 0, 3),
        (-2, -1, 3),
        (-1, -2, 3),
    ),
)