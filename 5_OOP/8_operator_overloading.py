# a = 1
# b = 2
# print(a + b)
# print(int.__add__(a, b))

class Vegetables:
    def __init__(self, carrot, beans):
        self.carrot = carrot
        self.beans = beans

    def __add__(self, other):
        carrot = self.carrot + other.carrot
        beans = self.beans + other.beans
        return Vegetables(carrot, beans)


v1 = Vegetables(5, 7)
v2 = Vegetables(3, 4)
v3 = v1 + v2
print(v3.carrot)
print(v3.beans)
