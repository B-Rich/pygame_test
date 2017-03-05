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
        if len(self.points.data) <= 0:
            return 0
        min_x = max_x = self.points[0].x
        min_y = max_y = self.points[0].y

        for point in self.points.data:
            if point.x > max_x:
                max_x = point.x
            if point.y > max_y:
                max_y = point.y
            if point.x < min_x:
                min_x = point.x
            if point.y < min_y:
                min_y = point.y

        return vector.Vector((min_x + max_x) / 2, (max_y + min_y) / 2)


    def transform(self, m):
        temp = self.points.translate(self.mp.multiply(-1))
        temp = temp.multiply(m)
        self.points = temp.translate(self.mp)

    def translate(self, vector):
        self.points = self.points.translate(vector)
        self.mp = self.mp.add(vector)


    def rotate(self, angle, point=0):
        if point == 0:
            point = self.mp
        temp = self.points.translate(point.multiply(-1))
        temp = temp.multiply(matrix.Matrix.rotationMatrix(angle))
        self.points = temp.translate(point)

    def operate(self, matrix):
        self.points = self.points.multiply(matrix)

    def getPointPairs(self, offset):
        pairs = []
        for vector in self.points.data:
            pairs.append((vector[0] + offset[0], -vector[1] + offset[1]))

        return pairs
    def mp_pair(self, offset):
        return (int(self.mp[0] + offset[0]), int(-self.mp[1] + offset[1]))
