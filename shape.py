import matrix, vector
class Shape:
    def __init__(self, points):
        self.points = matrix.PointMatrix(points)

    def rectangle(x, y, w, h):
        tl = vector.Vector(x, y)
        tr = vector.Vector(x + w, y)
        bl = vector.Vector(x, y + h)
        br = vector.Vector(x+h, y+w)
        return Shape([tl, bl, br, tr])



    def translate(self, vector):
        self.points.translate(vector)
    def operate(self, matrix):
        self.points.multiply(matrix)

    def getPointPairs(self, offset):
        pairs = []
        for vector in self.points.data:
            pairs.append((vector[0] + offset.x, -vector[1] + offset.y))

        return pairs
