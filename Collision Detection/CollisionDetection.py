from Position import Position
from Box import Box
from BoxBoxCollision import BoxBoxCollision

class CollisionDetection(object):

    @staticmethod
    def check_for_collision(node_a, node_b):
        #Axes
        (x_axis_a, y_axis_a, z_axis_a) = CollisionDetection.find_orthnormal_axes(node_a.orientation)
        (x_axis_b, y_axis_b, z_axis_b) = CollisionDetection.find_orthnormal_axes(node_b.orientation)

        #Centers
        center_a = CollisionDetection.find_center(node_a.start, node_a.end)
        center_b = CollisionDetection.find_center(node_b.start, node_b.end)

        #Boxes
        box_a = Box(center_a, x_axis_a, y_axis_a, z_axis_a, node_a.length, node_a.width, node_a.height)
        box_b = Box(center_b, x_axis_b, y_axis_b, z_axis_b, node_b.length, node_b.width, node_b.height)

        collision = BoxBoxCollision(box_a, box_b)

        return collision.static_box_test()


    @staticmethod
    def check_for_collision_velocity(node_a, node_b, time_step):

        #Axes
        (x_axis_a, y_axis_a, z_axis_a) = CollisionDetection.find_orthnormal_axes(node_a.orientation)
        (x_axis_b, y_axis_b, z_axis_b) = CollisionDetection.find_orthnormal_axes(node_b.orientation)

        #Boxes
        box_a = Box(node_a.start, x_axis_a, y_axis_a, z_axis_a, node_a.length, node_a.width, node_a.height)
        box_b = Box(node_b.start, x_axis_b, y_axis_b, z_axis_b, node_b.length, node_b.width, node_b.height)

        #Velocities
        velocity_a = node_a.calc_velocity(time_step)
        velocity_b = node_b.calc_velocity(time_step)

        #Time
        t_max = time_step

        collision = BoxBoxCollision(box_a, box_b)

        return collision.linear_box_test(t_max, velocity_a, velocity_b)

    
    @staticmethod
    def find_orthnormal_basis_1_vec(base_1):
        """
        Construct orthnormal basis based on https://www.geometrictools.com/Documentation/OrthonormalSets.pdf
        """
        base_1.normalize()

        #Construct the second basis
        base_2 = Position()
        abs_vals = [abs(base_1.x), abs(base_1.y),  abs(base_1.z)]
        if max(abs_vals) == abs(base_1.x):
            base_2.x = base_1.y
            base_2.y = -base_1.x
            base_2.z = 0.0
            base_2.normalize()
        elif max(abs_vals) == abs(base_1.y):
            base_2.x = 0.0
            base_2.y = base_1.z
            base_2.z = -base_1.y
            base_2.normalize()
        elif max(abs_vals) == abs(base_1.z):
            base_2.x = -base_1.z
            base_2.y = 0.0
            base_2.z = base_1.x
            base_2.normalize()

        base_3 = base_1.cross_product(base_2)
        base_3.normalize()
        
        return (base_1, base_2, base_3)

    
    @staticmethod
    def find_orthnormal_basis_2_vec(base_1, base_2):
        """
        Construct orthnormal basis based on https://www.geometrictools.com/Documentation/OrthonormalSets.pdf
        """
        base_1.normalize()
        base_2.normalize()
        base_3 = base_1.cross_product(base_2)
        
        return (base_1, base_2, base_3)

    
    @staticmethod
    def find_orthnormal_axes(orientation):
        x_axis = Position()
        y_axis = Position()
        z_axis = Position()

        #If no position change, use default axis
        set_x = False
        set_y = False
        set_z = False
        if orientation.x == 0.0:
            x_axis = Position(1.0,0,0)
            set_x = True
        
        if orientation.y == 0.0:
            y_axis = Position(0,1.0,0)
            set_y = True

        if orientation.z == 0.0:
            z_axis = Position(0,0,1.0)
            set_z = True

        #If two axes are already set, default third as well
        axes_set = [set_x, set_y, set_z]
        if sum(axes_set) == 2:
            if set_x and set_y:
                z_axis = Position(0,0,1.0)
            elif set_x and set_z:
                y_axis = Position(0,1.0,0)
            elif set_y and set_z:
                x_axis = Position(1.0,0,0)
            else:
                raise TypeError('Unknown set combination')
        #Find orthonormal basis, based on one known axis
        elif sum(axes_set) == 1:
            if set_x and orientation.dot_product(x_axis) == 0.0:
                return CollisionDetection.find_orthnormal_basis_2_vec(orientation, x_axis)
            elif set_y and orientation.dot_product(x_axis) == 0.0:
                return CollisionDetection.find_orthnormal_basis_2_vec(orientation, y_axis)
            elif set_z and orientation.dot_product(x_axis) == 0.0:
                return CollisionDetection.find_orthnormal_basis_2_vec(orientation, z_axis)
            else:
                return CollisionDetection.find_orthnormal_basis_1_vec(orientation)
        #Find orthnormal basis based on no known axis
        elif sum(axes_set) == 0:
            return CollisionDetection.find_orthnormal_basis_1_vec(orientation)

        return (x_axis, y_axis, z_axis)


    @staticmethod
    def find_center(start, end):
        center = Position()
        center.x = (start.x + end.x) / 2.0
        center.y = (start.y + end.y) / 2.0
        center.z = (start.z + end.z) / 2.0

        return center
