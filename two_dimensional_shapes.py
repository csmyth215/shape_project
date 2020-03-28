from shape_class import TwoDimensionalShape
import math

class Circle(TwoDimensionalShape):
    
    def __init__(self, r):
        self.r = r

    def announce_shape(self):
        return('circle')

    def get_area(self):
        return(math.pi * (self.r ** 2))
    
    def get_perimeter(self):
        return(math.pi * (self.r * 2))
        

class Quadrilateral(TwoDimensionalShape):
    def __init__(self, l, ph, interior_angle):
        self.l = l
        self.ph = ph
        self.interior_angle = math.radians(interior_angle)

    def announce_shape(self):
        return('quatrilateral')

    def get_area(self):
        return(self.l * self.ph)
    
    def get_perimeter(self):
        return((2 * self.l) + (2 * (self.ph / math.sin(self.interior_angle))))   

class Triangle(TwoDimensionalShape):
    def __init__(self, b, ph=None, a=None, c=None):
        self.b = b
        self.ph = ph

        if ph is not None:   
            self.a = math.sqrt(((0.5 * b) ** 2) + (ph ** 2))
            self.c = math.sqrt(((0.5 * b) ** 2) + (ph ** 2))
        else:
            self.a = a
            self.c = c

        self.halfp = 0.5 * (self.a + self.b + self.c)

    def announce_shape(self):
        return('triangle')

    def get_area(self):
        return(math.sqrt(self.halfp * (self.halfp - self.a) * (self.halfp - self.b) * (self.halfp - self.c)))
    
    def get_perimeter(self):
        return(self.a + self.b + self.c) 

