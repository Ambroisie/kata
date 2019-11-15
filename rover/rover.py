import enum
from dataclasses import dataclass


@dataclass
class Vector:
    x: int
    y: int


class Direction(enum.Enum):
    NORTH = "N"
    SOUTH = "S"
    EAST = "E"
    WEST = "W"


@dataclass
class Rover:
    pos: Vector = (0, 0)
    planet_size: Vector = (100, 100)
    dir: Direction = Direction.NORTH
