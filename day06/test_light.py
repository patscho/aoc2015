import pytest
from light import Light, Grid


def test_init():
    # Create a light at position (1,2)
    light = Light((1, 2))
    assert light.status == 0 and light.x == 1 and light.y == 2


def test_turn_on():
    light = Light((0, 0))
    light.turn_on()
    assert light.status == 1


def test_turn_off():
    light = Light((0, 0))
    light.turn_off()
    assert light.status == 0


def test_toggle():
    light = Light((0, 0))
    light.toggle()
    assert light.status == 1


def test_grid_init():
    grid = Grid(10)
    assert len(grid.lights) == 100


def test_grid_turn_on():
    grid = Grid(10)
    grid.turn_on((0, 0), (2, 2))
    assert (
        grid.lights[(0, 0)].status == 1
        and grid.lights[(1, 0)].status == 1
        and grid.lights[(2, 0)].status == 1
        and grid.lights[(0, 1)].status == 1
        and grid.lights[(1, 1)].status == 1
        and grid.lights[(2, 1)].status == 1
        and grid.lights[(0, 2)].status == 1
        and grid.lights[(1, 2)].status == 1
        and grid.lights[(2, 2)].status == 1
    )


def test_grid_turn_on():
    grid = Grid(10)
    grid.turn_on((0, 0), (9, 0))
    assert (
        grid.lights[(0, 0)].status == 1
        and grid.lights[(1, 0)].status == 1
        and grid.lights[(2, 0)].status == 1
        and grid.lights[(3, 0)].status == 1
        and grid.lights[(4, 0)].status == 1
        and grid.lights[(5, 0)].status == 1
        and grid.lights[(6, 0)].status == 1
        and grid.lights[(7, 0)].status == 1
        and grid.lights[(8, 0)].status == 1
        and grid.lights[(9, 0)].status == 1
    )


def test_number_of_lights_on():
    grid = Grid(10)
    grid.turn_on((0, 0), (9, 0))
    assert grid.number_of_lights_on() == 10
