import matrix, vector
class Shape:
    def __init__(self, points):
        self.points = matrix.PointMatrix(points)
        self.mp = self.getMidPoint()

    def rectangle(x, y, w, h):
        tl = vector.Vector(x, y)
        tr = vector.Vector(x + w, y)
        bl = vector.Vector(x, y + h)
        br = vector.Vector(x+h, y+w)
        return Shape([tl, bl, br, tr])

    def getMidPoint(self):
        x = y = 0
        for point in self.points.data:
            x = x + point.x
            y = y + point.y
        length = len(self.points.data)
        return vector.Vector(x / length, y / length)

    def transform(self, m):
        temp = self.points.translate(self.mp.multiply(-1))
        temp = temp.multiply(m)
        self.points = temp.translate(self.mp)

    def translate(self, vector):
        self.points = self.points.translate(vector)

    def rotate(self, angle):
        m = matrix.Matrix.rotationMatrix(angle)
        self.transform(m)

    def operate(self, matrix):
        self.points = self.points.multiply(matrix)

    def getPointPairs(self, offset):
        pairs = []
        for vector in self.points.data:
            pairs.append((vector[0] + offset.x, -vector[1] + offset.y))

        return pairs
