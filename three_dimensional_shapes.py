from shape_class import ThreeDimensionalShape
import math

class Sphere(ThreeDimensionalShape):
    def __init__(self, radius):
        self.radius = radius

    def announce_shape(self):
        return('sphere')

    def get_surface_area(self):
        return(4 * math.pi * (r ** 2))    

    def get_volume(self):
        return(4/3 * math.pi * (self.radius ** 3))


class SquarePrism(ThreeDimensionalShape):
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def announce_shape(self):
        return('prism')

    def get_surface_area(self):
        return((2 * (self.length * self.width)) + (2 * (self.length * self.height)) + (2 * (self.width * self.height)))   

    def get_volume(self):
        return(self.length * self.width * self.height)


class TriangularPrism(ThreeDimensionalShape):
    def __init__(self, b, l, ph=None, a=None, c=None):
        self.b = b
        self.ph = ph
        self.l = l

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
        return((self.b * self.l) + (self.a * self.l) + (self.c * self.l) + (2 * self.get_heron_area()))
        
    def get_volume(self):
        return((self.get_heron_area()) * self.l)


class Cylinder(ThreeDimensionalShape):
    def __init__(self, radius, length):
        self.radius = radius
        self.length = length
        self.circumference = radius * 2 * math.pi

    def announce_shape(self):
        return('cylinder')

    def get_surface_area(self):
        return((2 * math.pi * (self.radius ** 2)) + (self.circumference * self.length))

    def get_volume(self):
        return(math.pi * (self.radius ** 2) * self.length)

my_3d_shape = TriangularPrism(8, 10, ph=3)
print(my_3d_shape.get_heron_area())
# print(f"The {my_3d_shape.announce_shape()} has a surface area of", "{0:.2f}".format(my_3d_shape.get_surface_area()), "square units and a volume of", "{0:.2f}".format(my_3d_shape.get_volume()), "cubic units.")
