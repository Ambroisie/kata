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
