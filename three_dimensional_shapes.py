from shape_class import ThreeDimensionalShape
import math

class Sphere(ThreeDimensionalShape):
    def __init__(self, radius):
        self.radius = radius

    def announce_shape(self):
        return('sphere')

    def get_surface_area(self):
        return(4 * math.pi * (self.radius ** 2))    

    def get_volume(self):
        return(4/3 * math.pi * (self.radius ** 3))


class QuadPrism(ThreeDimensionalShape):
    def __init__(self, length, width, depth):
        self.length = length
        self.width = width
        self.depth = depth

    def announce_shape(self):
        return('prism')

    def get_surface_area(self):
        # Only accurate for cubes or cuboids. Needs tailoring for prisms with other quadrilateral faces
        return((2 * (self.length * self.width)) + (2 * (self.length * self.depth)) + (2 * (self.width * self.depth)))   

    def get_volume(self):
        return(self.length * self.width * self.depth)


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
    def __init__(self, radius, depth):
        self.radius = radius
        self.depth = depth
        self.circumference = radius * 2 * math.pi

    def announce_shape(self):
        return('cylinder')

    def get_surface_area(self):
        return((2 * math.pi * (self.radius ** 2)) + (self.circumference * self.depth))

    def get_volume(self):
        return(math.pi * (self.radius ** 2) * self.depth)

