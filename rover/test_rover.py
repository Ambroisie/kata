from rover import Direction, Rover


def test_rover_constructor():
    rov = Rover(pos=(0, 0), planet_size=(100, 100))
    assert rov.pos == (0, 0) and rov.planet_size == (100, 100)


def test_rover_default_values():
    rov = Rover()
    assert rov.pos == (0, 0) and rov.planet_size == (100, 100)


def test_rover_has_direction():
    rov = Rover(dir=Direction.NORTH)
    assert rov.dir == Direction.NORTH


def test_rover_default_direction_is_north():
    rov = Rover()
    assert rov.dir == Direction.NORTH
