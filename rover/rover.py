from dataclasses import dataclass


@dataclass
class Vector:
    x: int
    y: int


@dataclass
class Rover:
    pos: Vector
    planet_size: Vector
