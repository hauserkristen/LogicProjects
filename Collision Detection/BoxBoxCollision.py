import sys
from Utils import create_2D_matrix, create_vector

class BoxBoxCollision(object):
    def __init__(self,  box_a, box_b):
        self.box_a = box_a
        self.box_b = box_b
        self.quantity = 0
        self.zero_tolerance = 1e-6
        self.contact_time = 0.0


    def static_box_test(self):
        """
        Static test-intersection query.
        """ 
        #Checking for parallel axes
        cutoff = 1 - self.zero_tolerance
        existsParallelPair = False

        #Local variables
        A = self.box_a.axes
        B = self.box_b.axes
        EA = self.box_a.extent
        EB = self.box_b.extent
        C = create_2D_matrix(3,3)       #matrix C = A^T B, c_j = dot_product(A_i,B_j)
        AbsC = create_2D_matrix(3,3)    #|c_ij|
        AD = create_vector(3)           #dot_product(A_i,D)
        r0 = 0.0
        r1 = 0.0
        r = 0.0                         #interval radii and distance between centers
        r01 = 0.0                       #= R0 + R1

        #Compute difference between centers of boxes
        D = self.box_b.center - self.box_a.center

        #Go through all axes pairs, check for parallel axes then check if axes touch or cross

        #Axis C0+t*A0
        for i in xrange(0,3):
            C[0][i] = A[0].dot_product(B[i])
            AbsC[0][i] = abs(C[0][i])
            if AbsC[0][i] > cutoff:
                existsParallelPair = True
            
        
        AD[0] = A[0].dot_product(D)
        r = abs(AD[0])
        r1 = EB[0]*AbsC[0][0] + EB[1]*AbsC[0][1] + EB[2]*AbsC[0][2]
        r01 = EA[0] + r1
        if r > r01:
            return False
        

        #Axis C0+t*A1
        for i in xrange(0,3):
            C[1][i] = A[1].dot_product(B[i])
            AbsC[1][i] = abs(C[1][i])
            if AbsC[1][i] > cutoff:
                existsParallelPair = True
            
        
        AD[1] = A[1].dot_product(D)
        r = abs(AD[1])
        r1 = EB[0]*AbsC[1][0] + EB[1]*AbsC[1][1] + EB[2]*AbsC[1][2]
        r01 = EA[1] + r1
        if r > r01:
            return False
        

        #Axis C0+t*A2
        for i in xrange(0,3):
            C[2][i] = A[2].dot_product(B[i])
            AbsC[2][i] = abs(C[2][i])
            if AbsC[2][i] > cutoff:
                existsParallelPair = True
            
        
        AD[2] = A[2].dot_product(D)
        r = abs(AD[2])
        r1 = EB[0]*AbsC[2][0] + EB[1]*AbsC[2][1] + EB[2]*AbsC[2][2]
        r01 = EA[2] + r1
        if r > r01:
            return False
        

        #Axis C0+t*B0
        r = abs(B[0].dot_product(D))
        r0 = EA[0]*AbsC[0][0] + EA[1]*AbsC[1][0] + EA[2]*AbsC[2][0]
        r01 = r0 + EB[0]
        if r > r01:
            return False
        

        #Axis C0+t*B1
        r = abs(B[1].dot_product(D))
        r0 = EA[0]*AbsC[0][1] + EA[1]*AbsC[1][1] + EA[2]*AbsC[2][1]
        r01 = r0 + EB[1]
        if r > r01:
            return False
        

        #Axis C0+t*B2
        r = abs(B[2].dot_product(D))
        r0 = EA[0]*AbsC[0][2] + EA[1]*AbsC[1][2] + EA[2]*AbsC[2][2]
        r01 = r0 + EB[2]
        if r > r01:
            return False
        

        #At least one pair of box axes was parallel is sufficient for the separation of the boxes.
        if existsParallelPair:
            return True
        

        #Axis C0+t*A0xB0
        r = abs(AD[2]*C[1][0] - AD[1]*C[2][0])
        r0 = EA[1]*AbsC[2][0] + EA[2]*AbsC[1][0]
        r1 = EB[1]*AbsC[0][2] + EB[2]*AbsC[0][1]
        r01 = r0 + r1
        if r > r01:
            return False
        

        #Axis C0+t*A0xB1
        r = abs(AD[2]*C[1][1] - AD[1]*C[2][1])
        r0 = EA[1]*AbsC[2][1] + EA[2]*AbsC[1][1]
        r1 = EB[0]*AbsC[0][2] + EB[2]*AbsC[0][0]
        r01 = r0 + r1
        if r > r01:
            return False
        

        #Axis C0+t*A0xB2
        r = abs(AD[2]*C[1][2] - AD[1]*C[2][2])
        r0 = EA[1]*AbsC[2][2] + EA[2]*AbsC[1][2]
        r1 = EB[0]*AbsC[0][1] + EB[1]*AbsC[0][0]
        r01 = r0 + r1
        if r > r01:
            return False
        

        #Axis C0+t*A1xB0
        r = abs(AD[0]*C[2][0] - AD[2]*C[0][0])
        r0 = EA[0]*AbsC[2][0] + EA[2]*AbsC[0][0]
        r1 = EB[1]*AbsC[1][2] + EB[2]*AbsC[1][1]
        r01 = r0 + r1
        if r > r01:
            return False
        

        #Axis C0+t*A1xB1
        r = abs(AD[0]*C[2][1] - AD[2]*C[0][1])
        r0 = EA[0]*AbsC[2][1] + EA[2]*AbsC[0][1]
        r1 = EB[0]*AbsC[1][2] + EB[2]*AbsC[1][0]
        r01 = r0 + r1
        if r > r01:
            return False
        

        #Axis C0+t*A1xB2
        r = abs(AD[0]*C[2][2] - AD[2]*C[0][2])
        r0 = EA[0]*AbsC[2][2] + EA[2]*AbsC[0][2]
        r1 = EB[0]*AbsC[1][1] + EB[1]*AbsC[1][0]
        r01 = r0 + r1
        if r > r01:
            return False
        

        #Axis C0+t*A2xB0
        r = abs(AD[1]*C[0][0] - AD[0]*C[1][0])
        r0 = EA[0]*AbsC[1][0] + EA[1]*AbsC[0][0]
        r1 = EB[1]*AbsC[2][2] + EB[2]*AbsC[2][1]
        r01 = r0 + r1
        if r > r01:
            return False
        

        #Axis C0+t*A2xB1
        r = abs(AD[1]*C[0][1] - AD[0]*C[1][1])
        r0 = EA[0]*AbsC[1][1] + EA[1]*AbsC[0][1]
        r1 = EB[0]*AbsC[2][2] + EB[2]*AbsC[2][0]
        r01 = r0 + r1
        if r > r01:
            return False
        

        #Axis C0+t*A2xB2
        r = abs(AD[1]*C[0][2] - AD[0]*C[1][2])
        r0 = EA[0]*AbsC[1][2] + EA[1]*AbsC[0][2]
        r1 = EB[0]*AbsC[2][1] + EB[1]*AbsC[2][0]
        r01 = r0 + r1
        if r > r01:
            return False
        

        return True


    def is_seperated(self, min_a, max_a, min_b, max_b, speed, t_max, t_last):
        invSpeed = 0.0
        t = 0.0

        #Box b initially on left of box a
        if max_b < min_a: 
            if speed <= 0.0:
                return True
            
            invSpeed = 1.0 / speed

            t = (min_a - max_b)*invSpeed
            if t > self.contact_time:
                self.contact_time = t
            
            if self.contact_time > t_max:
                return True
            
            t = (max_a - min_b)*invSpeed
            if t < t_last:
                t_last = t
            
            if self.contact_time > t_last:
                return True
            
        #Box b initially on right of box a
        elif max_a < min_b: 
        
            if speed >= 0.0:
                return True
            
            invSpeed = 1.0/speed

            t = (max_a - min_b)*invSpeed
            if t > self.contact_time:
                self.contact_time = t
            
            if self.contact_time > t_max:
                return True
            
            t = (min_a - max_b)*invSpeed
            if t < t_last:
                t_last = t
            
            if self.contact_time > t_last:

                return True
            
        #Boxes intially overlap
        else: 
        
            if speed > 0.0:
                t = (max_a - min_b)/speed
                if t < t_last:
                    t_last = t

                if self.contact_time > t_last:
                    return True
                
            elif speed < 0.0:
            
                t = (min_a - max_b)/speed
                if t < t_last:
                    t_last = t
                
                if self.contact_time > t_last:
                    return True

        return False


    def linear_box_test(self, t_max, velocity_a, velocity_b):
        """
        The first time of contact (if any) is computed.
        """
        #Check if box initial position overlap, if so the collision was recorded last time step
        if self.static_box_test():
            return False

        #If boxes are moving at the same velocity, then its equivalent to static boxes
        if velocity_a == velocity_b:
            if self.static_box_test():
                self.contact_time = 0.0
                return True
            return False
        

        #Checking for parallel axes
        cutoff = 1 - self.zero_tolerance
        existsParallelPair = False

        #Local variables
        A = self.box_a.axes
        B = self.box_b.axes
        EA = self.box_a.extent
        EB = self.box_b.extent
        C = create_2D_matrix(3,3)       #matrix C = A^T B, c_j = dot_product(A_i,B_j)
        AbsC = create_2D_matrix(3,3)    #|c_ij|
        AD = create_vector(3)           #dot_product(A_i,D)
        AW = create_vector(3)           #dot_product(A_i,W)
        min0 = 0.0
        max0 = 0.0
        min1 = 0.0
        max1 = 0.0
        center = 0.0
        radius = 0.0
        speed = 0.0
        tlast = sys.float_info.max

        #Set contact time
        self.contact_time = 0.0
        
        #Compute difference between centers of boxes
        D = self.box_b.center - self.box_a.center

        #Compute difference of box velocities
        W = velocity_a - velocity_b

        #Axes C0+t*A[i]
        for i in xrange(0,3):
            for j in xrange(0,3):    
                C[i][j] = A[i].dot_product(B[j])
                AbsC[i][j] = abs(C[i][j])
                if AbsC[i][j] > cutoff:
                    existsParallelPair = True
                
            
            AD[i] = A[i].dot_product(D)
            AW[i] = A[i].dot_product(W)
            min0 = -EA[i]
            max0 = +EA[i]
            radius = EB[0]*AbsC[i][0] + EB[1]*AbsC[i][1] + EB[2]*AbsC[i][2]
            min1 = AD[i] - radius
            max1 = AD[i] + radius
            speed = AW[i]
            if self.is_seperated(min0, max0, min1, max1, speed, t_max, tlast):
                return False
            
        

        #Axes C0+t*B[i]
        for i in xrange(0,3):
            radius = EA[0]*AbsC[0][i] + EA[1]*AbsC[1][i] + EA[2]*AbsC[2][i]
            min0 = -radius
            max0 = +radius
            center = B[i].dot_product(D)
            min1 = center - EB[i]
            max1 = center + EB[i]
            speed = W.dot_product(B[i])
            if self.is_seperated(min0, max0, min1, max1, speed, t_max, tlast):
                return False
            
        
        #At least one pair of box axes was parallel, so the separation is
        #effectively in 2D where checking the "edge" normals is sufficient for
        #the separation of the boxes.
        if existsParallelPair:
            return True
        
        #Axis C0+t*A0xB0
        radius = EA[1]*AbsC[2][0] + EA[2]*AbsC[1][0]
        min0 = -radius
        max0 = +radius
        center = AD[2]*C[1][0] - AD[1]*C[2][0]
        radius = EB[1]*AbsC[0][2] + EB[2]*AbsC[0][1]
        min1 = center - radius
        max1 = center + radius
        speed = AW[2]*C[1][0] - AW[1]*C[2][0]
        if self.is_seperated(min0, max0, min1, max1, speed, t_max, tlast):
            return False
        
        #Axis C0+t*A0xB1
        radius = EA[1]*AbsC[2][1] + EA[2]*AbsC[1][1]
        min0 = -radius
        max0 = +radius
        center = AD[2]*C[1][1] - AD[1]*C[2][1]
        radius = EB[0]*AbsC[0][2] + EB[2]*AbsC[0][0]
        min1 = center - radius
        max1 = center + radius
        speed = AW[2]*C[1][1] - AW[1]*C[2][1]
        if self.is_seperated(min0, max0, min1, max1, speed, t_max, tlast):
            return False
        
        #Axis C0+t*A0xB2
        radius = EA[1]*AbsC[2][2] + EA[2]*AbsC[1][2]
        min0 = -radius
        max0 = +radius
        center = AD[2]*C[1][2] - AD[1]*C[2][2]
        radius = EB[0]*AbsC[0][1] + EB[1]*AbsC[0][0]
        min1 = center - radius
        max1 = center + radius
        speed = AW[2]*C[1][2] - AW[1]*C[2][2]
        if self.is_seperated(min0, max0, min1, max1, speed, t_max, tlast):
            return False
        
        #Axis C0+t*A1xB0
        radius = EA[0]*AbsC[2][0] + EA[2]*AbsC[0][0]
        min0 = -radius
        max0 = +radius
        center = AD[0]*C[2][0] - AD[2]*C[0][0]
        radius = EB[1]*AbsC[1][2] + EB[2]*AbsC[1][1]
        min1 = center - radius
        max1 = center + radius
        speed = AW[0]*C[2][0] - AW[2]*C[0][0]
        if self.is_seperated(min0, max0, min1, max1, speed, t_max, tlast):
            return False
        
        #Axis C0+t*A1xB1
        radius = EA[0]*AbsC[2][1] + EA[2]*AbsC[0][1]
        min0 = -radius
        max0 = +radius
        center = AD[0]*C[2][1] - AD[2]*C[0][1]
        radius = EB[0]*AbsC[1][2] + EB[2]*AbsC[1][0]
        min1 = center - radius
        max1 = center + radius
        speed = AW[0]*C[2][1] - AW[2]*C[0][1]
        if self.is_seperated(min0, max0, min1, max1, speed, t_max, tlast):
            return False
        
        #Axis C0+t*A1xB2
        radius = EA[0]*AbsC[2][2] + EA[2]*AbsC[0][2]
        min0 = -radius
        max0 = +radius
        center = AD[0]*C[2][2] - AD[2]*C[0][2]
        radius = EB[0]*AbsC[1][1] + EB[1]*AbsC[1][0]
        min1 = center - radius
        max1 = center + radius
        speed = AW[0]*C[2][2] - AW[2]*C[0][2]
        if self.is_seperated(min0, max0, min1, max1, speed, t_max, tlast):
            return False
        
        #Axis C0+t*A2xB0
        radius = EA[0]*AbsC[1][0] + EA[1]*AbsC[0][0]
        min0 = -radius
        max0 = +radius
        center = AD[1]*C[0][0] - AD[0]*C[1][0]
        radius = EB[1]*AbsC[2][2] + EB[2]*AbsC[2][1]
        min1 = center - radius
        max1 = center + radius
        speed = AW[1]*C[0][0] - AW[0]*C[1][0]
        if self.is_seperated(min0, max0, min1, max1, speed, t_max, tlast):
            return False
        
        #Axis C0+t*A2xB1
        radius = EA[0]*AbsC[1][1] + EA[1]*AbsC[0][1]
        min0 = -radius
        max0 = +radius
        center = AD[1]*C[0][1] - AD[0]*C[1][1]
        radius = EB[0]*AbsC[2][2] + EB[2]*AbsC[2][0]
        min1 = center - radius
        max1 = center + radius
        speed = AW[1]*C[0][1] - AW[0]*C[1][1]
        if self.is_seperated(min0, max0, min1, max1, speed, t_max, tlast):
            return False
        
        #Axis C0+t*A2xB2
        radius = EA[0]*AbsC[1][2] + EA[1]*AbsC[0][2]
        min0 = -radius
        max0 = +radius
        center = AD[1]*C[0][2] - AD[0]*C[1][2]
        radius = EB[0]*AbsC[2][1] + EB[1]*AbsC[2][0]
        min1 = center - radius
        max1 = center + radius
        speed = AW[1]*C[0][2] - AW[0]*C[1][2]
        if self.is_seperated(min0, max0, min1, max1, speed, t_max, tlast):
            return False
        
        return True
