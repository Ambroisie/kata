from rover import Direction, Rover, Vector


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
