import pytest
from main import what_floor, in_basement

STRING1 = "(()(()("
STRING2 = "())"
STRING3 = ")"
STRING4 = "()())"


def test_what_floor_1():
    floor = what_floor(STRING1)
    assert floor == 3


def test_what_floor_2():
    floor = what_floor(STRING2)
    assert floor == -1


def test_in_basement_1():
    position = in_basement(STRING3)
    assert position == 1


def test_in_basement_2():
    position = in_basement(STRING4)
    assert position == 5
