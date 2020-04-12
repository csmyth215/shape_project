from django.core.exceptions import ValidationError

def validate_abc(a, b, c):
    if a + b < c or b + c < a or a + c < b:
        raise ValidationError("Your three lengths do not make a valid triangle.  Please try again.")
    else:
        measurements = (a, b, c)
        return measurements