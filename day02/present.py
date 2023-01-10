class Present:
    def __init__(self, l: int, w: int, h: int) -> None:
        self.height = h
        self.length = l
        self.width = w

    def paper_needed(self):
        surface_area = (
            (2 * self.height * self.width)
            + (2 * self.length * self.width)
            + (2 * self.height * self.length)
        )
        small_1, small_2 = self.smallest_sides()
        smallest_area = small_1 * small_2
        return surface_area + smallest_area

    def smallest_sides(self):
        sides = [self.height, self.width, self.length]
        sides.sort()
        return sides[0], sides[1]

    def volume(self):
        return self.height * self.width * self.length

    def ribbon_needed(self):
        small_1, small_2 = self.smallest_sides()
        perimeter = small_1 + small_1 + small_2 + small_2
        volume = self.volume()
        return perimeter + volume
