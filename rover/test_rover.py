import pytest
from rover import Commander, Direction, ObstacleError, Rover, Vector


def test_rover_constructor():
    rov = Rover(pos={"x": 0, "y": 0}, planet_size={"x": 100, "y": 100})
    assert rov.pos == Vector(x=0, y=0) and rov.planet_size == Vector(x=100, y=100)


def test_rover_default_values():
    rov = Rover()
    assert rov.pos == Vector(x=0, y=0) and rov.planet_size == Vector(x=100, y=100)


def test_rover_has_direction():
    rov = Rover(dir=Direction.NORTH)
    assert rov.dir == Direction.NORTH


def test_rover_default_direction_is_north():
    rov = Rover()
    assert rov.dir == Direction.NORTH


def test_rover_can_go_forward_once_going_north():
    rov = Rover(
        pos=Vector(x=0, y=0), planet_size=Vector(x=10, y=10), dir=Direction.NORTH
    )
    rov.forward()
    assert rov.pos == Vector(x=0, y=1)


def test_rover_can_go_forward_twice_going_north():
    rov = Rover(
        pos=Vector(x=0, y=0), planet_size=Vector(x=10, y=10), dir=Direction.NORTH
    )
    rov.forward()
    rov.forward()
    assert rov.pos == Vector(x=0, y=2)


def test_rover_can_go_forward_going_east():
    rov = Rover(
        pos=Vector(x=0, y=0), planet_size=Vector(x=10, y=10), dir=Direction.EAST
    )
    rov.forward()
    assert rov.pos == Vector(x=1, y=0)


def test_rover_can_go_forward_going_south():
    rov = Rover(
        pos=Vector(x=0, y=1), planet_size=Vector(x=10, y=10), dir=Direction.SOUTH
    )
    rov.forward()
    assert rov.pos == Vector(x=0, y=0)


def test_rover_can_go_forward_going_west():
    rov = Rover(
        pos=Vector(x=1, y=0), planet_size=Vector(x=10, y=10), dir=Direction.WEST
    )
    rov.forward()
    assert rov.pos == Vector(x=0, y=0)


def test_rover_can_wrap_under_north_south():
    rov = Rover(
        pos=Vector(x=0, y=0), planet_size=Vector(x=10, y=10), dir=Direction.SOUTH
    )
    rov.forward()
    assert rov.pos == Vector(x=0, y=9)


def test_rover_can_wrap_under_east_west():
    rov = Rover(
        pos=Vector(x=0, y=0), planet_size=Vector(x=10, y=10), dir=Direction.WEST
    )
    rov.forward()
    assert rov.pos == Vector(x=9, y=0)


def test_rover_can_wrap_over_north_south():
    rov = Rover(
        pos=Vector(x=0, y=9), planet_size=Vector(x=10, y=10), dir=Direction.NORTH
    )
    rov.forward()
    assert rov.pos == Vector(x=0, y=0)


def test_rover_can_wrap_over_east_west():
    rov = Rover(
        pos=Vector(x=9, y=0), planet_size=Vector(x=10, y=10), dir=Direction.EAST
    )
    rov.forward()
    assert rov.pos == Vector(x=0, y=0)


def test_rover_can_go_backward_north():
    rov = Rover(
        pos=Vector(x=0, y=1), planet_size=Vector(x=10, y=10), dir=Direction.NORTH
    )
    rov.backward()
    assert rov.pos == Vector(x=0, y=0)


def test_rover_can_go_backward_south():
    rov = Rover(
        pos=Vector(x=0, y=0), planet_size=Vector(x=10, y=10), dir=Direction.SOUTH
    )
    rov.backward()
    assert rov.pos == Vector(x=0, y=1)


def test_rover_can_go_backward_west():
    rov = Rover(
        pos=Vector(x=0, y=0), planet_size=Vector(x=10, y=10), dir=Direction.WEST
    )
    rov.backward()
    assert rov.pos == Vector(x=1, y=0)


def test_rover_can_go_backward_east():
    rov = Rover(
        pos=Vector(x=1, y=0), planet_size=Vector(x=10, y=10), dir=Direction.EAST
    )
    rov.backward()
    assert rov.pos == Vector(x=0, y=0)


def test_rover_can_go_backward_wrapping_under_north_south():
    rov = Rover(
        pos=Vector(x=0, y=0), planet_size=Vector(x=10, y=10), dir=Direction.NORTH
    )
    rov.backward()
    assert rov.pos == Vector(x=0, y=9)


def test_rover_can_go_backward_wrapping_over_north_south():
    rov = Rover(
        pos=Vector(x=0, y=9), planet_size=Vector(x=10, y=10), dir=Direction.SOUTH
    )
    rov.backward()
    assert rov.pos == Vector(x=0, y=0)


def test_rover_can_go_backward_wrapping_under_east_west():
    rov = Rover(
        pos=Vector(x=0, y=0), planet_size=Vector(x=10, y=10), dir=Direction.EAST
    )
    rov.backward()
    assert rov.pos == Vector(x=9, y=0)


def test_rover_can_go_backward_wrapping_over_east_west():
    rov = Rover(
        pos=Vector(x=9, y=0), planet_size=Vector(x=10, y=10), dir=Direction.WEST
    )
    rov.backward()
    assert rov.pos == Vector(x=0, y=0)


def test_rover_can_turn_left():
    rov = Rover(dir=Direction.NORTH)
    rov.turn_left()
    assert rov.dir == Direction.WEST


def test_rover_can_turn_right():
    rov = Rover(dir=Direction.NORTH)
    rov.turn_right()
    assert rov.dir == Direction.EAST


def test_commander_constructor():
    com = Commander(
        rover=Rover(
            pos=Vector(x=12, y=27), planet_size=Vector(x=100, y=100), dir=Direction.WEST
        )
    )
    assert (
        com.rover.pos == Vector(x=12, y=27)
        and com.rover.planet_size == Vector(x=100, y=100)
        and com.rover.dir == Direction.WEST
    )


def test_commander_default_values():
    com = Commander()

    assert com.rover == Rover()


def test_commander_can_parse_left():
    com = Commander()
    com.parse_execute("L")
    assert com.rover == Rover(dir=Direction.WEST)


def test_commander_can_parse_right():
    com = Commander()
    com.parse_execute("R")
    assert com.rover == Rover(dir=Direction.EAST)


def test_commmander_can_parse_forward():
    com = Commander()
    com.parse_execute("F")
    assert com.rover == Rover(pos=Vector(x=0, y=1))


def test_commmander_can_parse_backward():
    com = Commander(rover=Rover(pos=Vector(x=0, y=1)))
    com.parse_execute("B")
    assert com.rover == Rover()


def test_commander_complex_command():
    com = Commander()
    com.parse_execute("FRFRFLB")
    assert com.rover == Rover(dir=Direction.EAST)


def test_commander_command_with_obstacles():
    com = Commander(obstacles=[Vector(x=1, y=0), Vector(x=1, y=2)])
    with pytest.raises(ObstacleError):
        com.parse_execute("FFRF")
    assert com.rover == Rover(pos=Vector(x=0, y=2), dir=Direction.EAST)
