import enum

from pydantic import BaseModel


class Vector(BaseModel):
    x: int = 0
    y: int = 0


class Direction(enum.Enum):
    NORTH = "N"
    SOUTH = "S"
    EAST = "E"
    WEST = "W"


class Rover(BaseModel):
    pos: Vector = Vector(x=0, y=0)
    planet_size: Vector = Vector(x=100, y=100)
    dir: Direction = Direction.NORTH

    def forward(self):
        if self.dir == Direction.NORTH:
            self.pos.y += 1
        elif self.dir == Direction.SOUTH:
            self.pos.y -= 1
        elif self.dir == Direction.EAST:
            self.pos.x += 1
        elif self.dir == Direction.WEST:
            self.pos.x -= 1

        if self.pos.x < 0:
            self.pos.x += self.planet_size.x
        if self.pos.y < 0:
            self.pos.y += self.planet_size.y
