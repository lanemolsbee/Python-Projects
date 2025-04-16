def load_game():
    '''
    This function loads the current state of the game.
    Args:
    None
    Returns:
    a dictionary representing a given value for the beginning
    of a line and all the values associated with that line.
    '''
    # Open the file in read mode and create the dictionary
    game_file = open("game.txt", "r")
    game = {}
    # Loop through the file, stripping new lines and splitting at tabs
    for line in game_file:
        line_words = line.strip("\n").split("\t")
        starting_int = int(line_words[0])
        # Create a new key-value pair for the dictionary
        if starting_int not in game:
            game[starting_int] = []
        # Append the rest of the line associated with a given key value         
        game[starting_int].append(line_words[1])
    game_file.close()
    return game

def load_objects():
    '''
    This function loads the objects in the game
    Args:
    None
    Returns:
    a dictionary with a tuple representing the first two
    integer values in a line and the first string, mapped to
    a list containing the rest of the values in that line
    that were separated by tabs
    '''
    # Open the file in read mode and create the dictionary
    object_file = open("objects.txt", "r")
    objects = {}
    # Iterate through the file, stripping new lines and splitting at tabs
    for line in object_file:
        line_words = line.strip("\n").split("\t")
        # Create a tuple consisting of the first two integer values and the first string
        values_tuple = (int(line_words[0]), int(line_words[1]), line_words[2])
       
        objects[values_tuple] = []
        # Iterate through the created list starting at index three to account for tabs
        for i in range(3, len(line_words)):
            objects[values_tuple].append(line_words[i])
    object_file.close()
    return objects

def load_travel_table():
    '''
    This function loads the travel table.
    Args:
    None
    Returns:
    A dictionary representing the travel table
    '''
    # Open the file in read mode and create the dictionary
    travel_file = open("travel_table.txt", "r")
    travel_table = {}
    # Iterate through the file, stripping new lines and splitting at tabs
    for line in travel_file:
        line_words = line.strip("\n").split("\t")
        # Create a tuple consisting of the first two integers
        values_tuple = (int(line_words[0]), int(line_words[1]))
        # Append the last string in the line
        travel_table[values_tuple] = line_words[2]

    travel_file.close()
    return travel_table

def print_instructions():
    '''
    This function prints the game instructions.
    Args:
    None
    Returns:
    Nothing
    '''
    # Open the file in read mode.
    f = open("instructions.txt", "r")
    # Iterate through the file, stripping new lines and printing each file line
    for line in f:
        line_words = line.strip("\n")
        print(line_words)
    f.close()

def get_location(location, game, objects, player_objects):
    '''
    This function gets the next location from the game data.
    It doesn't return anything, it prints messages related to
    objects (if the user has them or not) and location information
    Args:
        location: integer
        game: dictionary with location and string information
        objects: dictionary of location, binary (0 or 1), and object name
        player_objects: list of strings
    Returns:
        None
    '''
    # for each string associated with that location in the game
    # dictionary, print that line
    for line in game[location]:
        print(line)

    # check if location has an object associated with it
    for key, value in objects.items():
        # if there's an object associated with this location
        # and the possible action is to take it (0)
        # and user hasn't taken it yet, print message associate with
        # object
        if key[0] == location and key[1] == 0 and key[2] not in player_objects:
            print(value[0])

        # if there's an object associated with this location
        # and we need to check if the user has it (1)
        if key[0] == location and key[1] == 1:
            if key[2] in player_objects:
                # user has the object
                print(value[1])
            else:
                # user does not have the object
                print(value[0])


def go_to_location(location, travel_table, objects, player_objects, answer):
    '''
    This function checks for the user's input (their answer), the objects
    that are available for the users to take, and the objects the user
    has in their object list
    Args:
        location: integer
        travel_table: dictionary with current location, possible to go
                      location and verb that takes user to to go location
        objects: dictionary of location, binary (0 or 1), and object name
        player_objects: list of strings
        answer: input from the user (string)
    Returns:
        next location (integer)
    '''
    # check if user wants to take an object
    if "take" in answer.lower():
        for key in objects:
            # check if there's an object to take
            if key[0] == location and key[1] == 0:
                # add object to user's object list
                player_objects.append(key[2])

    # check if the user needs to have an object to proceed
    for key in objects:
        # if there's a needed object for this location
        # but the user does not have it, return current location 
        # meaning the user doesn't go anywhere
        if key[0] == location and key[1] == 1 and key[2] not in player_objects:
            return location

    # no objects to take or needed to go anywhere
    # check where to go based on user's answer
    for x_y, verb in travel_table.items():
        if x_y[0] == location and verb in answer.upper():
            return x_y[1]


def play_game():
    '''
    This function is the main game playing function.
    It loads all text files for the game, and asks
    for the player's input
    '''
    # load game.txt
    game = load_game()
    # load objects.txt
    objects = load_objects()
    # load travel_table.txt
    travel_table = load_travel_table()
    # player starts with no objects
    player_objects = []
    # player starts at location 0
    location = 0
    # get info for location 0
    get_location(location, game, objects, player_objects)
    # ask if player wants instructions
    answer = input("> ")
    if "y" in answer.lower():
        print_instructions()
    # go to location 1 (start game for real)
    location += 1
    # this is just a demo with 11 locations
    while location < 12:
        # print info on current location
        get_location(location, game, objects, player_objects)
        # request player input
        answer = input("> ")
        # extra line break
        print()
        # player can exit at any time by inputting "exit"
        if "exit" not in answer.lower():
            # player doesn't want to exit
            # get next location based on player's input
            where_to_go = go_to_location(location, travel_table, objects, 
                                      player_objects, answer)
            # if a possible location was found
            if where_to_go:
                # change location
                location = where_to_go
        else: # user entered "exit"
            location = 12
    print("This is the end of this game demo.")


print_instructions()