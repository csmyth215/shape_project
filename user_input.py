import sys
from two_dimensional_shapes import *
from three_dimensional_shapes import *

# Currently lacking final input option to ask the user if they would like to run the program again.

# Need to restructure code to separate user input from calculations, 
# and group calculations common to several shapes.

# Need to write automated tests to identify calculation or programming errors.

def get_radius(item):
    item = str(item)
    print(f"Tell me the radius of the {item}: ")
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

    return(float(rad))

def get_quad_properties(quad):
    # requires wording alignment

    quad = str(quad)
    print(f"Tell me the length and perpendicular height of {quad}: ")
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

        properties = (leng, perph, angle)
        properties_ints = []
        for i in properties:
            properties_ints.append(int(i))
        return properties_ints

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
                return get_bh()
            elif known_combo == 2:
                validation_pending = False
                return get_abc()
            elif known_combo == 3:
                validation_pending = False
                print("The calculator needs that minimum knowledge for now, sorry!")
            else:
                print("Please enter '1', '2', or '3'.")
        except ValueError as ex:
            print("Please enter '1', '2', or '3'.")
            print("Debug!:", ex)

def get_bh():
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

        bh = []
        base = float(base)
        ph = float(perph)
        bh.append(base)
        bh.append(perph)
    
    return bh

def get_abc():
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
        
        abcfloats = []
        a = float(a)
        b = float(b)
        c = float(c)
        abcfloats.append(a)
        abcfloats.append(b)
        abcfloats.append(c)

        if a + b > c and b + c > a and a + c > b and count == 3:
            abc_validation_pending = False 
        else:
            print("Your three lengths do not make a valid triangle.  Please try again.")
    
    return abcfloats

def determine_prism_type():
    print("What shape is the base of your prism?")
    prisms = {1: "Quadrilateral", 2: "Triangle", 3: "Other"}
    for x, y in prisms.items():
        print(x,".", y)
    validation_pending = True
    while validation_pending == True:
        prism = input()
        try:
            prism = int(prism)
            if prism == 1:
                validation_pending = False
                this_prism_properties = (1, get_quad_properties("one prism face"))
                return this_prism_properties
            elif prism == 2:
                validation_pending = False
                print("Thinking of the triangular face of your prism...")
                this_prism_properties = (2, determine_triangle_knowledge())
                return this_prism_properties
            elif prism == 3:
                validation_pending = False
                print("The calculator isn't built for prisms with so may size yet, sorry!")
            else:
                print("Please enter '1', '2', or '3'.")
        except ValueError as ex:
            print("Please enter '1', '2', or '3'.")
            print("Debug!:", ex)

def determine_depth(shape):
    print(f"Tell me the depth of your {shape}: ") 
    validation_pending = True
    while validation_pending == True:
        depth = input("Depth: ")
        try: 
            depth = int(depth)
            if depth > 0:
                length_validation_pending = False
            else:
                print("Please enter a numerical value greater than 0.")  
        except:
            try:
                depth = float(depth)
                if depth > 0:
                    length_validation_pending = False
                else:
                    print("Please enter a numerical value greater than 0.")
            except ValueError:
                print("Please enter a numerical value.")
        
        return(float(depth))

def size_two_dimensional_shape():
    two_dimensional_inventory = {1: 'Circle', 2: 'Quadrilateral', 3: 'Triangle', 4: 'Other'}
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
            this_radius = get_radius("circle")
            my_circle = Circle(this_radius)
            print(f"Your circle has radius", this_radius, "units, perimeter", 
            '{0:.2f}'.format(my_circle.get_perimeter()), "units and area", 
            '{0:.2f}'.format(my_circle.get_area()), "square units")
        
        elif shape_number == 2:
            validation_pending = False
            this_quad = get_quad_properties("your quadrilateral")
            my_quad = Quadrilateral(this_quad[0], this_quad[1], this_quad[2])
            print("Your shape has length", this_quad[0], "units, 
            perpendicular height", this_quad[1], "units, perimeter", 
            '{0:.2f}'.format(my_quad.get_perimeter()), "units and area", 
            '{0:.2f}'.format(my_quad.get_area()), "square units")
        
        elif shape_number == 3:
            validation_pending = False
            properties = determine_triangle_knowledge()
            if properties is None:
                print("Aborting program for now (insufficient knowledge).")
                sys.exit()
            if len(properties) == 3:
                # abc known            
                my_tri = Triangle(properties[1], a=properties[0], c=properties[2])
                print("Your triangle has lengths", properties[0],",", properties[1], 
                "and", properties[2], "units, perimeter", '{0:.2f}'.format(my_tri.get_perimeter()), 
                "units and area", '{0:.2f}'.format(my_tri.get_area()), "square units")

            elif len(properties) == 2:
                # base and height known
                my_tri = Triangle(properties[0], ph=properties[1])
                print("Your triangle has base", properties[0], "units, perpendicular height", 
                properties[1], "units, perimeter", '{0:.2f}'.format(my_tri.get_perimeter()), 
                "units and area", '{0:.2f}'.format(my_tri.get_area()), "square units")

            else:
                print("Error encountered. Contact administrator.")

        elif shape_number == 4:
            validation_pending = False
            print("Other shapes will be coming soon.")
        else:
            print("Please enter either '1', '2' '3' or '4'.")

def size_three_dimensional_shape():
    three_dimensional_inventory = {1: 'Sphere', 2: 'Prism', 3: 'Cylinder', 4: 'Other'}
    for x, y in three_dimensional_inventory.items():
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
            this_radius = get_radius("sphere")
            my_sphere = Sphere(this_radius)
            print(f"Your sphere has radius", this_radius, 
            ", surface area", '{0:.2f}'.format(my_sphere.get_surface_area()), 
            "square units and volume", '{0:.2f}'.format(my_sphere.get_volume()), "cubic units.")
        
        elif shape_number == 2:
            validation_pending = False
            properties = determine_prism_type()
            if properties[1] is None:
                print("Aborting program for now (insufficient knowledge).")
                sys.exit()    
            d = determine_depth("prism")

            if properties[0] == 1:
                my_quad_prism = QuadPrism(properties[1][0], properties[1][1], d)
                print(f"Your prism has surface area", 
                '{0:.2f}'.format(my_quad_prism.get_surface_area()), 
                "square units and volume", '{0:.2f}'.format(my_quad_prism.get_volume()), "cubic units.")
      
            elif properties[0] == 2:
                if len(properties[1]) == 3:
                    # abc known  
                    my_tri_prism = TriangularPrism(properties[1][1], d, a=properties[1][0], c=properties[1][2])
                    print("Your prism has surface area", 
                    '{0:.2f}'.format(my_tri_prism.get_surface_area()), 
                    "square units and volume", '{0:.2f}'.format(my_tri_prism.get_volume()), "cubic units.")
      
                elif len(properties[1]) == 2:
                    # base and height known
                    my_tri_prism = TriangularPrism(properties[1][0], d, ph=properties[1][1])
                    print("Your prism has surface area", 
                    '{0:.2f}'.format(my_tri_prism.get_surface_area()), 
                    "square units and volume", 
                    '{0:.2f}'.format(my_tri_prism.get_volume()), "cubic units.")
                
                else:
                    print("Error encountered. Contact administrator.")
      
        elif shape_number == 3:
            validation_pending = False
            this_radius = get_radius("circular face")
            d = determine_depth("cylinder")
            my_cylinder = Cylinder(this_radius, d)
            print(f"Your cylinder has radius", this_radius, 
            ", depth", d, 
            ", surface area", '{0:.2f}'.format(my_cylinder.get_surface_area()), 
            "square units and volume", '{0:.2f}'.format(my_cylinder.get_volume()), "cubic units.")
        
        elif shape_number == 4:
            validation_pending = False
            print("Other shapes will be coming soon.")
        else:
            print("Please enter either '1', '2' '3' or '4'.")

def determine_dimension_track():
    dimension_list = {1: 'Two dimensions', 2: 'Three dimensions'}

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
                size_two_dimensional_shape()
            elif dimension_count == 3:
                size_three_dimensional_shape()
        else:
            print("Please enter either '2' or '3'.")

determine_dimension_track()