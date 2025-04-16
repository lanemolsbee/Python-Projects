'''
File: rhymes.py
Author: Lane Molsbee
Course: CSC120, Spring 2024
Purpose: This program reads in a file 
with a name supplied by the user. 
It then prints all the words that rhyme
with each pronunciation of the supplied word. 
'''
def read_file(file_name):
    '''
    This function reads in a file of words
    and their pronunciations.
    Parameters:
    file_name is a string representing the name of the file to be read
    Returns:
    a dictionary where each key is a word and each key
    maps to a 2D list where each sublist is a list
    containing the phonemes of each possible pronunciation
    '''
    file = open(file_name, "r")
    words = {}
    for line in file:
        parts = line.split()
        # Add a new word and its first pronunciation
        if parts[0] not in words:
            words[parts[0]] = []
            words[parts[0]].append(parts[1:len(parts)])
        # Add a new pronunciation to an existing word
        else:
            words[parts[0]].append(parts[1:len(parts)])
    file.close()
    return words

def collect_rhymes(words, word):
    '''
    This function determines the words that
    rhyme with every pronunication of the given word
    Parameters:
    words is a dictionary where each key is a word
    and each key maps to a 2D list with each
    sublist being a pronunciation of the key
    word is a string that represents a word
    to be used in determining rhymes
    Returns:
    A list containing the rhyming words found
    sorted alphabetically and in all upper-case
    '''
    all_pronunciations = []
    rhyming_words = []
    # Create a list of all pronunciations of the input word
    for key in words:
        if key == word:
            for i in range(len(words[key])):
                all_pronunciations.append(words[key][i])
    # Cycle through the pronunciation dictionary
    for key in words:
        # Cycle through each pronunciation
        for pro in words[key]:
            # Compare to each pronunciation of input word
            for x in all_pronunciations:
                if does_rhyme(x, pro):
                    rhyming_words.append(key)
    
    rhyming_words = sorted(rhyming_words)
    for i in range(len(rhyming_words)):
        rhyming_words[i] = rhyming_words[i].upper()
    return rhyming_words

def does_rhyme(first_pro, second_pro):
    '''
    This function takes two lists of phonemes
    and determines if the two lists would
    form words that have a perfect rhyme
    Parameters:
    first_pro is a list containing the phonemes of a word
    second_pro is a list containing the phonemes of the second
    Returns:
    True if the words form a perfecy rhyme and False otherwise
    '''
    # Create the tail and head of the first word
    first_tail = []
    first_head = []
    for i in range(len(first_pro)):
        if len(first_pro[i]) == 3:
            if first_pro[i][2] == "1":
                # Start with the index and move to the end of the list
                for i2 in range(i, len(first_pro)):
                    first_tail.append(first_pro[i2])
                if i != 0:
                    # Create the head if there is one
                    for i3 in range(0, i):
                        first_head.append(first_pro[i3])
    # Create the head and tial for the second word
    second_tail = []
    second_head = []
    for i in range(len(second_pro)):
        if len(second_pro[i]) == 3:
            if second_pro[i][2] == "1":
                # Start with the index and move to the end of the list
                for i2 in range(i, len(second_pro)):
                    second_tail.append(second_pro[i2])
                if i != 0:
                    # Create the head if there is one
                    for i3 in range(0, i):
                        second_head.append(second_pro[i3])
    # Determien if the tails are equal and heads are not
    if first_tail == second_tail and first_head[-1:] != second_head[-1:]:
        return True
    return False

def main():
    '''
    This function takes user input to open a file
    and print all the words that rhyme with each
    pronunciation of the given word.
    '''
    # Create the pronunciation dictionary
    file_name = input()
    pros_dict = read_file(file_name)
    
    word = input()
    word = word.upper()
    # Collect all the rhyming words 
    rhyme_words = collect_rhymes(pros_dict, word)
    for x in rhyme_words:
        print(x)

main()




