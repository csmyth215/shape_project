from django.shortcuts import render, redirect
from .forms import *
import math

# Opportunities for improvement:
# - change all numeric dictionary keys to meaningful/transparent words
# - streamline references to dimensions i.e. use either lower or uppercase, not interchangeable
# - enter option to select measurement unit

# Create your views here.

def error(request, text):
    context = {'error': text}
    return render(request, 'metric_calculator/error.html', context)

# Determine approach.
def index(request):
    """The home page for the metric calculator."""
    return render(request, 'metric_calculator/index.html')

def determine_dimension_path(request):
    """Ask the user to specify 2D or 3D."""
    if request.method != 'POST':
        form = Dimensions()
    else:
        form = Dimensions(data=request.POST)
        if form.is_valid():
            dimensions = form.cleaned_data['shape_dimensions']
            if dimensions == "1":
                end_text = """It seems you already know the one thing there is to know! 
                \nThe calculator can't help you further."""
                return error(request, end_text)
            elif dimensions == "2":
                return redirect('metric_calculator:2D')
            elif dimensions == "3":
                return redirect('metric_calculator:3D')
            elif dimensions == "4":
                end_text = "The calculator isn't that good (yet!), sorry."
                return error(request, end_text)

    context = {'form': form}
    return render(request, 'metric_calculator/dimensions.html', context)
    
def specify_two_d_shape(request):
    """Ask user to pick from list of 2D shapes."""
    if request.method != 'POST':
        form = TwoDimensional()
    else:
        form = TwoDimensional(data=request.POST)
        if form.is_valid():
            shape = form.cleaned_data['shape']
            if shape == "1":
                return redirect('metric_calculator:circle')
            elif shape == "2":
                return redirect('metric_calculator:2D_parallels')
            elif shape == "3":
                return redirect('metric_calculator:triangle_info')
            elif shape == "4":
                end_text = "Other shapes will be coming soon."
                return error(request, end_text)


    context = {'form': form}
    return render(request, 'metric_calculator/2d_options.html', context)

def specify_three_d_shape(request):
    """Ask user to pick from list of 3D shapes."""  
    if request.method != 'POST':
        form = ThreeDimensional()
    else:
        form = ThreeDimensional(data=request.POST)
        if form.is_valid():
            shape = form.cleaned_data['shape']
            if shape == "1":
                return redirect('metric_calculator:sphere')
            elif shape == "2":
                return redirect('metric_calculator:3D_parallels')
            elif shape == "3":
                return redirect('metric_calculator:triangular_info')
            elif shape == "4":
                return redirect('metric_calculator:cylinder')
            elif shape == "5":
                end_text = "Other shapes will be coming soon."
                return error(request, end_text)

    context = {'form': form}
    return render(request, 'metric_calculator/3d_options.html', context)  

def get_2d_triangle_approach(request):
    """Determine if user knows abc or bh."""
    if request.method != 'POST':
        form = TriangleDimensions()
    else:
        form = TriangleDimensions(data=request.POST)
        if form.is_valid():
            approach = form.cleaned_data['known_measurements']
            if approach == "1":
                return redirect('metric_calculator:bh_tri')            
            elif approach == "2":
                return redirect('metric_calculator:abc_tri')
            elif approach == "3":
                end_text = "The calculator needs that minimum knowledge for now, sorry!"
                return error(request, end_text)

    context = {'form': form, 'shape': 'triangle'}
    return render(request, 'metric_calculator/triangle_approach.html', context)

def get_3d_triangle_approach(request):
    """Determine if user knows abc or bh."""
    if request.method != 'POST':
        form = TriangleDimensions()
    else:
        form = TriangleDimensions(data=request.POST)
        if form.is_valid():
            approach = form.cleaned_data['known_measurements']
            if approach == "1":
                return redirect('metric_calculator:bh_tri_prism')            
            elif approach == "2":
                return redirect('metric_calculator:abc_tri_prism')
            elif approach == "3":
                end_text = "The calculator needs that minimum knowledge for now, sorry!"
                return error(request, end_text)

    context = {'form': form, 'shape': 'triangular prism'}
    return render(request, 'metric_calculator/triangle_approach.html', context)

def get_2d_parallel_lines(request):
    """Check if shape has two sets of parallel lines."""
    if request.method != 'POST':
        form = Parallels()
    else:
        form = Parallels(data=request.POST)
        if form.is_valid():
            count = form.cleaned_data['parallel_count']
            print(count)
            if count == "2":
                return redirect('metric_calculator:quad')
            elif count == "1":
                end_text = "The shape metric calculator doesn't work with trapezia just yet, sorry!"
                return error(request, end_text)

    context = {'form': form, 'shape': '2D_quad'}
    return render(request, 'metric_calculator/parallels.html', context)

def get_3d_parallel_lines(request):
    """Check if shape has two sets of parallel lines."""
    if request.method != 'POST':
        form = Parallels()
    else:
        form = Parallels(data=request.POST)
        if form.is_valid():
            count = form.cleaned_data['parallel_count']
            if count == "2":
                return redirect('metric_calculator:quad_prism')
            elif count == "1":
                end_text = "The shape metric calculator doesn't work with trapezia just yet, sorry!"
                return error(request, end_text)

    context = {'form': form, 'shape': '3D_quad'}
    return render(request, 'metric_calculator/parallels.html', context)

# Get dimensions and calculate. 

def circle_results(request):
    """Ask for radius and return circle perimeter and area."""
    if request.method != 'POST':
        form = RadiusInput()
    else:
        form = RadiusInput(data=request.POST)
        if form.is_valid():
            radius = form.cleaned_data['r']
            perimeter = radius * 2 * math.pi
            area = radius ** 2 * math.pi

            context = {'is_3d': False, 'shape': 'circle', 'perimeter': perimeter, 'area': area}
            return render(request, 'metric_calculator/results.html', context)

    context = {'form': form, 'shape': 'circle'}
    return render(request, 'metric_calculator/input_dimensions.html', context)

def quad_results(request):
    """Ask for length, perpendicular height and interior angle, 
    and return perimeter and area."""
    if request.method != 'POST':
        form = QuadInput()
    else:
        form = QuadInput(data=request.POST)
        if form.is_valid():
            length = form.cleaned_data['l']
            height = form.cleaned_data['h']
            int_angle = math.radians(form.cleaned_data['deg'])

            area = length * height
            perimeter = (2 * length) + (2 * (height / math.sin(int_angle)))
            context = {'is_3d': False, 'shape': 'quadrilateral', 'perimeter': perimeter, 'area': area, 'angle': int_angle}
            return render(request, 'metric_calculator/results.html', context)


    context = {'form': form, 'shape': 'quadrilateral'}
    return render(request, 'metric_calculator/input_dimensions.html', context)

def abc_triangle_results(request):
    """Ask for lengths, check lengths, and return perimeter and area."""
    if request.method != 'POST':
        form = ABCInput()
    else:
        form = ABCInput(data=request.POST)
        if form.is_valid():
            measurements = form.clean_lengths()
            a = measurements[0]
            b = measurements[1]
            c = measurements[2]

            perimeter = a + b + c
            halfp = perimeter * 0.5
            area = math.sqrt(halfp * (halfp - a) * (halfp - b) * (halfp - c))

            context = {'is_3d': False, 'shape': 'triangle', 'perimeter': perimeter, 'area': area}
            return render(request, 'metric_calculator/results.html', context)


    context = {'form': form, 'shape': 'abc_triangle'}
    return render(request, 'metric_calculator/input_dimensions.html', context)

def bh_triangle_results(request):
    """Ask for base and perpendicular height, and return perimeter and area."""
    if request.method != 'POST':
        form = BHInput()
    else:
        form = BHInput(data=request.POST)
        if form.is_valid():
            b = form.cleaned_data['b']
            h = form.cleaned_data['h']
            a = math.sqrt(((0.5 * b) ** 2) + (h ** 2))
            c = math.sqrt(((0.5 * b) ** 2) + (h ** 2))

            perimeter = a + b + c
            halfp = perimeter * 0.5
            area = math.sqrt(halfp * (halfp - a) * (halfp - b) * (halfp - c))

            context = {'is_3d': False, 'shape': 'triangle', 'perimeter': perimeter, 'area': area}
            return render(request, 'metric_calculator/results.html', context)


    context = {'form': form, 'shape': 'bh_triangle'}
    return render(request, 'metric_calculator/input_dimensions.html', context)

def sphere_results(request):
    """ Ask for radius and return sphere volume and surface area."""
    if request.method != 'POST':
        form = RadiusInput()
    else:
        form = RadiusInput(data=request.POST)
        if form.is_valid():
            radius = form.cleaned_data['r']
            surface_area = 4 * math.pi * (radius ** 2)
            volume = 4/3 * math.pi * (radius ** 3)

            context = {'is_3d': True, 'shape': 'sphere', 'surface_area': surface_area, 'volume': volume}
            return render(request, 'metric_calculator/results.html', context)

    context = {'form': form, 'shape': 'sphere'}
    return render(request, 'metric_calculator/input_dimensions.html', context)

def abc_tri_prism_results(request):
    """Ask for lengths and depth, check lengths, and return volume and surface area."""
    if request.method != 'POST':
        form = ABCTriPrismInput()
    else:
        form = ABCTriPrismInput(data=request.POST)
        if form.is_valid():
            measurements = form.clean_lengths()
            a = measurements[0]
            b = measurements[1]
            c = measurements[2]
            d = form.cleaned_data['d']

            perimeter = a + b + c
            halfp = perimeter * 0.5
            area = math.sqrt(halfp * (halfp - a) * (halfp - b) * (halfp - c))
            surface_area = (b * d) + (a * d) + (c * d) + (2 * area)
            volume = area * d

            context = {'is_3d': True, 'shape': 'triangular prism', 'surface_area': surface_area, 'volume': volume}
            return render(request, 'metric_calculator/results.html', context)

    context = {'form': form, 'shape': 'abc_tri_prism'}
    return render(request, 'metric_calculator/input_dimensions.html', context)

def bh_tri_prism_results(request):
    """Ask for base, perpendicular height and depth, and return volume and surface area."""
    if request.method != 'POST':
        form = BHTriPrismInput
    else:
        form = BHTriPrismInput(data=request.POST)
        if form.is_valid():
            b = form.cleaned_data['b']
            h = form.cleaned_data['h']
            d = form.cleaned_data['d']
            a = math.sqrt(((0.5 * b) ** 2) + (h ** 2))
            c = math.sqrt(((0.5 * b) ** 2) + (h ** 2))

            perimeter = a + b + c
            halfp = perimeter * 0.5
            area = math.sqrt(halfp * (halfp - a) * (halfp - b) * (halfp - c))
            surface_area = (b * d) + (a * d) + (c * d) + (2 * area)
            volume = area * d

            context = {'is_3d': True, 'shape': 'triangular prism', 'surface_area': surface_area, 'volume': volume}
            return render(request, 'metric_calculator/results.html', context)


    context = {'form': form, 'shape': 'bh_tri_prism'}
    return render(request, 'metric_calculator/input_dimensions.html', context)

def quadprism_results(request):
    """Ask for length, perpendicular height, interior angle and depth, 
    and return volume and surface area."""
    if request.method != 'POST':
        form = QuadPrismInput()
    else:
        form = QuadPrismInput(data=request.POST)
        if form.is_valid():
            l = form.cleaned_data['l']
            h = form.cleaned_data['h']
            int_angle = math.radians(form.cleaned_data['deg'])
            d = form.cleaned_data['d']
            side = h / math.sin(int_angle)

            area = l * h
            perimeter = (2 * l) + (2 * side)
            surface_area = (2 * (l * h)) + (2 * (l * d)) + (2 * (side * d))
            volume = l * h * d 
            context = {'is_3d': True, 'shape': 'quad prism', 'surface_area': surface_area, 'volume': volume}
            return render(request, 'metric_calculator/results.html', context)

    context = {'form': form, 'shape': 'quad_prism'}
    return render(request, 'metric_calculator/input_dimensions.html', context)

def cylinder_results(request):
    """Ask for radius and depth, and return volume and surface area."""
    if request.method != 'POST':
        form = CylinderInput()
    else:
        form = CylinderInput(data=request.POST)
        if form.is_valid():
            r = form.cleaned_data['r']
            d = form.cleaned_data['d']
            circumf = r * 2 * math.pi
            surface_area = (2 * math.pi * (r ** 2)) + (circumf * d)
            volume = math.pi * (r ** 2) * d

            context = {'is_3d': True, 'shape': 'cylinder', 'surface_area': surface_area, 'volume': volume}
            return render(request, 'metric_calculator/results.html', context)

    context = {'form': form, 'shape': 'cylinder'}
    return render(request, 'metric_calculator/input_dimensions.html', context)