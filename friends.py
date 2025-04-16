'''
File: friends.py
Author: Lane Molsbee
Course: CSC 120, Spring 2024
Purpose: this program tests the 
LinkedList and Node classes and uses them
to determine the friends in common between
two people from a text file. 
'''
from linked_list import *

def main():
    '''
    This function uses user input to fulfill
    the function of the program.
    Parameters: None
    Returns: nothing
    This is the only function in this file
    and it exists to use the LinkedList
    and Node classes to perform the overall
    function of the program. 
    '''
    # File processing
    friends_list = LinkedList()
    file_name = input('Input file: ')    
    file = open(file_name, 'r')
    for line in file:
        people = line.strip().split()
        friends_list.add_person(people[0])
        friends_list.add_person(people[1])
        friends_list.add_to_list(people[0], people[1])
        friends_list.add_to_list(people[1], people[0])
    
    person_one = input('Name 1: ')
    person_two = input('Name 2: ')
    file.close()
    # Error trap
    if person_one not in friends_list:
        print("ERROR: Unknown person", person_one)
        return
    elif person_two not in friends_list:
        print("ERROR: Unknown person", person_two)
        return
    
    # Find and print the friends in common. 
    friends_list = friends_list.friends_in_common(person_one, person_two)    
    friends_list.sort()
    current = friends_list._head
    if current == None:
        return
    print("Friends in common:")
    while current != None:
        print(current.name())
        current = current._next
    

main()
