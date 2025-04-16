'''
File: battleship.py
Author: Lane Molsbee
Course: CSC 120, Spring 2024
Purpose: This program implements a battleship
board with pre-defined ship placements and guesses
and determines if the ship placements are valid,
then runs through guesses until the ships are sunk. 
It requires no actual playing of the game. 
'''
import sys
class GridPos:
    '''
    This class represents a position on the grid.
    Its primary method is coords().
    It is to be constructed using two integers. 
    This class is vital to the overall functioning
    of the program as it is used to build the board
    and each instance of this class contains a part
    of a ship that is used in the program.
    '''
    def __init__(self, x, y):
        '''
        This is the class constructor.
        Parameters:
        x and y are integers representing
        an x-coordinate and y-coordinate on
        the board, respectively.
        Returns: nothing
        This function also has instance variables
        determining whether part of a ship is contained
        within the instance and if the position
        has been guessed or not. 
        '''
        self._x = x
        self._y = y
        self._ship = None
        self._guessed = False
    
    def coords(self):
        return (self._x, self._y)
    def guess(self):
        self._guessed = True
    
    def __str__(self):
        '''
        This is the __str__ method for the class.
        Parameters: None
        Returns: a string representation of the object
        '''
        # Used to print the board and whether there is a ship
        if self._ship == None:
            return "x"
        else:
            return self._ship
    def __repr__(self):
        '''
        This is the __repr__ method for the class.
        Parameters: None
        Returns: a string representation of the object
        '''
        if self._ship == None:
            return "x"
        else:
            return self._ship
        
class Board:
    '''
    This class represents the battleship board.
    Its primary methods are guess and place_ships.
    It is to be constructed using a list of Ship objects.
    This class contains the board that is used to guess
    and it consists of a 2D list of GridPos objects.
    '''
    def __init__(self, ships):
        '''
        This is the class constructor.
        Parameters: ships is a list of Ship objects
        Returns: nothing
        '''
        # Build the board
        self._grid = []
        for i in range(10):
            row = []
            for j in range(10):
                row.append(GridPos(i,j))
            self._grid.append(row)
        self._ships = ships
   
    def place_ships(self):
        '''
        This function places the ships on the board.
        Parameters: none
        Returns: nothing
        This function utilizes the _ships attribute
        in order to place each position of each Ship
        object on the board.
        '''
        for ship in self._ships:
            for pos in ship._positions:
                for row in self._grid:
                    for gridpos in row:
                        # Determine if the coordinates are equal
                        if pos.coords() == gridpos.coords():
                            gridpos._ship = ship._type        
    def guess(self, gridpos):
        '''
        This function makes a guess on the board.
        Parameters: gridpos is a GridPos object
        representing a guess to be made. 
        Returns: nothing
        This function is primarily responsible
        for printing out the hit and miss messages,
        and it also determines if all the ships have been sunk.
        '''
        for row in self._grid:
            for pos in row:
                if pos.coords() == gridpos.coords():
                    # Account for spaces not guessed
                    if pos._guessed == False:
                        pos._guessed = True
                        if pos._ship == None:
                            print("miss")
                        else:
                            # Determine which ship was hit                            
                            for ship in self._ships:
                                if ship._type == pos._ship:
                                    ship._not_hit -= 1
                                    if ship._not_hit == 0:
                                        print("{} sunk".format(ship))
                                    else:
                                        print('hit')
                    else:
                        # Account for whether there was a ship
                        if pos._ship == None:
                            print("miss (again)")
                        else:
                            print("hit (again)")
        # Determine if all the ships have been sunk
        all_sunk = True
        for ship in self._ships:
            if ship._not_hit != 0:
                all_sunk = False
        if all_sunk:
            print("all ships sunk: game over")

    def __str__(self):
        '''
        This is the __str__ method for the class. 
        Parameters: none
        Returns: nothing
        This function converts the board into
        a printable grid. 
        '''
        lis = ""
        for row in self._grid:
            lis += str(row) + "\n"
        return lis
    def __repr__(self):
        '''
        This is the __repr__ method for the class. 
        Parameters: none
        Returns: nothing
        This function converts the board into
        a printable grid. 
        '''
        lis = ""
        for row in self._grid:
            lis += str(row) + "\n"
        return lis

class Ship:
    '''
    This class represents a Ship on the board. 
    Its primary methods are just its __str__ 
    and __repr__ methods.
    It is to be constructed with a string
    and a list.
    Each Ship object contains a list of all
    the positions it occupies on the board.
    '''
    def __init__(self,type, positions):
        '''
        This is the class constructor.
        Parameters:
        type is a one-character string representing the Ship type.
        positions is a list of GridPos objects representing
        all the positions the Ship occupies on the Board.
        A main thing to note about this class is
        its _not_hit attribute, which is vital for 
        determining whether all the ships have been sunk. 
        '''
        self._type = type
        # Determine the ship size
        self._size = 0
        if type == "A":
            self._size = 5
        elif type == "B":
            self._size = 4
        elif type == "S":
            self._size = 3
        elif type == "D":
            self._size = 3
        elif type == "P":
            self._size = 2
        self._positions = positions
        self._not_hit = self._size
    
    def __str__(self):
        '''
        This is the __str__ method for the class. 
        Parameters: none
        Returns: a string representation of the object
        '''
        # Return type so message can be printed if sunk
        if self._not_hit == 0:
            return self._type
        return self._type + ":" + str(self._positions) +\
              "," + str(self._not_hit)
    def __repr__(self):
        '''
        This is the __str__ method for the class. 
        Parameters: none
        Returns: a string representation of the object
        '''
        # Return type so message can be printed if sunk
        if self._not_hit == 0:
            return self._type
        return self._type + ":" + str(self._positions) +\
              "," + str(self._not_hit)

def build(positions):
    '''
    This function builds the list of 
    positions a Ship object occupies.
    Parameters: positions is a list of Ship endpoints
    Returns:
    a list consisting of all the grid positions
    a Ship object occupies. 
    '''
    # Build horizontal ships
    points = []
    if positions[0]._y == positions[1]._y:
        # Start with the lower x-value
        lower_x = min(positions[0]._x, positions[1]._x)
        higher_x = max(positions[0]._x, positions[1]._x)
        for i in range(lower_x, higher_x + 1):
            points.append(GridPos(i, positions[0]._y))
    # Build vertical ships
    elif positions[0]._x == positions[0]._x:
        # Start with the lower y-value
        lower_y = min(positions[0]._y, positions[1]._y)
        higher_y = max(positions[0]._y, positions[1]._y)
        for i in range(lower_y, higher_y + 1):
            points.append(GridPos(positions[0]._x, i))
    return points

def get_ships(file_lines):
    '''
    This function gets all the Ships in the file.
    Parameters: file_lines is a list containing
    each line of the file. 
    Returns: a list of Ship objects.
    '''
    ships = []
    for line in file_lines:
        elts = line.split()
        # Get the numerical values as integers
        for i in range(1, len(elts)):
            elts[i] = int(elts[i])
        type = elts[0]
        positions = []
        # Get the endpoints
        pos_one = GridPos(elts[1], elts[2])
        pos_two = GridPos(elts[3], elts[4])
        positions.append(pos_one)
        positions.append(pos_two)
        positions = build(positions)
        ships.append(Ship(type, positions))
    return ships

def get_guesses(file_lines, board):
    '''
    This function gets and makes the guesses.
    Parameters:
    file_lines is a list of all the lines
    in the guess file
    board is a board object representing
    the initial board that is then modified.
    '''
    for line in file_lines:
        # Account for new line at end of file
        if len(line) == 1:
            return
        elts = line.strip("\n").split()
        x = int(elts[0])
        y = int(elts[1])
        gridpos = GridPos(x,y)
        # Make the guess if it is legal
        if guess_is_legal(gridpos):
            board.guess(GridPos(x,y))
        else:
            print("illegal guess")

def guess_is_legal(gridpos):
    '''
    This function determines if a guess is legal,
    that is, if its values are between 0 and 9 inclusive.
    Parameters: gridpos is a GridPos object
    representing the guess to be made
    Returns: a boolean value determining
    if the guess is legal
    '''
    if gridpos._x < 0 or gridpos._x > 9:
        return False
    if gridpos._y > 9 or gridpos._y < 0:
        return False
    return True

def composition(file_lines):
    '''
    This function determines whether the fleet
    composition is correct.
    Parameters: file_lines is a list of all
    the lines in the file. 
    Returns: nothing
    This function is the first of five error
    tests that are run in sequential order
    to determine if the ship placements 
    are valid. 
    '''
    ships = {}
    for line in file_lines:
        # Get the ships and their counts
        if line[0] not in ships:
            ships[line[0]] = 1
        else:
            ships[line[0]] += 1
    # Determine if the ship was not in the file            
    if "A" not in ships or "B" not in ships\
    or "S" not in ships or "D" not in ships\
    or "P" not in ships:
        print("ERROR: fleet composition incorrect")
        sys.exit(0)
    # Determine if there were more than one of any type
    for count in ships.values():
        if count > 1:
            print("ERROR: fleet composition incorrect")
            sys.exit(0)

def bounds(file_lines):
    '''
    This function determines if the ship
    placements are out of bounds. 
    Parameters: file_lines is a list of all
    the lines in the file. 
    Returns: nothing
    This is the second of the two tests run in 
    sequential order to determine if the ship
    placements are valid. 
    '''
    for line in file_lines:
        # Get the numerical values
        nums = line.split()[1:]
        for i in range(len(nums)):
            nums[i] = int(nums[i])
        for val in nums:
            if val < 0 or val > 9:
                print("ERROR: ship out-of-bounds: "\
                      + line)
                sys.exit(0)

def alignment(file_lines):
    '''
    This function determines if the ships
    are horizontal or vertical.
    Parameters: file_lines is a list of all
    the lines in the file
    Returns: nothing
    This is the third of five tests run in sequential
    order to determine if the ship placements are valid.
    This is done by determining if the endpoints
    of the ships have unique numbers for each
    coordinate point.  
    '''
    for line in file_lines:
        nums = line.split()[1:]
        if nums[0] != nums[2] and nums[1] != nums[3]:
            print("ERROR: ship not horizontal or vertical: " + line)
            sys.exit(0)

def overlap(file_lines):
    '''
    This function determines if there are any
    overlapping ships in the file. 
    Parameters: file_lines is a list of all
    the lines in the file.
    Returns: nothing
    This is the fourth of five tests run in sequential
    order to determine if the ship placements are valid. 
    This is done by starting with the first line
    and going through the file to see if there are any
    endpoints that are the same for two different ships. 
    '''
    line = file_lines[0].split()
    gridpos_one = GridPos(line[1],line[2])
    gridpos_two = GridPos(line[3],line[4])
    for i in range(1,len(file_lines)):
        curr_line = file_lines[i].split()
        curr_one = GridPos(curr_line[1], curr_line[2])
        curr_two = GridPos(curr_line[3], curr_line[4])
        if gridpos_one.coords() == curr_one.coords() or\
        gridpos_two.coords() == curr_two.coords():
            print("ERROR: overlapping ship: " + file_lines[i])
            sys.exit(0)

def size(file_lines):
    '''
    This function determines if the size
    of the ship is incorrect. 
    Parameters: file_lines is a list of all
    the lines in the file. 
    Returns: nothing
    This is the fifth and final of the five tests
    run in sequential order to determine if the 
    ship placements are valid. 
    '''
    types = {
        "A":5,
        "B":4,
        "S":3,
        "D":3,
        "P":2
    }
    for line in file_lines:
        elts = line.strip("\n").split()
        # Convert numerical characters to integers
        for i in range(1,len(elts)):
            elts[i] = int(elts[i])
        if elts[0] == "A":
            # Account for vertical ships
            if elts[2] == elts[4]:
                if abs(elts[1] - elts[3]) + 1 != types[elts[0]]:
                    print("ERROR: incorrect ship size: " + line)
                    sys.exit(0)
            # Account for horizontal ships
            elif elts[1] == elts[3]:
                if abs(elts[2] - elts[4]) + 1 != types[elts[0]]:
                    print("ERROR: incorrect ship size: " + line)
                    sys.exit(0)
        elif elts[0] == "B":
            # Account for vertical ships
            if elts[2] == elts[4]:
                if abs(elts[1] - elts[3]) + 1 != types[elts[0]]:
                    print("ERROR: incorrect ship size: " + line)
                    sys.exit(0)
            # Account for horizontal ships
            elif elts[1] == elts[3]:
                if abs(elts[2] - elts[4]) + 1 != types[elts[0]]:
                    print("ERROR: incorrect ship size: " + line)
                    sys.exit(0)
        elif elts[0] == "S":
            # Account for vertical ships
            if elts[2] == elts[4]:
                if abs(elts[1] - elts[3]) + 1 != types[elts[0]]:
                    print("ERROR: incorrect ship size " + line)
                    sys.exit(0)
            # Account for horizontal ships
            elif elts[1] == elts[3]:
                if abs(elts[2] - elts[4]) + 1 != types[elts[0]]:
                    print("ERROR: incorrect ship size " + line)
                    sys.exit(0)
        elif elts[0] == "D":
            # Account for vertical ships
            if elts[2] == elts[4]:
                if abs(elts[1] - elts[3]) + 1 != types[elts[0]]:
                    print("ERROR: incorrect ship size " + line)
                    sys.exit(0)
            # Account for horizontal ships
            elif elts[1] == elts[3]:
                if abs(elts[2] - elts[4]) + 1 != types[elts[0]]:
                    print("ERROR: incorrect ship size " + line)
                    sys.exit(0)
        elif elts[0] == "P":
            # Account for vertical ships
            if elts[2] == elts[4]:
                if abs(elts[1] - elts[3]) + 1 != types[elts[0]]:
                    print("ERROR: incorrect ship size " + line)
                    sys.exit(0)
            # Account for horizontal ships
            elif elts[1] == elts[3]:
                if abs(elts[2] - elts[4]) + 1 != types[elts[0]]:
                    print("ERROR: incorrect ship size " + line)
                    sys.exit(0)

def failed_ship(file_lines):
    '''
    This function runs all the placement error tests.
    Parameters: file_lines is a list of all
    the lines in the file
    Returns: nothing
    '''
    composition(file_lines)
    bounds(file_lines)
    alignment(file_lines)
    overlap(file_lines)
    size(file_lines)

def main():
    '''
    This function runs the program. 
    Parameters: none
    Returns: nothing
    '''
    placement_name = input()
    placement_file = open(placement_name, "r")
    placement_lines = placement_file.readlines()
    failed_ship(placement_lines)
    guess_name = input()
    guess_file = open(guess_name, "r")
    guess_lines = guess_file.readlines()
    # Get the ships and make the guesses
    ships = get_ships(placement_lines)
    board = Board(ships)
    board.place_ships()
    get_guesses(guess_lines, board)

main()