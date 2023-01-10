class Light:
    def __init__(self, position: tuple) -> None:
        self.status = 0
        self.position = position
        self.x, self.y = position[0], position[1]
        self.brightness = 0

    def increase_brightness(self, x: int):
        self.brightness += x

    def decrease_brightness(self, x: int):
        if self.brightness > 0:
            self.brightness -= x

    def turn_on(self):
        self.status = 1

    def turn_off(self):
        self.status = 0

    def toggle(self):
        if self.status == 0:
            self.status = 1
        else:
            self.status = 0


class Grid:
    def __init__(self, x: int):
        self.lights = self.init_grid(x)

    def init_grid(self, x: int) -> dict:
        lights = {}
        for i in range(x):
            for j in range(x):
                lights[(i, j)] = Light((i, j))
        return lights

    def turn_on(self, start: tuple, end: tuple):
        for i in range(start[0], end[0] + 1):
            for j in range(start[1], end[1] + 1):
                self.lights[(i, j)].turn_on()

    def turn_off(self, start: tuple, end: tuple):
        for i in range(start[0], end[0] + 1):
            for j in range(start[1], end[1] + 1):
                self.lights[(i, j)].turn_off()

    def toggle(self, start: tuple, end: tuple):
        for i in range(start[0], end[0] + 1):
            for j in range(start[1], end[1] + 1):
                self.lights[(i, j)].toggle()

    def number_of_lights_on(self):
        number = 0
        for light in self.lights:
            if self.lights[light].status:
                number += 1
        return number

    def brightness_plus_one(self, start: tuple, end: tuple):
        for i in range(start[0], end[0] + 1):
            for j in range(start[1], end[1] + 1):
                self.lights[(i, j)].increase_brightness(1)

    def brightness_minus_one(self, start: tuple, end: tuple):
        for i in range(start[0], end[0] + 1):
            for j in range(start[1], end[1] + 1):
                self.lights[(i, j)].decrease_brightness(1)

    def brightness_plus_two(self, start: tuple, end: tuple):
        for i in range(start[0], end[0] + 1):
            for j in range(start[1], end[1] + 1):
                self.lights[(i, j)].increase_brightness(2)

    def total_brightness(self):
        brightness = 0
        for light in self.lights:
            brightness += self.lights[light].brightness
        return brightness
