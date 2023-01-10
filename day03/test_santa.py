import pytest
from santa import Santa


def test_move_1():
    santa = Santa()
    santa.move(">")
    assert len(santa.houses_visited) == 2


def test_move_2():
    santa = Santa()
    santa.move("^")
    santa.move(">")
    santa.move("v")
    santa.move("<")
    assert len(santa.houses_visited) == 4


def test_move_3():
    santa = Santa()
    santa.move("^")
    santa.move("v")
    santa.move("^")
    santa.move("v")
    santa.move("^")
    santa.move("v")
    santa.move("^")
    santa.move("v")
    santa.move("^")
    santa.move("v")
    assert len(santa.houses_visited) == 2
