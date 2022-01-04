from random import randint

color_dict = {
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46)
}


class Block:
    def __init__(self):
        self.value = 2 if randint(1, 10) < 7 else 4
        self.color = color_dict[self.value]
        self.size = 100

    def update(self):
        self.color = color_dict[self.value]

    def __repr__(self):
        return str(self.value)
