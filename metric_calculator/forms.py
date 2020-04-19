from django import forms
from .validators import *

class Dimensions(forms.Form):
    DIMENSIONS = ((1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four'))
    shape_dimensions = forms.ChoiceField(widget=forms.RadioSelect, choices=DIMENSIONS)


class TwoDimensional(forms.Form):
    SHAPES = ((1, 'Circle'), (2, 'Quadrilateral'), (3, 'Triangle'), (4, 'Other'))
    shape = forms.ChoiceField(widget=forms.RadioSelect, choices=SHAPES)


class ThreeDimensional(forms.Form):
    SHAPES = ((1, 'Sphere'), (2, 'Prism (Quad)'), (3, 'Prism (Triangular)'), (4, 'Cylinder'), (5, 'Other'))
    shape = forms.ChoiceField(widget=forms.RadioSelect, choices=SHAPES)


class Parallels(forms.Form):
    COUNT = ((1, 'One'), (2, 'Two'))
    parallel_count = forms.ChoiceField(widget=forms.RadioSelect, choices=COUNT)


class TriangleDimensions(forms.Form):
    MEASUREMENTS = ((1, "Base and perpendicular height"), (2, "All three sides"), (3, "Neither 1 nor 2"))
    known_measurements = forms.ChoiceField(widget=forms.RadioSelect, choices=MEASUREMENTS)

class RadiusInput(forms.Form):
    r = forms.FloatField(min_value=0.01, label="Radius (cm)")

class QuadInput(forms.Form):
    l = forms.FloatField(min_value=0.01, label="Length (cm)")
    h = forms.FloatField(min_value=0.01, label="Perpendicular height (cm)")
    deg = forms.FloatField(max_value=90, min_value=0.01, label="Interior angle (degrees)")

class ABCInput(forms.Form):
    a = forms.FloatField(min_value=0.01, label="Length a (cm)")
    b = forms.FloatField(min_value=0.01, label="Length b (cm)")
    c = forms.FloatField(min_value=0.01, label="Length c (cm)")
        
    def clean_lengths(self):
        raw_a = self.cleaned_data['a']
        raw_b = self.cleaned_data['b']
        raw_c = self.cleaned_data['c']
        if raw_a + raw_b < raw_c or raw_b + raw_c < raw_a or raw_a + raw_c < raw_b:
            raise ValidationError("Your three lengths do not make a valid triangle.  Please try again.")

        measurements = (raw_a, raw_b, raw_c)
        return measurements

    def clean(self):
        self.clean_lengths()

class BHInput(forms.Form):
    b = forms.FloatField(min_value=0.01, label="Base (cm)")
    h = forms.FloatField(min_value=0.01, label="Perpendicular height (cm)")

class CylinderInput(RadiusInput):
    d = forms.FloatField(min_value=0.01, label="Depth (cm)")

class QuadPrismInput(QuadInput):
    d = forms.FloatField(min_value=0.01, label="Depth (cm)")

class ABCTriPrismInput(ABCInput):
    d = forms.FloatField(min_value=0.01, label="Depth (cm)")

class BHTriPrismInput(BHInput):
    d = forms.FloatField(min_value=0.01, label="Depth (cm)")