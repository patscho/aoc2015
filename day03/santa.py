class Santa:
    def __init__(self) -> None:
        self.position = (0, 0)
        self.houses_visited = set()
        self.houses_visited.add(self.position)

    def move(self, dir: str):
        if dir == ">":
            self.position = (self.position[0] + 1, self.position[1])
        elif dir == "<":
            self.position = (self.position[0] - 1, self.position[1])
        elif dir == "^":
            self.position = (self.position[0], self.position[1] + 1)
        elif dir == "v":
            self.position = (self.position[0], self.position[1] - 1)
        self.houses_visited.add(self.position)
