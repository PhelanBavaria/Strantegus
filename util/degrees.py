

class Degrees:
    def __init__(self, amount=0):
        self.amount = amount

    def __check(self, amount):
        amount = amount % 360
        if amount < 0:
            amount = 360 + amount
        return amount

    def __add__(self, other):
        return self.__check(self.amount + other)

    def __iadd__(self, other):
        self.amount = self.__check(self.amount + other)
        return self

    def __sub__(self, other):
        return self.__check(self.amount - other)

    def __isub__(self, other):
        self.amount = self.__check(self.amount - other)
        return self

    def __str__(self):
        return str(self.amount) + ' degrees'

    def __repr__(self):
        return str(self.amount) + ' degrees'

    def __int__(self):
        return self.amount


if __name__ == '__main__':
    d = Degrees()
    d += 340
    print(d, '== 340')
    d += 50
    print(d, '== 30')
    d -= 60
    print(d, '== 330')
    d -= 340
    print(d, '== 350')
    a = d + 10
    print(a, '== 0 ', d, '== 350')
    a = d - 10
    print(a, '== 340 ', d, '== 350')

    dictionary = {180: 'Hello'}
    i = Degrees(180)
    print(dictionary[int(i)])
