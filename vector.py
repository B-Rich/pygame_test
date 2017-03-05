import math

class Vector:
    def __init__(self):
        self.x = self.y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def multiply(self, Matrix):
        x = self.x * Matrix[0] + self.y * Matrix[1]
        y = self.x * Matrix[2] + self.y * Matrix[3]

        return Vector(x, y)
    def add(self, v):
        return Vector(self.x + v.x, self.y + v.y)

    def __getitem__(self, i):
        if i == 0:
            return self.x
        else:
            return self.y



    def __str__(self):
        return str(self.x) + "i + " + str(self.y) + "j"
