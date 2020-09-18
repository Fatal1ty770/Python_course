class Clothes:
    def __init__(self, v, h):
        self.v = v
        self.h = h


    def square_c(self, v):
        return self.v / 6.5 + 0.5


    def square_s(self, h):
        return (self.h  << 1  + 0.3)

    @property
    def full_square(self):
        return str(f'Площадь общая ткани \n'
                   f' {(self.v / 6.5 + 0.5) + ((self.h << 1) + 0.3)}')


class Coat(Clothes):
    def __init__(self, v, h):
        super().__init__(v, h)
        self.square_c = (self.v / 6.5 + 0.5)

    def __str__(self):
        return f'Ткани для пальто {self.square_c}'


class Suit(Clothes):
    def __init__(self, v, h):
        super().__init__(v, h)
        self.square_s = ((self.h << 1) + 0.3)

    def __str__(self):
        return f'Ткани для костюма {self.square_s}'


coat = Coat(3, 6)
suit = Suit(6, 4)
print(coat)
print(suit)
print(coat.full_square)

