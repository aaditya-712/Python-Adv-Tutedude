class const_dest:
    x = 0

    def __init__(self, color, type):
        self.color = color
        self.type = type
        print("Constructor Called")

    def __del__(self):
        print("Destructor Called")

cd = const_dest("Black", "SUV")
print(cd.color)
print(cd.type)

cd1 = const_dest("White", "Sedan")
print(cd1.color)
print(cd1.type)
