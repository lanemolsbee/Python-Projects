'''
Author: Lane Molsbee
Class: CSC120 Spring 2024
Purpose: This program determines which Pokemon type(s)
have the greatest average value for any given stat
that the user provides
'''
def read_csv():
    '''
    This function reads in a CSV file and creates
    a dictionary wherein each key is a certain Pokemon type,
    and each key  maps to another dictionary where the keys
    are Pokemon names that map to a list containing the
    stats of that particular Pokemon.
    Parameters:
    none
    Returns: a 2-level dictionary that conforms
    to the specifications described above
    '''
    file_name = input()
    file = open(file_name, "r")
    data = {}
    
    for line in file:
        words = line.split(",")
        # Ensures the first line is skipped
        if words[0] != "#":
            # The second index corresponds to the type
            if words[2] not in data:
                data[words[2]] = {}
                # The [4:10] slicing includes only the stats
                data[words[2]][words[1]] = words[4:11]
            else:
                data[words[2]][words[1]] = words[4:11]
    file.close()
    return data



def compute_stats(data_dict):
    '''
    This function computes the average stats across Pokemon types.
    It creates a dictionary wherein each key is a Pokemon type,
    and each key maps to a list containing the average stat
    values for that type
    Parameters: data_dict is a 2D dictionary wherein
    the keys are Pokemon types and each key maps to a dictionary
    where the keys are Pokemon names; each subkey maps
    to a list containin the stats for that Pokemon
    Returns: a dictionary stats_dict where each key
    is a Pokemon type that maps to a list containing
    the average stat values for Pokemon across that type
    '''
    stats_dict = {}
    for key in data_dict:
        stats_dict[key] = []
    
    for key in data_dict:
        # Determines the number of pokemon of each type
        num_pokemon = len(data_dict[key])
        total = 0
        # Outer loop goes through each stat
        for i in range(0,7):
            total = 0
            # Inner loop goes through each pokemon
            for subkey in data_dict[key]:
                total += int(data_dict[key][subkey][i])
            average = total / num_pokemon
            stats_dict[key].append(average)
    # print(stats_dict)
    return stats_dict

def find_greatest(stats_dict):
    '''
    The greatest_stats dictionary will itself contain as
    keys the various stat types, which map to a tuple
    containing a list of all the types that have the 
    highest stat as the first element 
    '''
    greatest_stats = ["total", "hp", "attack", "defense", "specialattack",
                      "specialdefense", "speed"]
    greatest_stats_dict = {}
    # Iterate through each stat, in order of greatest_stats
    for i in range(0,7):
        # Create a standin list that will be immediately removed
        types = ["standin"]
        max_value = 0
        # Consider each Pokemon type
        for key in stats_dict:
            if stats_dict[key][i] > max_value:
                # Destroy the list if a new greatest stat is found
                for x in types:
                    types.remove(x)
                # Start a new list with the new type and stat
                types.append(key)
                max_value = stats_dict[key][i]
            # Append a new type to the list if the max stats were equal
            elif stats_dict[key][i] == max_value:
                types.append(key)
        greatest_stats_dict[greatest_stats[i]] = (sorted(types), max_value)
    


    # print(greatest_stats_dict)
    return greatest_stats_dict

def main():
    # Create the greatest_stats dictionary
    poke_dict = read_csv()
    stats = compute_stats(poke_dict)
    greatest_stats = find_greatest(stats)
    continuing = input()
    # Iterate until there is an empty string
    while continuing != "":
        # If the input was not an empty string,
        # but also was not in the list of keys,
        # take user input again to restart the loop
        if continuing.lower() not in greatest_stats.keys():
            continuing = input()
        else:
            # Iterate through each key in greatest_stats
            for key in greatest_stats:
                # Determine if the entered key is a certain stat.
                if continuing.lower() == key.lower():
                    # Iterate through each element in the tuple
                    for x in greatest_stats[key][0]:
                        print("{}: {}".format(x, greatest_stats[key][1]))
            continuing = input()

main()






    



