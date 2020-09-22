from random import randint


class LotoGame:
    def __init__(self, p1, p2):
        pass

    def start(self):
        y = 0
        while y < 20:
            y +=1

            nomer = randint(1,91)
            print(nomer)
            kart = ' '.join([str(elem) for elem in p1.nums])
            print(kart)
            kart1 = kart[0:9] + '\n' + kart[10:19] + '\n' + kart[20:]
            print(kart1)
            if nomer in p1.nums:
                print('inside!!!!!!!!!!')
                pos = p1.nums.index(nomer)
                p1.nums.remove(nomer)
                p1.nums.insert(pos, '-')


            else:
                print('not in')


class LotoCard:
    def __init__(self):
        self.nums = a = []
        for i in range(15):
            b = randint(1,91)
            a.append(b)

    def __str__(self):
        return ' '.join([str(elem) for elem in p1.nums])


p1 = LotoCard()
p2 = LotoCard()

print(p1)
# print(p2)

Loto = LotoGame(p1, p2)
Loto.start()

