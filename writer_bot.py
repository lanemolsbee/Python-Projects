'''
File: writer_bot.py
Author: Lane Molsbee
Course: CSC 120, Spring 2024
Purpose: This program utilizes
the Markov Chain Analaysis algorithm
in order to generate random text
based on word statistics in a file. 
It utilizes tuple prefixes and analyzes
the frequency with which certian word prefix
and suffix pairs occur. 
'''
import random
# Every word must have a prefix
NONWORD = " "
SEED = 8
random.seed(SEED)
def get_words(file):
    '''
    This function iterates through a file
    object and gets all the words in it. 
    Parameters: 
    file is a file object with text
    Returns: a list of all the words
    in the file.
    Its main purposes is to get a list
    of the words so that a dictionary
    of prefixes and suffixes can be made.
    '''
    words = []
    for line in file:
        elements = line.strip().split()
        for word in elements:
            words.append(word)
    return words

def shift_tuple(tup, value):
    '''
    This function takes a tuple of length
    n and shifts it.
    Parameters: 
    tup is a tuple of length n
    value is a new value to be added
    Returns: a new tuple such that
    its elements are the n to n - 1
    elements of tup and finally the
    value that is added. 
    This function is vital for getting
    all the prefixes of a specified length
    from the file. 
    '''
    first_elts = list(tup[1:len(tup)])
    first_elts.append(value)
    return tuple(first_elts)

def build(n, words):
    '''
    This function constructs the dictionary
    require to generate the random text.
    Parameters:
    n is an integer specifying the length
    of the tuple prefix.
    words is a list of all the words in the file.
    Returns:
    a dictionary such that every word in the file
    has a prefix and each prefix of length n
    maps to a list of words that follow that prefix. 
    '''
    base = []
    # Construct the prefix of nonword and first word
    for i in range(n):
        base.append(NONWORD)
    tup = tuple(base)
    prefixes = {}
    i = 0
    # Set the nonwords prefix to have a suffix of the first word
    prefixes[tup] = [words[0]]
    
    while i < len(words) - 1:
        # Shift to next prefix
        tup = shift_tuple(tup, words[i])
        if tup not in prefixes:
            prefixes[tup] = [words[i + 1]]
        else:
            # Accounts for multiplicity of pre-suf pair.
            prefixes[tup].append(words[i + 1])
        i += 1
    return prefixes
    
def generate(words_left, table):
    '''
    This function generates the random text.
    Parameters:
    words_left is an integer representing
    the amount of words to be generated.
    table is a dictionary representing
    the prefix-suffix pairs in the file. 
    Returns:
    a list of randomly generated words
    This function is the backbone of the program
    and generates all the random text to
    be printed. 
    '''
    tlist = []
    # First two words are first two in the file.
    for key in table:
        if NONWORD not in key:
            tup = key
            break
    for x in tup:
        tlist.append(x)
    words_left -= len(tup)
    # Generate the rest of the text
    while tup in table and words_left > 0:
        if len(table[tup]) == 1:
            tlist.append(table[tup][0])
            tup = shift_tuple(tup, table[tup][0])
        else:
            rand = random.randint(0,len(table[tup]) - 1)
            print(str(rand))
            tlist.append(table[tup][rand])
            tup = shift_tuple(tup, table[tup][rand])
        words_left -= 1
    return tlist
    
def print_text(rand_text):
    '''
    This function prints the text such that
    each line has at most ten words.
    Parameters:
    rand_text is a list of the randomly
    generated words from the file.
    Returns: nothing
    '''
    built_string = ''
    for i in range(len(rand_text)):
        # Print and break if it's the tenth word.
        if i != 0 and i % 10 == 0:
            print(built_string)
            built_string = ""
        built_string += rand_text[i] + " "
    print(built_string)
        
def main():
    '''
    This function takes the input
    to build the randomly generated text. 
    Parameters:
    none
    Returns: Nothing
    '''
    file_name = input()
    tup_size = int(input())
    words_to_generate = int(input())
    sfile = open(file_name, 'r')
    words = get_words(sfile)
    table = build(tup_size, words)
    rand_text = generate(words_to_generate, table) 
    print_text(rand_text)

main()   