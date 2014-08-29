__author__ = 'mukhtar'
from numbers import Number

def square_perimeter(side : Number) -> Number:
    """
    Calculate perimeter of a square from side length.
    @param side: the side length
    @return: the perimeter (same units as side length)
    >>> square_perimeter(4)
    16
    """
    return 4*side
print(square_perimeter(5))



print(square_perimeter(6))

def square_area(side):
    """
calculate area of a square from side length
:param side:the side length
:return:the area (units^2 from side)
    >>> square_area(4)
16
    """
    return side*side
print (square_area (8))


if _name_ =="_main_":
    sampleside=4
    print("area:",
          square_area(sampleside),
          "perimeter:",
          square_perimeter(sampleside))
