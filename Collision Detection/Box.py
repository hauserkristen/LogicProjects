from Position import Position

class Box(object):
    def __init__(self, center, x_axis, y_axis, z_axis, extent_x, extent_y, extent_z):
        self.center = center

        self.axes = [] #Position
        self.axes.append(x_axis)
        self.axes.append(y_axis)
        self.axes.append(z_axis)

        self.extent = [] #float
        self.extent.append(extent_x / 2.0)
        self.extent.append(extent_y / 2.0)
        self.extent.append(extent_z / 2.0)

    def compute_vertices(self):
        ext_axis_x = self.axes[0] * self.extent[0]
        ext_axis_y = self.axes[1] * self.extent[1]
        ext_axis_z = self.axes[2] * self.extent[2]

        vertices = []
        vertices.append(self.center - ext_axis_x - ext_axis_y - ext_axis_z)
        vertices.append(self.center + ext_axis_x - ext_axis_y - ext_axis_z)
        vertices.append(self.center + ext_axis_x + ext_axis_y - ext_axis_z)
        vertices.append(self.center - ext_axis_x + ext_axis_y - ext_axis_z)
        vertices.append(self.center - ext_axis_x - ext_axis_y + ext_axis_z)
        vertices.append(self.center + ext_axis_x - ext_axis_y + ext_axis_z)
        vertices.append(self.center + ext_axis_x + ext_axis_y + ext_axis_z)
        vertices.append(self.center - ext_axis_x + ext_axis_y + ext_axis_z)
        
        return vertices
