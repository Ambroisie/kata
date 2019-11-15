from dataclasses import dataclass
from typing import Tuple

Vector = Tuple[int, int]

@dataclass
class Rover():
    pos: Vector
    planet_size: Vector
