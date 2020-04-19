from two_dimensional_shapes import *
import math

def test_circle():
    c = Circle(5)
    assert c.get_area() == 25 * math.pi
    assert c.get_perimeter() == 10 * math.pi
