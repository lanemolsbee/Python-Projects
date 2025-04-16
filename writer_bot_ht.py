'''
File: writer_bot_ht.py
Author: Lane Molsbee
Course: CSC 120, Spring 2024
Purpose: This program behaves the same way as writer_bot.
It reads a text file and generates a dictionary of prefixes
for words, and uses the statistical properties of the 
file's words to generate random text of a specified length.
However, this program uses a HashTable ADT in order to do this.
'''
import random
import sys
NONWORD = "@"
SEED = 8
class HashTable:
    '''
    This class represents a hash table. 
    Its primary methods are _hash, put, and get. 
    It is to be constructed using an integer.
    This class contains the dictionary that stores
    the word prefixes and their suffixes
    in order to generate the random text. 
    It maintains a list of keys with the words
    in the order they appear in the file,
    broken up using the prefix lengths. 
    For processing, this makes it easier to access
    the keys in the dictionary by just seeing
    if the current prefix is in the list of keys.
    '''
    def __init__(self, size):
        '''
        This is the class constructor. 
        Parameters:
        size is an integer representing the size of the hash table.
        Returns:
        nothing
        '''
        self._pairs = [None] * size
        self._size = size
        self._keys = []
    def _hash(self, key):
        '''
        This is the class hashing function. 
        Parameters:
        key is a string representing a dictionary key
        Returns:
        an integer representing index for the key to be placed at.
        This function uses polynomials in order to generate
        the hash value for the key. 
        '''
        p = 0
        for c in key:
            p = 31 * p + ord(c)
        return p % self._size
    def put(self, key, value):
        '''
        This function inserts a key-value pair into the table.
        Parameters:
        key is a string reprsenting the dictionary key
        value is a string representing the dictionary value
        '''
        i = self._hash(key)
        # Use linear probing to find the insertion spot
        if self._pairs[i] != None:
            if self._pairs[i][0] == key:
                return
            while True:
                i -= 1
                if i < 0:
                    i = len(self._pairs) - 1
                if self._pairs[i] == None:
                    break
        self._pairs[i] = [key, [value]]
            
    def add_key(self, key):
        self._keys.append(key)

    def get(self, key):
        '''
        This function retrieves the list associated with a key.
        Parameters:
        key is a string representing the key to be accessed.
        Returns:
        the value associated with that key in the Hash Table
        '''
        i = self._hash(key)
        if self._pairs[i] != None and self._pairs[i][0] == key:
            return self._pairs[i][1]
        else:
            # If the value reaches none, the key was never inserted
            while self._pairs[i] != None:
                if self._pairs[i][0] == key:
                    return self._pairs[i][1]
                i -= 1
            return None
    def keys(self):
        return self._keys
    def __contains__(self, key):
        '''
        This is the class __contains__ function.
        Parameters:
        key is the key to be searched for
        Returns:
        a boolean value representing whether the key
        is in the hash table. 
        '''
        if self.get(key) != None:
            return True
        return False
    
    def __str__(self):
        '''
        This is the class __str__ method
        Parameters: none
        Returns: a string representation of the hash table. 
        '''
        converted = "{"
        for i in range(len(self._pairs)):
            if self._pairs[i] == None:
                converted += "None, "
            else:
                converted += str(self._pairs[i]) + ", "
        converted += "}"
        return converted
    
    def __repr__(self):
        '''
        This is the class __repr__ method
        Parameters: none
        Returns: a string representation of the hash table. 
        '''
        converted = "{"
        for i in range(len(self._pairs)):
            if self._pairs[i] == None:
                converted += "None, "
            else:
                converted += str(self._pairs[i]) + ", "
        converted += "}"
        return converted

# Copied from writer_bot
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
# Copied from writer_bot
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


def build(table_size, prefix_size, words):
    '''
    This function builds the hash table. 
    Parameters:
    table_size is an integer representing the size of the table
    prefix_size is an integer representing the size
    of the prefixes to be used in the table
    words is a list of words to be processed and added
    to the table as key-value pairs. 
    This function is vital to the overall functioning of this program
    as it is what builds the dictionary that is used to
    generate the random text. 
    '''
    # Create the prefix of only the NONWORD characters
    base = []
    for i in range(prefix_size):
        base.append(NONWORD)
    # Use a tuple to make it easier to shift
    tup = tuple(base)
    prefixes = HashTable(table_size)
    prefixes._keys.append(" ".join(tup))
    i = 0
    prefixes.put(" ".join(tup), words[0])
    # Loop through the file to build
    while i < len(words) - 1:
        tup = shift_tuple(tup, words[i])
        prefixes._keys.append(" ".join(tup))
        string_tup = " ".join(tup)
        if string_tup not in prefixes:
            prefixes.put(string_tup, words[i + 1])
        else:
            prefixes.get(string_tup).append(words[i + 1])
        i += 1
    return prefixes

def generate(words_left, table):
    '''
    This functin generates the random text.
    Parameters:
    words_left is an integer representing the number of
    words to be put into the random text, assuming that
    the prefixes created are always in the table.
    table is a HashTable object representing the dictionary
    to be used to generate the text. 
    Returns: a list tlist that contains all the random
    words that are to be printed. 
    '''
    tlist = []
    curr_prefix = None
    for key in table._keys:
        # Get the first prefix with no non-words
        if NONWORD not in key:
            curr_prefix = key
            break
    for x in curr_prefix.split():
        tlist.append(x)
    words_left -= len(curr_prefix.split())
    # Tuple keeps track of the current prefix
    tup = tuple(curr_prefix.split())
    add_value = None
    while curr_prefix in table._keys and words_left > 0: 
        if len(table.get(curr_prefix)) == 1:
            add_value = table.get(curr_prefix)[0]
            tup = shift_tuple(tup, add_value)
            tlist.append(add_value)
            curr_prefix = " ".join(tup)
            words_left -= 1
        else:   
            rand = random.randint(0, len(table.get(curr_prefix)) - 1)
            add_value = table.get(curr_prefix)[rand]
            tlist.append(add_value)
            tup = shift_tuple(tup, add_value)
            curr_prefix = " ".join(tup)
            words_left -= 1
    return tlist

# Copied from writer_bot
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
        built_string += str(rand_text[i]) + " "
    print(built_string)


def main():
    '''
    This is the main function of the file. 
    Parameters: none
    Returns: nothing
    '''
    random.seed(SEED)
    file_name = input()
    table_size = int(input())
    prefix_size = int(input())
    if prefix_size < 1:
        print("ERROR: specified prefix size is less than one")
        sys.exit(0)
    words_to_generate = int(input())
    if words_to_generate < 1:
        print("ERROR: specified size of the generated text is less than one")
        sys.exit(0)
    sfile = open(file_name, 'r')
    words = get_words(sfile)
    table = build(table_size, prefix_size, words)
    sfile.close()
    generated_words = generate(words_to_generate, table)
    print_text(generated_words)

main()