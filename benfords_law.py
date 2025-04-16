'''
Lane Molsbee
CSC110
11/1/2023
This program contains a number of functions to
implement a Benford's Law analysis.
'''

def csv_to_list(file_name):
    '''
    This function takes a file and creates a
    list of all the numbers, integer or float,
    that appeared in the file
    Args:
    file_name: a string representing the file name
    Returns:
    a list of all the numbers that appeared in the file
    '''
    # Open the file in read mode
    file = open(file_name, 'r')
    numbers_list = []
    # Iterate through each line in the file

    for line in file:
        # Create a list of all the strings in the file separated at commas
        nums = line.strip("\n").split(",")
        # Iterate through the list
        for i in range(len(nums)):
            # Determine whether item is numeric or float, and append if so
            if nums[i].isnumeric():
                numbers_list.append(nums[i])
            if "." in nums[i]:
                if nums[i].replace(".", "").isnumeric():
                    numbers_list.append(nums[i])
    file.close()
    return numbers_list

def count_start_digits(numbers):
    '''
    This function keeps track of the number of times a 
    certain number started a value in the list by using a dictionary.
    Args:
    numbers: a list representing a group of numbers
    Returns:
    a dictionary representing the count of each time a number
    started a value in the dictionary
    '''
    number_frequencies = {}
    # Create the initial dictionary where each number appears zero times
    for i in range(1,10):
        number_frequencies[i] = 0
    # Iterate through the list
    for i in range(len(numbers)):
        # Create a digit to correspond to the keys
        digit = int(numbers[i][0])
        # Add to the appropriate key if the first digit was not zero
        if digit != 0:
            number_frequencies[digit] += 1
       
    return number_frequencies
    
def digit_percentages(counts):
    '''
    This function creates a dictionary representing
    the percentage of a number frequency to the total
    amount of number frequencies
    Args:
    counts: a dictionary representing the frequency
    a particular number began a value in the data set
    Returns:
    a dictionary representing the percentage of a particular
    number's frequency to the total frequency count
    '''
    # Create the dictionary, using a loop
    percentages = {}
    for i in range(1, 10):
        percentages[i] = 0
    # Create the total frequencies, loop through the input dictionary to find it
    total = 0
    for key in counts:
        total += counts[key]
    # Loop through the input dictionary and calculate percentages rounded to 2 places
    for key in counts:
        percentages[key] = round((counts[key] / total) * 100,2)
    return percentages

def check_benfords_law(percentages):
    '''
    This function determines whether the data satisfies Benford's law.
    Args:
    percentages: a dictionary representing the percentage of the whole
    that a certain number frequency occupied
    Returns:
    a boolean determining whether Benford's law was satisfied
    '''
    # Determine if the 1-percentage falls between 25 and 40 inclusive
    if (25 <= percentages[1] and percentages[1] <= 40) != True:
        return False
    # Determine if the 2-percentage falls between 12 and 27 inclusive
    if (12 <= percentages[2] and percentages[2] <= 27) != True:
        return False
    # Determine if the 3-percentage falls between 7 and 22 inclusive
    if (7 <= percentages[3] and percentages[3] <= 22) != True:
        return False
    # Determine if the 4-percentages falls between 4 and 19 inclusive
    if (4 <= percentages[4] and percentages[4] <= 19) != True:
        return False
    # Determine if the 5-percentage falls between 2 and 17 inclusive
    if (2 <= percentages[5] and percentages[5] <= 17) != True:
        return False
    # Determine if the 6-percentage falls between 1 and 16 inclusive
    if (1 <= percentages[6] and percentages[6] <= 16) != True:
        return False
    # Determine if the 7- and 8-percentages fall between 0 and 15 inclusive
    if (0 <= percentages[7] and percentages[7] <= 15) != True:
        return False    
    if (0 <= percentages[8] and percentages[8] <= 15) != True:
        return False
    # Determine if the 9-percentage falls between 0 and 14 inclusive
    if (0 <= percentages[9] and percentages[9] <= 14) != True:
        return False
    # Return True assuming all the conditions above were true
    return True

