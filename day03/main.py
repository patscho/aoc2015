from santa import Santa

with open("day03/input.txt") as f:
    moves = f.readline().strip()


def part_1():
    santa = Santa()
    for move in moves:
        santa.move(move)
    print(f"Number of houses visited by Santa: {len(santa.houses_visited)}")


def part_2():
    santa = Santa()
    robo_santa = Santa()
    for i in range(0, len(moves), 2):
        santa.move(moves[i])
    for j in range(1, len(moves), 2):
        robo_santa.move(moves[j])
    all_houses = santa.houses_visited.union(robo_santa.houses_visited)
    print(f"Number of houses visited by Santa and Robo-Santa: {len(all_houses)}")


part_1()
part_2()
