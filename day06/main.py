from light import Grid

FILE = "day06/input.txt"

grid = Grid(1000)
with open(FILE) as f:
    instructions = [item.strip() for item in f.readlines()]


def part_1():
    for i in instructions:
        do_this = i.split()
        if len(do_this) == 5:
            start = tuple(map(int, do_this[2].split(",")))
            end = tuple(map(int, do_this[4].split(",")))
            if do_this[1] == "on":
                grid.turn_on(start, end)
            else:
                grid.turn_off(start, end)
        elif len(do_this) == 4:
            start = tuple(map(int, do_this[1].split(",")))
            end = tuple(map(int, do_this[3].split(",")))
            grid.toggle(start, end)

    print(grid.number_of_lights_on())


def part_2():
    for i in instructions:
        do_this = i.split()
        if len(do_this) == 5:
            start = tuple(map(int, do_this[2].split(",")))
            end = tuple(map(int, do_this[4].split(",")))
            if do_this[1] == "on":
                grid.brightness_plus_one(start, end)
            else:
                grid.brightness_minus_one(start, end)
        elif len(do_this) == 4:
            start = tuple(map(int, do_this[1].split(",")))
            end = tuple(map(int, do_this[3].split(",")))
            grid.brightness_plus_two(start, end)
    print(grid.total_brightness())


part_2()
