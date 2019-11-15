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


DIRECTIONS = [Direction.NORTH, Direction.EAST, Direction.SOUTH, Direction.WEST]


class Rover(BaseModel):
    pos: Vector = Vector(x=0, y=0)
    planet_size: Vector = Vector(x=100, y=100)
    dir: Direction = Direction.NORTH

    def _translate(self, value):
        if self.dir == Direction.NORTH:
            self.pos.y += value
        elif self.dir == Direction.SOUTH:
            self.pos.y -= value
        elif self.dir == Direction.EAST:
            self.pos.x += value
        elif self.dir == Direction.WEST:
            self.pos.x -= value

        if self.pos.x < 0:
            self.pos.x += self.planet_size.x
        if self.pos.y < 0:
            self.pos.y += self.planet_size.y

        self.pos.x %= self.planet_size.x
        self.pos.y %= self.planet_size.y

    def forward(self):
        self._translate(1)

    def backward(self):
        self._translate(-1)

    def _turn(self, value):
        index: int = DIRECTIONS.index(self.dir)
        self.dir = DIRECTIONS[(index + value) % len(DIRECTIONS)]

    def turn_left(self):
        self._turn(-1)

    def turn_right(self):
        self._turn(1)
