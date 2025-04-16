'''
File: word_search.py
Author: Lane Molsbee
Course: CSC120, Spring 2024
Purpose: This program simulates a word search game.
It contains functions for reading in the word list and grid
from a file as well as determining whether a given
word found in the grid is contained in the list and is
at least three characters long. It searches
horizontally left to right and right to left
as well as vertically up and down. Only top left 
to bottom right diagonals are considered. 
'''
def get_word_list(file_name):
    '''
    Read in the word list from a file.
    Parameters: file_name is a string that
    represents the name of the file
    Returns: a list containing all the words
    in the read-in file. 
    '''
    file = open(file_name, "r")
    word_list = []
    for line in file:
        word_list.append(line)
    return word_list
    

def read_letters_file(file_name):
    '''
    Reads in a grid with elements separated by spaces,
    stripping the spaces (for ease of searching).
    Parameters: file_name is a string representing
    the name of the text file containing the grid.
    Returns: a 2D list representing the grid
    '''
    file = open(file_name, "r")
    grid = []
    for line in file:
        letters = line.strip().split(" ")
        grid.append(letters)
    
    return grid

def occurs_in(substr, word_list):
    '''
    Determines if a string occurs in the list of words
    Parameters:
    substr is a string representing a word
    that could occur in the list
    word_list is a list representing 
    the words
    Returns: a boolean determining whether
    substr is a word in word_list
    '''
    find_word = substr.lower()
    for x in word_list:
        compare_word = x.lower()
        if find_word == compare_word:
            return True
    return False

def is_legal(word):
    '''
    Determines if a word contains at least 3 letters
    Parameters: word is a string
    Returns: a boolean representing whether the word 
    contains at least 3 letters
    '''
    status = False
    if len(word) >= 3:
        status = True
    return status
    
def search_horizontal(word_list, grid):
    
    '''
    Searches a grid row by row, determining every possible
    substring of each list going left to right and right to left,
    and then determining if each substring is legal and occurs in the
    list of words.
    Parameters:
    word_list is a list containing the list of words
    grid is a 2D list representing the grid
    '''
    found_words = []
    words = []
    # loop through the list and strip each character of new lines
    for i in range(len(word_list)):
        words.append(word_list[i].strip("\n"))
    for i in range(len(grid)):
        # Length determines the length of the substring
        for length in range(0, len(grid[i])):
            # Subtract length from the rest of the row
            for x in range(0, len(grid[i]) - length):
                sub = concat_elements(grid[i], x, length + x)
                # Strip new lines to avoid skipping characters
                sub = sub.strip("\n")                
                if occurs_in(sub, words) and is_legal(sub):
                    found_words.append(sub)
        # Reverses each row and strips new lines
        row = grid[i]
        for i in range(len(row)):
            row[i] = row[i].strip("\n")
        reversed_list = row[::-1]
                
        # The variable rev_length also determines substring length 
        for rev_length in range(0, len(reversed_list)):
            # Subtract length from the rest of the row
            for x2 in range(0, len(reversed_list) - rev_length):
                sub = concat_elements(reversed_list, x2, rev_length + x2)
                if occurs_in(sub, words) and is_legal(sub):
                    found_words.append(sub)
    return found_words   
           

def concat_elements(slist, startpos, stoppos):
    '''
    Concatenates elements of a list together based on certain
    index ranges
    Parameters:
    slist: a list of strings
    startpos: an integer representing the starting
    position for concatenation
    stoppos: an integer representing the ending
    position for concatenation
    '''
    concat_string = ""
    # Handles it when both arguments are out of bounds
    if startpos < 0 and stoppos >= len(slist):
        # Concatenate every element of the list
        for i in range(0, len(slist)):
            concat_string += str(slist[i])
    # Handles when startpos is out of bounds
    elif startpos < 0:
        for i in range(0, stoppos + 1):
            concat_string += str(slist[i])
    # Handles when stoppos is out of bounds
    elif stoppos >= len(slist):
        for i in range(startpos, len(slist)):
            concat_string += str(slist[i])
    # Handles when startpos is greater than stoppos
    elif startpos > stoppos:
        return ""
    else:
        # When arguments are within the intended ranges
        for i in range(startpos, stoppos + 1):
            concat_string += str(slist[i])
        
                
    return concat_string

def column2list(grid, n):
    '''
    Converts a column in a list to a horizontal list
    Parameters:
    grid: a 2D list representing a grid of elements
    n: an integer representing which column to convert
    '''
    position_list = []    
    for i in range(len(grid)):
        # Prevents n from being outside the number of columns
        if n < len(grid[i]): 
            # Since n is fixed, appends elements of a fixed column
            position_list.append(grid[i][n])
    return position_list

def search_vertical(word_list, grid):
    '''
    Searches each column up and down
    Parameters:
    word_list is a list of words
    grid is a 2D list containing various letters
    '''
    found_words = []
    converted_grid = []
    # Uses a variable n to loop through each column and append it as list
    for n in range(len(grid)):
        converted_grid.append(column2list(grid, n))
    # Search as a horizontal list
    found_words = search_horizontal(word_list, converted_grid)
    return found_words
        
def search_diagonal(word_list, grid):
    found_words = []
    diagonals = []
    substring = ""
    words = []
    # loop through the list and strip each character of new lines
    for i in range(len(word_list)):
        words.append(word_list[i].strip("\n"))
    # Iterate through the main diagonal (top left to bottom right corner)
    for i in range(len(grid)):
        substring += grid[i][i]
    diagonals.append(substring)
   
    substring = ""
    
    # Iterate through all diagonals below the main one
    for i in range(1, len(grid) - 2):
        for j in range(0, len(grid[i]) - i):
            substring += grid[j + i][j]
        diagonals.append(substring)
        substring = ""
    
    
    # Iterate through all diagonals above the main one
    for i in range(1, len(grid) - 2):
        for j in range(0, len(grid[i]) - i):
            substring += grid[j][j + i]
        diagonals.append(substring)
        substring = ""
    
    
    for i in range(len(diagonals)):
        # Length determines the length of the substring
        for length in range(len(diagonals[i])):
            # Subtract length from the rest of the row
            for x in range(0, len(diagonals[i]) - length):
                sub = concat_elements(diagonals[i], x, length + x)
                # Strip new lines to ensure characters aren't skipped
                sub = sub.strip("\n")                
                if occurs_in(sub, words) and is_legal(sub):
                    found_words.append(sub)
    
    return found_words




def main():
    '''
    This function reads in an input word list and grid, 
    and then searches the grid using various other functions
    to determine all the words, in alphabetical order,
    of the list that appeared in the grid. 
    '''
    words_file = input()
    grid_file = input()    
    word_list = get_word_list(words_file)   
    letters_grid = read_letters_file(grid_file)
    all_words = []
    horizontal_words = search_horizontal(word_list, letters_grid)
    vertical_words = search_vertical(word_list, letters_grid)
    diagonal_words = search_diagonal(word_list, letters_grid)
    for x in horizontal_words:
        all_words.append(x)
    for x in vertical_words:
        all_words.append(x)
    for x in diagonal_words:
        all_words.append(x)
    all_words = sorted(all_words)
    for x in all_words:
        print(x)

main()