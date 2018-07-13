from Position import Position

class Node(object):
    """Holds bounding box of object that moves from start position to end position"""

    def __init__(self, start, end, length, width, height):
        self.start = start
        self.end = end
        self.length = length
        self.width = width
        self.height = height


    @property
    def orientation(self):
        orientation = self.start - self.end
        orientation.normalize()
        return orientation


    def calc_velocity(self, time_step):
        velocity = Position()
        velocity.x = (self.end.x - self.start.x) / time_step
        velocity.y = (self.end.y - self.start.y) / time_step
        velocity.z = (self.end.z - self.start.z) / time_step
        return velocity
