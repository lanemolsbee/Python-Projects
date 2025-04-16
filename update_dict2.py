def update_dict2(dict2, key1, key2, value):
    if key1 in dict2:
        dict2[key1][key2] = value
    else:
        dict2[key1] = dict(key2)
        dict2[key1][key2] = value
    return dict2