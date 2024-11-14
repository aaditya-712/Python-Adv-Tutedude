class simple:

    def __init__(self):
        self.value_1 = 1
        self.value_2 = 2

    def _A1_(self):
        print("Apple")

    def __B2_(self):
        print("Banana")

s = simple()
print(s.value_1)
s._A1_()
s._simple__B2_()
print(dir(s))