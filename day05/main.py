import re


def check_three_vowels(string: str):
    counter = 0
    vowels = ["a", "e", "i", "o", "u"]
    for char in vowels:
        counter += string.count(char)
    if counter >= 3:
        return True
    else:
        return False


def check_doubles(string: str):
    for letter in string:
        if letter + letter in string:
            return True
    return False


def check_naughty_combo(string: str):
    naughty_combos = ["ab", "cd", "pq", "xy"]
    for combo in naughty_combos:
        if combo in string:
            return True
    return False


def check_any_two_twice(string: str):
    for i in range(len(string) - 1):
        substring = string[i : i + 2]
        if string.count(substring) > 1:
            return True
    return False


def check_repeat_with_one_in_between(string: str):
    for i in range(len(string) - 2):
        if string[i] == string[i + 2]:
            return True
    return False


# def is_nice_part_1():
#     nice = 0
#     for s in strings:
#         if check_three_vowels(s) and check_doubles(s) and not check_naughty_combo(s):
#             nice += 1
#     return nice


def is_nice_part_2():
    nice = 0
    for s in strings:
        if is_nice_part_two(s):
            nice += 1
    return nice


def is_nice_part_two(s):
    return check_any_two_twice(s) and check_repeat_with_one_in_between(s)


with open("input.txt") as f:
    strings = [string.strip() for string in f.readlines()]

# nice = is_nice_part_1()
# print(f"Part 1: There are {nice} nice strings.")

nice = is_nice_part_2()
print(f"Part 2: There are {nice} nice strings.")
