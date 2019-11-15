from dataclasses import dataclass


@dataclass
class Vector:
    x: int
    y: int


@dataclass
class Rover:
    pos: Vector = (0, 0)
    planet_size: Vector = (100, 100)
