FILE = "/Users/ho36us/Dev/aoc2015/day01/input.txt"


def read_input_file(file):
    with open(FILE) as file:
        brackets = file.read()
    return brackets


def what_floor(brackets):
    opening_brackets = brackets.count("(")
    closing_brackets = brackets.count(")")
    floor = opening_brackets - closing_brackets
    return floor


def in_basement(brackets: str) -> int:
    pos = 1
    for i in range(pos, len(brackets) + 1):
        slice = brackets[:i]
        if what_floor(slice) == -1:
            pos = i
            break
        pos = i
    return pos


brackets = read_input_file(FILE)
print(what_floor(brackets))
print(in_basement(brackets))
