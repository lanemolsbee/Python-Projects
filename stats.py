'''
Lane Molsbee
CSC110
10/5/2023
This program contains several functions
for calculating mean, variance, 
standard deviation, and range
'''

def mean(numbers):
    '''
    This function calculates the mean
    of a list of numbers
    Args:
    numbers: a list containing a list of numbers
    Returns:
    The average value of the list variable numbers
    rounded to two decimal places
    '''
    mean = 0
    # Assigns an index variable and iterates through the list
    i = 0
    while i < len(numbers):
        mean += numbers[i]
        i += 1
    # Finishes the mean calculation and returns the rounded value
    mean = mean / len(numbers)
    return round(mean, 2)

def variance(numbers):
    '''
    This function calculates the variance
    of a list of numbers.
    Args:
    numbers:  list containing a list of numbers
    Returns:
    The variance of the list variable numbers
    rounded to two decimal places
    '''
    mean_value = mean(numbers)
    var = 0
    # Assigns an index and iterates through the list
    i = 0
    while i < len(numbers):
        var += (numbers[i] - mean_value) ** 2
        i += 1
    # Finishes the variance calculation and returns the rounded value
    var = var / (len(numbers) - 1)
    return round(var, 2)

def sd(numbers):
    '''
    This function calculates the standard
    deviation of a list of numbers.
    Args:
    numbers: list containing a list of numbers
    Returns:
    The standard deviation of the list of numbers
    '''
    var = variance(numbers)
    standard_deviation = var ** (0.5)
    return round(standard_deviation, 2)

def list_range(numbers):
    '''
    This function returns the range of a list
    of numbers.
    Args:
    numbers: a list containing a list of numbers
    Returns:
    The range of the list of numbers
    '''
    max_value = numbers[0]
    min_value = numbers[0]
    # Assigns index and iterates to determine max value
    i = 0
    while i < len(numbers):
        if numbers[i] > max_value:
            max_value = numbers[i]
        i += 1
    # Reassigns index and iterates to determine min value
    i = 0
    while i < len(numbers):
        if numbers[i] < min_value:
            min_value = numbers[i]
        i += 1
    # Calculate the range of the list
    range_of_list = max_value - min_value
    return range_of_list



