from two_dimensional_shapes import *
from three_dimensional_shapes import *

def determine_dimension_track():
    dimension_list = {2: 'Two dimensions', 3: 'Three dimensions'}

    print("Welcome to the shape metric calculator. \nHow many dimensions does your shape have?")
    for x, y in dimension_list.items():
        print(x,".", y)
    validation_pending = True
    while validation_pending == True:
        dimension_count = (input())
        try:
            dimension_count = int(dimension_count)
        except ValueError:
            pass
        if dimension_count in dimension_list.keys():
            validation_pending = False 
            print(f"\nWhich category does your {dimension_list[dimension_count][:-1].lower()}al shape best fit into?")
            if dimension_count == 2:
                select_two_dimensional_shape()
            elif dimension_count == 3:
                select_three_dimensional_shape()
        else:
            print("Please enter either '2' or '3'.")

def select_two_dimensional_shape():
    two_dimensional_inventory = {1: 'circle', 2: 'quadrilateral', 3: 'triangle', 4: 'other'}
    for x, y in two_dimensional_inventory.items():
        print(x,".", y)
    validation_pending = True
    while validation_pending == True:
        shape_number = input()
        try:
            shape_number = int(shape_number)
        except ValueError:
            pass
        if shape_number == 1:
            validation_pending = False
            perform_circle_calculations()
        elif shape_number == 2:
            validation_pending = False
            perform_quad_calculations()
        elif shape_number == 3:
            validation_pending = False
            determine_triangle_knowledge()
        elif shape_number == 4:
            validation_pending = False
            print("Other shapes will be coming soon.")
        else:
            print("Please enter either '1', '2' '3' or '4'.")
        
      

def perform_circle_calculations():
    print("Tell me the circle's radius: ")
    validation_pending = True
    while validation_pending == True:
        rad = input()
        try: 
            rad = int(rad)
            if rad > 0:
                validation_pending = False
            else:
                print("Please enter a numerical value greater than 0.")  
        except:
            try:
                rad = float(rad)
                if rad > 0:
                    validation_pending = False
                else:
                    print("Please enter a numerical value greater than 0.")  
            except ValueError:
                print("Please enter a numerical value.")

    my_circle = Circle(rad)
    print("Your circle has radius", rad, "units, perimeter", '{0:.2f}'.format(my_circle.get_perimeter()), "units and area", '{0:.2f}'.format(my_circle.get_area()), "square units")


def perform_quad_calculations():
    print("Tell me your shape's length and perpendicular height: ")
    length_validation_pending = True
    perph_validation_pending = True

    while length_validation_pending == True:
        leng = input("Length: ")
        try: 
            leng = int(leng)
            if leng > 0:
                length_validation_pending = False
            else:
                print("Please enter a numerical value greater than 0.")  
        except:
            try:
                leng = float(leng)
                if leng > 0:
                    length_validation_pending = False
                else:
                    print("Please enter a numerical value greater than 0.")
            except ValueError:
                print("Please enter a numerical value.")
        
    while perph_validation_pending == True:
        perph = input("Perpendicular height: ")
        try:
            perph = int(perph)
            if perph > 0:
                perph_validation_pending = False
            else:
                print("Please enter a numerical value greater than 0.")  
        except:
            try:
                perph = float(perph)
                if perph > 0:
                    perph_validation_pending = False
                else:
                    print("Please enter a numerical value greater than 0.")         
            except ValueError:
                print("Please enter a numerical value greater than 0.")  

    print("How many pairs of parallel side does your shape have - 1 or 2?")
    parallel_varification_pending = True
    while parallel_varification_pending == True:
        parallel_pairs = input()
        try:
            parallel_pairs = int(parallel_pairs)
            if parallel_pairs > 0 and parallel_pairs <= 2:
                parallel_varification_pending = False
            else:
                print("Please enter '1' or '2'.")
        except ValueError:
                print("Please enter '1' or '2'.")

    if parallel_pairs == 2:
        print(f"What is the smallest interior angle in your shape (in degrees)?")
        angle_validation_pending = True
        while angle_validation_pending == True:
            angle = input()
            try:
                angle = int(angle)
                if angle > 0 and angle <= 90:
                    angle_validation_pending = False
                else:
                    print("Please enter a numerical value greater than 0 and less than or equal to 90.")  
            except:
                try:
                    angle = float(angle)
                    if angle > 0 and angle <= 90:
                        angle_validation_pending = False
                    else:
                        print("Please enter a numerical value greater than 0 and less than or equal to 90.")  
                except ValueError:
                    print("Please enter a numerical value greater than 0 and less than or equal to 90.")

        my_quad = Quadrilateral(leng, perph, angle)
        print("Your shape has length", leng, "units, perpendicular height", perph, "units, perimeter", '{0:.2f}'.format(my_quad.get_perimeter()), "units and area", '{0:.2f}'.format(my_quad.get_area()), "square units")

    else:
        print("The shape metric calculator doesn't work with trapezia just yet, sorry!")



def determine_triangle_knowledge():
    print("What triangle metrics do you already know?")
    triangle_combinations = {1: "Base and perpendicular height", 2: "All three sides", 3: "Neither 1 nor 2"}
    for x, y in triangle_combinations.items():
        print(x,".", y)
    validation_pending = True
    while validation_pending == True:
        known_combo = input()
        try:
            known_combo = int(known_combo)
            if known_combo == 1:
                validation_pending = False
                perform_triangle_calculations_with_two_metrics()
            elif known_combo == 2:
                validation_pending = False
                perform_triangle_calculations_with_three_metrics()
            elif known_combo == 3:
                validation_pending = False
                print("The calculator needs that minimum knowledge for now, sorry!")
            else:
                print("Please enter '1', '2', or '3'.")
        except ValueError as ex:
            print("Please enter '1', '2', or '3'.")
            print("Debug!:", ex)


def perform_triangle_calculations_with_two_metrics():
    print("Tell me the base and perpendicular height of your triangle: ")
    base_validation_pending = True
    perph_validation_pending = True

    while base_validation_pending == True:
        base = input("Base: ")
        try: 
            base = int(base)
            if base > 0:
                base_validation_pending = False
            else:
                print("Please enter a numerical value greater than 0.")  
        except:
            try:
                base = float(base)
                if base > 0:
                    base_validation_pending = False
                else:
                    print("Please enter a numerical value greater than 0.")
            except ValueError:
                print("Please enter a numerical value.")

    while perph_validation_pending == True:
        perph = input("Perpendicular height: ")
        try:
            perph = int(perph)
            if perph > 0:
                perph_validation_pending = False
            else:
                print("Please enter a numerical value greater than 0.")  
        except:
            try:
                perph = float(perph)
                if perph > 0:
                    perph_validation_pending = False
                else:
                    print("Please enter a numerical value greater than 0.")         
            except ValueError:
                print("Please enter a numerical value greater than 0.")   

    my_tri = Triangle(base, ph=perph)
    print("Your triangle has base", base, "units, perpendicular height", perph, "units, perimeter", '{0:.2f}'.format(my_tri.get_perimeter()), "units and area", '{0:.2f}'.format(my_tri.get_area()), "square units")


def perform_triangle_calculations_with_three_metrics():
    print("Tell me the lengths of the three sides of your triangle: ")

    abc_validation_pending = True
    while abc_validation_pending == True:
        abc = []
        a = input("Length a: ")
        abc.append(a)
        b = input("Length b: ")
        abc.append(b)
        c = input("Length c: ")
        abc.append(c)

        count = 0
        for x in abc:
            try: 
                x = int(x)
                if x > 0:
                    count += 1
                else:
                    print("Please enter numerical values greater than 0.")
            except:
                try:
                    x = float(x)
                    if x > 0:
                        count += 1
                    else:
                        print("Please enter numerical values greater than 0.")
                except ValueError:
                    print("Please enter numerical values greater than 0.")

        if count == 3:
            abc_validation_pending = False
    
    a = float(a)
    b = float(b)
    c = float(c)
# Handle math domain error i.e. combination of lengths not possible to make triangle.

    my_tri = Triangle(b, a=a, c=c)
    print("Your triangle has lengths", a, b, "and", c, "units, perimeter", '{0:.2f}'.format(my_tri.get_perimeter()), "units and area", '{0:.2f}'.format(my_tri.get_area()), "square units")

def select_three_dimensional_shape():
    print("3D is coming soon!")

determine_dimension_track()
