from rover import Rover


def test_rover_constructor():
    rov = Rover(pos=(0, 0), planet_size=(100, 100))
    assert rov.pos == (0, 0) and rov.planet_size == (100, 100)
