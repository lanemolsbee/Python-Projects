'''

Lane Molsbee
CSC110
Programming Project 1
This program contains four functions for
calculating the areas of various shapes
'''
def rectangle_area(base, height):
    '''

    This function uses two arguments to calculate
    the area of a rectangle
    Args:
    base: a float representing the base
    of the rectangle
    height: a float representing the height
    of the rectangle
    Returns:
    The product of base and height, or the 
    area of a rectangle
    '''
    # Returns the area
    return base * height

def triangle_area(a,b,c,):
    '''
    
    This function uses three arguments a, b, and c
    to calculate the area of a triangle
    Args:
    a: a float representing a side of the triangle
    b: a float representing another side of the shape\
    c: a float representing the final side
    Returns:
    The area of the triangle by using Heron's formula
    '''
    # Calculates the semiperimeter
    s = (a + b + c) / 2
    # Returns the area
    return (s * (s-a) * (s-b) * (s-c)) ** (1/2)

def trapezoid_area(base_1, base_2, height):
    '''

    This function uses three arguments to calculate
    the area of a trapezoid
    Args:
    base_1: a float representing the first base of
    the trapezoid
    base_2: a float representing the second base
    height: a float representing the height of
    the trapezoid
    Returns:
    The area of the trapezoid
    '''
    # Returns the area
    return (1/2) * (base_1 + base_2) * height

def circle_area(radius):
    '''

    This function uses one argument to calculate
    the area of a circle
    Args:
    radius: a float representing the radius of a circle
    Returns:
    The area of the circle rounded to two decimal places
    '''
    # Returns the area
    return round(3.1415 * radius ** 2, 2)