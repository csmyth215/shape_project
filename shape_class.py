import math
from abc import ABC, abstractmethod

# Create parent Shape classes
class TwoDimensionalShape(ABC):

    @abstractmethod
    def announce_shape(self):
        ...

    @abstractmethod
    def get_area(self):
        ...
        
    @abstractmethod
    def get_perimeter(self):
        ...



class ThreeDimensionalShape(ABC):

    @abstractmethod
    def announce_shape(self):
        ...

    @abstractmethod
    def get_surface_area(self):
        ...

    @abstractmethod
    def get_volume(self):
        ... 
