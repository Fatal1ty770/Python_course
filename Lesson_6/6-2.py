class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width


    def raschet(self, mass1, tolsh):
        print(self._width * self._length * mass1 * tolsh)

road1 = Road(1000, 10)

road1.raschet(10, 5)