def shuffle_dict(somedict):
    keys = sorted(somedict.keys())
    values = sorted(somedict.values())
    sorted_dict = {}
    for i in range(len(keys)):
        sorted_dict[keys[i]] = values[i]
    return sorted_dict
