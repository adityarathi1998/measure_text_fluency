import itertools

# Defines a Cartesian point
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return '(%d, %d)'%(self.x, self.y)
    # Calculate the cross product with another point
    def cross_product(self, point):
        return self.x * point.y - self.y * point.x
    # Subtract a point from itself
    def subtract(self, point):
        return Point(self.x - point.x, self.y - point.y)
    # Check if two points have the same values
    def equals(self, point):
        return self.x == point.x and self.y == point.y

# Defines a Cartesian line segment made of two Points.
class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
    def __repr__(self):
        return '<%s, %s>'%(self.point1, self.point2)
    # Intersection of two line segments
    def intersects(self, line):
        # Get the difference between the points on each line
        r = self.point2.subtract(self.point1)
        s = line.point2.subtract(line.point1)

        numerator = line.point1.subtract(self.point1).cross_product(r)
        denominator = r.cross_product(s)

        # Check if lines are collinear
        if numerator == 0 and denominator == 0:
            # Check if any of the endpoints are equal
            if self.point1.equals(line.point1) or self.point1.equals(line.point2) or \
                    self.point2.equals(line.point1) or self.point2.equals(line.point2):
                return True
            x_check = [line.point1.x - self.point1.x < 0,
                       line.point1.x - self.point2.x < 0,
                       line.point2.x - self.point1.x < 0,
                       line.point2.x - self.point2.x < 0]
            y_check = [line.point1.y - self.point1.y < 0,
                       line.point1.y - self.point2.y < 0,
                       line.point2.y - self.point1.y < 0,
                       line.point2.y - self.point2.y < 0]

            return not (all(x_check) or all([not e for e in x_check])) or \
                    not (all(y_check) or all([not e for e in y_check]))
        # Check if lines are parallel
        elif denominator == 0:
            return False

        u = numerator / denominator
        t = line.point1.subtract(self.point1).cross_product(s) / denominator

        return t >= 0 and t <= 1 and u >= 0 and u <= 1

# Count the number of intersections between a list of Lines with each other
def count_intersections(lines):
    return sum([1 for line1, line2 in itertools.combinations(lines, 2) if line1.intersects(line2)])
