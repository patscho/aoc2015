import pytest
from present import Present


def test_paper_needed_1():
    present = Present(2, 3, 4)
    paper = present.paper_needed()
    assert paper == 58


def test_paper_needed_2():
    present = Present(1, 1, 10)
    paper = present.paper_needed()
    assert paper == 43


def test_volume_1():
    present = Present(2, 3, 4)
    assert present.volume() == 24


def test_volume_2():
    present = Present(1, 1, 10)
    assert present.volume() == 10


def test_smallest_sides_1():
    present = Present(2, 3, 4)
    small_1, small_2 = present.smallest_sides()
    assert small_1 == 2 and small_2 == 3


def test_smallest_sides_2():
    present = Present(1, 1, 10)
    small_1, small_2 = present.smallest_sides()
    assert small_1 == 1 and small_2 == 1


def test_ribbon_needed_1():
    present = Present(2, 3, 4)
    assert present.ribbon_needed() == 34


def test_ribbon_needed_2():
    present = Present(1, 1, 10)
    assert present.ribbon_needed() == 14
