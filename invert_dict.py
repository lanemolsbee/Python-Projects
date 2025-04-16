def invert_dict(origdict):
    origdict_keys = origdict.keys()
    origdict_values = origdict.values()
    newdict = {}
    for i in range(len(origdict_keys)):
        newdict[origdict_values[i]] = origdict_keys[i]
    return newdict