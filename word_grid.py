'''
File: word_grid.py
Author: Lane Molsbee
Course: CSC120, Spring 2024
Purpose: this program contains functions to create
a grid of random letters
'''
import random

def init():
    '''
    This function takes user input to determine a value for
    the grid size and to seed a random number generator
    Parameters: none
    Returns: an integer representing the size of the square grid.
    '''
    grid_size = int(input())
    seed_value = input()
    random.seed(seed_value)
    return grid_size

def make_grid(grid_size):
    '''
    This function makes the grid, filling each available
    spot with randomly generated letters based on numbers
    '''
    grid = []
    # Iterates until the number of columns and rows is equal to the grid size
    for i in range(grid_size):
        letters_list = []
        for j in range(grid_size):
            number = random.randint(0,25)
            letter = number2letter(number)
            letters_list.append(letter)
            
        grid.append(letters_list)

    return grid
    
def print_grid(grid):
    '''
    This function prints the grid.
    Parameters: none
    Returns: nothing
    '''
    # Use the join function to print each row of the grid
    for i in grid:
        print(",".join(i))
        

def number2letter(n):
    '''
    This function uses a number and matches it to a letter
    of the alphabet.
    Parameters: n is an integer representing a string index
    Returns: the letter n corresponds to in the alphabet
    '''
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return alphabet[n]

def main():
    '''
    This function takes user input to create and print a grid
    using the other functions
    Parameters: none
    Returns: nothing
    '''
    grid_size = init()
    grid = make_grid(grid_size)
    print_grid(grid)

main()
    



