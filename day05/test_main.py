import pytest
from main import (
    check_three_vowels,
    check_doubles,
    check_naughty_combo,
    check_any_two_twice,
    check_repeat_with_one_in_between,
    is_nice_part_two,
)


def test_check_three_vowels():
    string = "ugknbfddgicrmopn"
    assert check_three_vowels(string) == True


def test_check_doubles():
    string = "ugknbfddgicrmopn"
    assert check_doubles(string) == True


def test_check_naughty_combo():
    string = "haegwjzuvuyypxyu"
    assert check_naughty_combo(string) == True


def test_check_any_two_twice_1():
    string = "qjhvhtzxzqqjkmpb"
    assert check_any_two_twice(string) == True


def test_check_any_two_twice_2():
    string = "aaa"
    assert check_any_two_twice(string) == False


def test_check_repeat_with_one_in_between_1():
    string = "qjhvhtzxzqqjkmpb"
    assert check_repeat_with_one_in_between(string) == True


def test_check_repeat_with_one_in_between_2():
    string = "aaaaaaaaaaa"
    assert check_repeat_with_one_in_between(string) == True


def test_is_nice_part_two_1():
    string = "qjhvhtzxzqqjkmpb"
    assert is_nice_part_two(string) == True


def test_is_nice_part_two_2():
    string = "xxyxx"
    assert is_nice_part_two(string) == True


def test_is_nice_part_two_3():
    string = "uurcxstgmygtbstg"
    assert is_nice_part_two(string) == False


def test_is_nice_part_two_4():
    string = "ieodomkazucvgmuy"
    assert is_nice_part_two(string) == False
