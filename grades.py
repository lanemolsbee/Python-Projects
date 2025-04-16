'''

Lane Molsbee
CSC110
Programming Project 2
9/20/2023
This program contains 4 functions relating to grades,
namely determining letter grade, pass or fail status, 
percentage calculation, and final grade calculation
'''

def letter_grade(grade):
    '''
    This function returns a letter grade for
    a given numerical grade.
    Args:
    grade: a float representing a numerical grade
    Returns:
    A string representing the letter grade.
    '''
    # Determine if the grade is outside the range
    if grade < 0 or grade > 100:
        return "X"
    # Returns a grade of E if the conditions are met
    if 0 <= grade and grade < 60:
        return "E"
    # Returns a grade of D if the conditions are met
    if 60 <= grade and grade < 70:
        return "D"
    # Returns a grade of C if the conditions are met
    if 70 <= grade and grade < 80:
        return "C"
    # Returns a grade of B if the conditions are met
    if 80 <= grade and grade < 90:
        return "B"
    # Returns a grade of A if the conditions are met
    if 90 <= grade and grade <= 100:
        return "A"

def pass_or_fail(letter_grade):
    '''
    This function returns a string representing
    whether the student passed or failed
    Args:
    letter_grade(grade): a string representing
    the letter grade using the letter_grade function
    Returns:
    A string representing whether the student passed or failed
    '''
    # Returns Error if multiple characters are in the string
    if len(letter_grade) != 1:
        return "Error"
    # Each if statement returns pass if the condition was met
    if letter_grade == "A":
        return "Pass"
    elif letter_grade == "B":
        return "Pass"
    elif letter_grade == "C":
        return "Pass"
    elif letter_grade == "D":
        return "Pass"
    # Returns Fail otherwise
    else:
        return "Fail"
    
def point_grade(score, total_points):
    '''
    This function returns the percentage grade.
    Args:
    score: a float representing the total score
    total_points: a float representing the total
    number of points available
    Returns:
    A float representing the percentage rounded
    to two decimal places
    '''
    percentage = (score / total_points) * 100
    return round(percentage, 2)

def get_grade_results(score, total_points):
    '''
    This function returns a string representing
    the student's calculated percentage, letter grade,
    and whether they passed or failed
    Args:
    score: a float representing the total score
    to be used with point_grade to
    calculate the percentage
    total_points: a flaot representing the total
    number of points available, also to be used
    to calculate the percentage
    Returns:
    A string telling the student their percentage,
    letter grade, and whether they passed or failed
    '''
    grade_number = point_grade(score, total_points)
    grade_letter = letter_grade(grade_number)
    pass_status = pass_or_fail(grade_letter)
    full_string = "Your grade is " + str(grade_number) + " "
    full_string = full_string + "(" + grade_letter + " - "
    full_string = full_string + pass_status + ")"
    return full_string