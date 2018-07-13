import math

class Position(object):
    """
    Creates an object to hold a position in 3D space
    """
    def __init__(self, x = 0.0, y = 0.0, z = 0.0):
        self.x = x
        self.y = y
        self.z = z

    @property
    def magnitude(self):
        return math.sqrt(self.x*self.x + self.y*self.y + self.z*self.z)


    def calc_distance(self, point):
        return math.sqrt((point.x - self.x)**2 + (point.y - self.y)**2 + (point.z - self.z)**2)


    def dot_product(self, point_2):
        return self.x*point_2.x + self.y*point_2.y + self.z*point_2.z

    
    def cross_product(self, point_2):
        cp = Position()
        cp.x = self.y*point_2.z - self.z*point_2.y
        cp.y = self.z*point_2.x - self.x*point_2.z
        cp.z = self.x*point_2.y - self.y*point_2.x
        return cp


    def normalize(self):
        mag = self.magnitude
        if mag > 0:
            self.x /= mag
            self.y /= mag
            self.z /= mag
        return


    def divide_scalar(self, scale):
        result = Position()
        if scale != 0:
            result.x = self.x / scale
            result.y = self.y / scale
            result.z = self.z / scale
        return result


    def negate(self):
        result = Position()
        result.x = self.x * -1.0
        result.y = self.y * -1.0
        result.z = self.z * -1.0
        return result


    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(self, other.__class__):
            return self.x == other.x and self.y == other.y and self.z == other.z
        return False


    def __ne__(self, other):
        """Overrides the default implementation"""
        return not self.__eq__(other)


    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y, self.z + other.z)

    
    def __sub__(self, other):
        return Position(self.x - other.x, self.y - other.y, self.z - other.z)


    def __mul__(self, other):
        return Position(self.x * other, self.y * other, self.z * other)

    __rmul__ = __mul__
