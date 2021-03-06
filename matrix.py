import math

class Matrix:
    def __init__(self):
        self.data = [
                     0, 0,
                     0, 0
                    ]
    def identityMatrix():
        m = Matrix()
        m.data = [1, 0, 0, 1]
        return m

    def rotationMatrix(angle):
        m = Matrix()
        m.data = [
                   math.cos(angle), -math.sin(angle),
                   math.sin(angle),  math.cos(angle)
                 ]
        return m

    def __getitem__(self, i):
        return self.data[i]


class PointMatrix:
    def __init__(self, points):
        self.data = points

    def multiply(self, m):
        data = []
        for point in self.data:
            data.append(point.multiply(m))

        return PointMatrix(data)

    def __getitem__(self, index):
        return self.data[index]

    def translate(self, v):
        data = []
        for point in self.data:
            data.append(point.add(v))
        return PointMatrix(data)
