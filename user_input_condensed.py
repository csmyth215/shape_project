import sys
from two_dimensional_shapes import *
from three_dimensional_shapes import *
from user_interaction import *

"""Outer loop to be added to accommodate input for several shapes in one session."""

def process_twodimensional_shape():
    # process two-dimensional objects
    print("Is your shape a...")

    shapedict = {1: 'Circle', 2: 'Quadrilateral', 3: 'Triangle', 4: 'Other'}
    shape = this_session.get_input_from_dict(shapedict)
    if shape == 1:
        r = this_session.get_open_input(shapedict[1], ['radius'])
        my_circle = Circle(r[0])
        this_session.print_perimeter('circle', my_circle)
        this_session.print_area('circle', my_circle)


    elif shape == 2:
        (l, ph, interior_angle) = this_session.get_open_input(shapedict[2],
        ['length', 'perpendicular height', 'smallest interior angle'])
        my_quad = Quadrilateral(l, ph, interior_angle)
        this_session.print_perimeter('quadrilateral', my_quad)
        this_session.print_area('quadrilateral', my_quad)

    elif shape == 3:
        # bh or abc?
        print("What triangle metrics do you already know?")
        metrics = this_session.collect_triangle_info()

        if len(metrics) == 2:
            my_tri = Triangle(metrics[0], ph=metrics[1])
        
        if len(metrics) == 3:
            my_tri = Triangle(metrics[1], a=metrics[0], c=metrics[2])

        this_session.print_perimeter('triangle', my_tri)
        this_session.print_area('triangle', my_tri)

    elif shape == 4:
        print("Other shapes will be coming soon.")
        sys.exit()

def process_threedimensional_shape():
    # process three-dimensional objects
    print("Is your shape a...") 

    shapedict = {1: 'Sphere', 2: 'Prism', 3: 'Cylinder', 4: 'Other'}
    shape = this_session.get_input_from_dict(shapedict)

    if shape == 1:
        r = this_session.get_open_input(shapedict[1], ['radius'])
        my_sphere = Sphere(r[0])
        this_session.print_surface_area('sphere', my_sphere)
        this_session.print_volume('sphere', my_sphere)

    if shape == 2:
        print("What shape is the base of your prism?")
        prisms = {1: "Quadrilateral", 2: "Triangle", 3: "Other"}
        prismtype = this_session.get_input_from_dict(prisms)

        if prismtype == 1:
            (l, w, d) = this_session.get_open_input(shapedict[2], ['length', 'width', 'depth'])
            my_prism = QuadPrism(l, w, d)
            this_session.print_surface_area('prism', my_prism)
            this_session.print_volume('prism', my_prism)

        if prismtype == 2:
            print("What metrics do you already know about the triangular base?")
            metrics = this_session.collect_triangle_info()
            d = this_session.get_open_input(shapedict[2], ['depth'])

            if len(metrics) == 2:
                my_tri = TriangularPrism(metrics[0], d, ph=metrics[1])
        
            if len(metrics) == 3:
                my_tri = TriangularPrism(metrics[1], d, a=metrics[0], c=metrics[2])

            this_session.print_surface_area('triangular prism', my_tri)
            this_session.print_volume('triangular prism', my_tri)


    if shape == 3:
        (r, d) = this_session.get_open_input(shapedict[3], ['radius', 'depth'])
        my_cylinder = Cylinder(r, d)
        this_session.print_surface_area('cylinder', my_cylinder)
        this_session.print_volume('cylinder', my_cylinder)

    if shape == 4:
        print("Other shapes will be coming soon.")
        sys.exit()

# Create a new input session
this_session = UserInteraction()

print("""Welcome to the shape metric calculator. 
\nHow many dimensions does your shape have?""")

dimensions = {1: 'One dimension', 2: 'Two dimensions', 3: 'Three dimensions'}
dimension_count = this_session.get_input_from_dict(dimensions)
if dimension_count == 1:
    print("I'll have to draw the line at that one sadly. The calculator won't be able to help you further.")
elif dimension_count == 2:
    process_twodimensional_shape()
elif dimension_count == 3:
    process_threedimensional_shape()

