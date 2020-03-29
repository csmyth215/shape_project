import sys

class UserInteraction():

    def get_input_from_dict(self, options):
        # use for 2D/3D, for description, for triangle knowledge and for pairs of parallel lines
        for x, y in options.items():
            print(x, y)
        validation_pending = True
        while validation_pending == True:
            i = input()
            keys = options.keys()
            try:
                i = int(i)
                if i in keys:
                    validation_pending = False
                else:
                    print(f"Please enter {', '.join([str(i) for i in numbers[:-1]])} or {numbers[-1]}")
            except ValueError as ex:
                print(f"Please enter {', '.join([str(i) for i in numbers[:-1]])} or {numbers[-1]}")
                print("Debug!:", ex)
        return i

    def get_open_input(self, shape, dimensions):
        if len(dimensions) is None:
            print("Error encountered. Contact administrator")
            sys.exit()
        elif len(dimensions) == 1:
            print(f"Tell me the {dimensions[0]} of your {shape}: ")
        elif len(dimensions) == 2:
            print(f"Tell me the {dimensions[0]} and {dimensions[-1]} of your shape: ")
        elif len(dimensions) > 2:
            print(f"Tell me the {', '.join([str(i) for i in dimensions[:-1]])} and {dimensions[-1]} of your shape: ")
        else:
            print("Error encountered. Contact administrator")
            sys.exit()            

        responses = []
        validation_pending = True
        while validation_pending == True:
            for i in dimensions:
                x = input(f"{i}: ")
                try: 
                    x = int(x)
                    if x > 0:
                        validation_pending = False
                        responses.append(float(x))
                    else:
                        print("Please enter a numerical value greater than 0.")  
                except:
                    try:
                        x = float(x)
                        if x > 0:
                            validation_pending = False
                            responses.append(float(x))
                        else:
                            print("Please enter a numerical value greater than 0.")
                    except ValueError:
                        print("Please enter a numerical value.")               

        return responses

    def collect_triangle_info(self):
        approaches = {1: "Base and perpendicular height", 2: "All three sides", 3: "Neither 1 nor 2"}
        approach = self.get_input_from_dict(approaches)     

        if approach == 1:
            (b, ph) = self.get_open_input('triangle', ['base', 'perpendicular height'])
            measurements = (b, ph)
        
        elif approach == 2:
            check_ongoing = True
            while check_ongoing:
                (a, b, c) = self.get_open_input('triangle', ['Length A', 'Length B', 'Length C'])
                if a + b > c and b + c > a and a + c > b:
                    check_ongoing = False
                    measurements = (a, b, c)
                else:
                    print("Your three lengths do not make a valid triangle.  Please try again.")

        elif approach == 3:
            print("The calculator needs that minimum knowledge for now, sorry!")
            sys.exit() 

        return measurements
    
    def print_dimensions(self, shape_name, metrics):
        for x, y in metrics.items():
            print(f"Your {shape_name} has {x} {y} units.") 
             
    def print_perimeter(self, shape_name, shape):
        print(f"Your {shape_name} has perimeter", '{0:.2f}'.format(shape.get_perimeter()), "units.")

    def print_area(self, shape_name, shape):
        print(f"Your {shape_name} has area", '{0:.2f}'.format(shape.get_area()), "square units.")

    def print_surface_area(self, shape_name, shape):
        print(f"Your {shape_name} has surface area", '{0:.2f}'.format(shape.get_surface_area()), "square units.")

    def print_volume(self, shape_name, shape):
        print(f"Your {shape_name} has volume", '{0:.2f}'.format(shape.get_volume()), "cubic units.")

