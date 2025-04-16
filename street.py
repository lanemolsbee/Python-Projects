b'''
File: street.py
Author: Lane Molsbee
Course: CSC 120, Spring 2024
Purpose: This program renders a printed
street using user input. It utilizes multiple
classes to construct each building up to and including the
maximum height of any given structure. It includes parks,
buildings, and empty lots composed of various elements. 
'''
class Building:
    '''
    This class represents a building to be printed.
    Its primary methods are its constuctor as well
    as its construct method.
    It is to be constructed using integers and a string.
    There is nothing in particular to note about this class,
    other than that it is never directly used by
    the main function. It is utilized by only one function.
    '''
    def __init__(self, width, height, brick):
        '''
        This is the class constructor.
        Parameters:
        width and height are integers representing
        the width and height of the building.
        Brick is a string representing the material
        the building is to be constructed with. 
        Returns: nothing
        '''
        self._width = width
        self._height = height
        self._brick = brick
        self._orig_height = height
    
    def width(self):
        return self._width
    
    def height(self):
        return self._height
    
    def construct(self, max_height):
        '''
        This method constructs a list of the 
        building's elements, line by line
        from the bottom of the building to the sky above.
        Parameters: 
        max_height is an integer representing the maximum
        possible height of the building. 
        Returns: a list representing the line-by-line
        elements of the building up to and including
        the maximum height, using whitespace if necessary. 
        '''
        if max_height == 0:
            return []
        else:
            if self._height > 0:
                # Decrement the height to build
                self._height -= 1
                return [self._brick * self._width]\
                + self.construct(max_height - 1)
            else:
                # Build the empty space above.
                return [' '*self._width]\
                + self.construct(max_height - 1)
    
    def reset_height(self):
        self._height = self._orig_height
    
    def at_height(building_elts, n):
        '''
        This function finds the element at position
        n in the list of building lines.
        Parameter: n is an integer for a list index.
        Returns: the nth position of the generated list. 
        '''
        return building_elts[n]
    

class Park:
    '''
    This class represents a park to be printed. 
    Its primary method is construct.
    This class is to be constructed using
    an integer and a string. 
    This class is also not directly used. 
    '''
    def __init__(self, width, foliage):
        '''
        This is the class constructor
        Parameters:
        width is an integer that represents
        the width of the park. 
        foliage is a string representing what the
        leaves of the tree in the center of the park should be. 
        Returns: nothing
        '''
        self._width = width
        self._height = 5
        self._foliage = foliage
    
    def height(self):
        return self._height
    
    def construct(self, max_height):
        '''
        This method constructs the park's list representation.
        Parameters: max_height is an integer representing
        the maximum height of the park, including whitespace.
        Returns: a list of the park's line-by-line elements
        from the bottom of the park to the maximum height. 
        '''
        if max_height == 0:
            return []
        else:
            # Build the tree
            if self._height > 0:
                if self._height > 3:
                    # Decrement the tree space remaining
                    self._height -= 1
                    middle = self._width // 2
                    return [" " * middle + "|" + " " * middle] + \
                    self.construct(max_height - 1)
                else:
                    if self._height == 3:
                        self._height -= 1
                        middle = (self._width - 5) // 2
                        # Generate 5 leaves
                        return [" " * middle + self._foliage *\
                                 5 + " " * middle] \
                        + self.construct(max_height - 1)
                    elif self._height == 2:
                        self._height -= 1
                        middle = (self._width - 3) // 2
                        # Generate 3 leaves
                        return [' ' * middle + self._foliage * \
                                3 + " " * middle] + \
                        self.construct(max_height - 1)
                    elif self._height == 1:
                        self._height -= 1
                        middle = self._width // 2
                        # Generate 1 leaf. 
                        return [' ' * middle + self._foliage + " "\
                         * middle] + self.construct(max_height - 1)
            else:
                # Generate the whitespace above the tree. 
                return [' ' * self._width] + self.construct(max_height - 1)
    
    def width(self):
        return self._width
    
    def at_height(self, park, n):
        '''
        This function finds the element at position
        n in the list of building lines.
        Parameter: n is an integer for a list index.
        Returns: the nth position of the generated list. 
        '''
        return park[n]


class EmptyLot:
    '''
    This class represents an empty lot. 
    Its primary method is construct.
    It is to be constructed using an integer and string. 
    This class is also not directly used. 
    '''
    def __init__(self, width, trash):
        '''
        This is the class constructor.
        Parameters: width is an integer
        representing the width of the lot. 
        trash is a string representing the type of trash.
        '''
        self._width = width
        self._height = 1
        # Account for _ to make spaces. 
        if "_"  in trash:
            new_trash = str_replace(trash, "_", " ")
            self._trash = new_trash
        else:
            self._trash = trash

    def width(self):
        return self._width

    def height(self):
        return self._height

    def construct(self, max_height):
        '''
        This method constructs the empty lot
        including the white space above it. 
        Parameters: max_height is an integer
        representing the maximum height of the lot,
        including the whitespace above it. 
        '''
        if max_height == 0:
            return []
        else:
            if max_height > 1:
                # Create the whitespace above the lot. 
                return self.construct(max_height - 1) +\
                      [' ' * self._width]
                
            elif max_height == 1:
                # Ensure the trash string fits within width
                full = self._width // len(self._trash)
                remainder = self._width % len(self._trash)                
                remaining = self._trash[0:remainder]                
                return self.construct(max_height - 1) +\
                      [self._trash * full + remaining]

    def at_height(self, lot, n):
        '''
        This function finds the element at position
        n in the list of building lines.
        Parameter: n is an integer for a list index.
        Returns: the nth position of the generated list. 
        '''
        return lot[n]


def str_replace(original, string_one, string_two):
    '''
    This function replaces characters in in a string.
    Parameters:
    original is a string representing the original
    string before modification
    string_one is a string representing the character to be replaced
    string_two is a string representing the replacement character.
    Returns:
    The modified string
    '''
    if len(original) == 0:
        return ''
    else:
        if original[0] == string_one:
            return string_two  + str_replace(original[1:], \
                                string_one, string_two)
        else:
            return original[0] + str_replace(original[1:], string_one,\
                                             string_two)

def find_total_width(elts_list):
    '''
    This function finds the total width of the street.
    Parameters: elts_list is a list of street elements,
    including Building, Park, and EmptyLot objects. 
    Returns: the sum of the element widths
    '''
    if len(elts_list) == 0:
        return 0
    else:
        return elts_list[0].width() + find_total_width(elts_list[1:])

def find_max_height(elts_list, max):
    '''
    This function finds the maximum height
    of the street for printing. 
    Parameters:
    elts_list is a list containing street elements,
    including Building, Park, and EmptyLot objects.
    Returns: the maximum height out of each object.
    '''
    if len(elts_list) == 0:
        return max
    else:
        if max < elts_list[0].height():
            max = elts_list[0].height()
            return find_max_height(elts_list[1:], max)
        else:
            return find_max_height(elts_list[1:], max)
        
def construct_street(elts, max_height):
    '''
    This function constructs the street using
    the construct method of the object.
    Parameters: elts is a list of park elements,
    including Building, Park, and EmptyLot objects.
    max_height is an integer representing the maximum
    possible height of the street. 
    Returns: a 2d-list consisting of the list
    representations of the street elements. 
    '''
    if len(elts) == 0:
        return []
    else:
        return [elts[0].construct(max_height)] +\
              construct_street(elts[1:], max_height)
        
def get_buildings(elts):
    '''
    This function creates the buildings
    to be used by the other functions. 
    Parameters: elts is a list containing
    strings of structure parameters. 
    Returns: a list of street elements, 
    including Building, Park, and EmptyLot objects. 
    '''
    if len(elts) == 0:
        return []
    else:
        if elts[0][0] == "p":
            stats = elts[0].lstrip("p:").split(",")
            width = int(stats[0])
            foliage = stats[1]
            park = Park(width, foliage)
            return [park] + get_buildings(elts[1:])
        elif elts[0][0] == "b":
            stats = elts[0].lstrip("b:").split(",")
            width = int(stats[0])
            height = int(stats[1])
            brick = stats[2]
            building = Building(width, height, brick)
            return [building] + get_buildings(elts[1:])
        elif elts[0][0] == "e":
            stats = elts[0].lstrip("e:").split(",")
            width = int(stats[0])
            trash = stats[1]
            lot = EmptyLot(width, trash)
            return [lot] + get_buildings(elts[1:])

def print_street(street, height):
    '''
    This function prints the street using print_row. 
    Parameters: street is a 2d-list of list
    representations of the structures. 
    height is an integer representing the
    height to be rendered at. 
    '''
    if len(street) == 0:
        return
    else:
        if height < 0:
            return
        else:
            print("|", end = "")
            print_row(street, height)
            print("|")
            print_street(street, height - 1)

def print_row(street, height):
    '''
    This function renders the elements of the lists
    at the provided height. 
    Parameters:
    street is a 2d-list of list representations
    of the structures in the street. 
    height is an integer representing the 
    height to be rendered at. 
    '''
    if len(street) == 0:
        return
    else:
        print(street[0][height], end = "")
        print_row(street[1:], height)

def main():
    '''
    This function fulfills the purposes of this
    program in order to render the street.
    It takes no parameters and returns nothing. 
    '''
    street_name = input("Street:")
    street_elts = street_name.split()
    buildings = get_buildings(street_elts)
    width = find_total_width(buildings)
    height = find_max_height(buildings, 0)
    street = construct_street(buildings, height)
    # Create the upper border and empty space above
    print("+" + "-" * width + "+")
    print("|" + " " * width + "|")
    print_street(street, height - 1)
    print("+" + "-" * width + "+")

main()