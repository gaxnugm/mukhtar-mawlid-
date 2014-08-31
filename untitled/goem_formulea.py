__author__ = 'mukhtar'
from numbers import Number
from numpy import*

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


def rectangle_area(length,width):
    """
    calculate area of rectangle for variable length and width.
    :param length:
    :param width:
    :param side:the side length,width
    :return:the area (unit from length,width)
    >>> rectangle,area (4,7)
    28
    """
    #length,width= 4.7
    return length*width
print (rectangle_area (4,7))


def parallelogram_area(base,height):
    """
     calculate the area of parallelogram for variable base and length
    :param base:
    :param height:
    :return:the area (unit from base,area)
    >>> parallelogram,area (7,3)
    21
    """
    #base,width=7,3
    return base*height
print(parallelogram_area(7,3))



def sphere_area(radius):
    """
    calculate the area of sphere with given variable pi and radius

    :param radius:
    :return:the area (unite from radius)
     >>> sphere_area (2)
    25.12
    """
    return 4*pi*radius*radius
print (sphere_area(2))

def circle_area(radius):
    """
    calculate the area of circle with given variable radius
    :param radius:
    :return:the area (unit from radius)
    >>> circle area (5)
    15.7
    """
    return pi*radius*radius
print (circle_area(5))


def triangle_area(base,height):
    """
    calculate the area of triangle with given variable base and height
    :param base:
    :param height:
    :return:the area (unit from base,height)
    >>>traingle area (7,6)
    21
    """
    return (base*height)/2
print(triangle_area(7,6))


def trapezoid_area(base,height):
    """
    calculate the area of trapezoid with given variable base and height
    :param base:
    :param height:
    :return:the area (unit from base,height)
     >>>trapezoid_area (2,4)
     8
     """
    return (height*(base+base))/2
print(trapezoid_area(2,4))

def cube_volume(side):
    """
     calculate the volume of cube with given variable side
    :param side:
    :return:the volume (unit from side)
    >>> cube_volume(3)
    27
    """
    return (side*side*side)

print (cube_volume(3))

def cylinder_volume(radius,height):
    """
    calculate the volume of cylinder with given variable radius and height
    :param radius:
    :param height:
    :return:the volume (unit from radius,height)
     >>> cylinder_volume (2,3)
     37.68
    """
    return (pi*radius*radius*height)
print (cylinder_volume(2,3))

def pyramid_volume(base,height):
    """
    calculate the volume of pyramid with given variable base and height
    :param base:
    :param height:
    :return:the volume (unit from base,height)
     >>> pyramid_volume (3,5)
     5
    """
    return (base*height)/3
print (pyramid_volume(3,5))


