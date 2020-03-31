from shape_class import ThreeDimensionalShape
import math

class Sphere(ThreeDimensionalShape):
    def __init__(self, r):
        self.r = r

    def announce_shape(self):
        return('sphere')

    def get_surface_area(self):
        return(4 * math.pi * (self.r ** 2))    

    def get_volume(self):
        return(4/3 * math.pi * (self.r ** 3))


class QuadPrism(ThreeDimensionalShape):
    def __init__(self, l, ph, angle, d):
        self.l = l
        self.ph = ph
        self.angle = math.radians(angle)
        self.d = d

    def announce_shape(self):
        return('prism')

    def get_remaining_sides(self):
        return self.ph / math.sin(self.angle)
        
    def get_surface_area(self):
        return((2 * (self.l * self.ph)) + (2 * (self.l * self.d)) + (2 * (self.get_remaining_sides() * self.d)))   

    def get_volume(self):
        return(self.l * self.ph * self.d)


class TriangularPrism(ThreeDimensionalShape):
    def __init__(self, b, d, ph=None, a=None, c=None):
        self.b = b
        self.ph = ph
        self.d = d

        if ph is not None:   
            self.a = math.sqrt(((0.5 * b) ** 2) + (ph ** 2))
            self.c = math.sqrt(((0.5 * b) ** 2) + (ph ** 2))
        else:
            self.a = a
            self.c = c

        self.halfp = 0.5 * (self.a + self.b + self.c)

    def announce_shape(self):
        return('triangular prism')

    def get_heron_area(self):
        return(math.sqrt(self.halfp * (self.halfp - self.a) * (self.halfp - self.b) * (self.halfp - self.c)))

    def get_surface_area(self):
        return((self.b * self.d) + (self.a * self.d) + (self.c * self.d) + (2 * self.get_heron_area()))
        
    def get_volume(self):
        return((self.get_heron_area()) * self.d)


class Cylinder(ThreeDimensionalShape):
    def __init__(self, r, d):
        self.r = r
        self.d = d
        self.cirf = r * 2 * math.pi

    def announce_shape(self):
        return('cylinder')

    def get_surface_area(self):
        return((2 * math.pi * (self.r ** 2)) + (self.cirf * self.d))

    def get_volume(self):
        return(math.pi * (self.r ** 2) * self.d)

