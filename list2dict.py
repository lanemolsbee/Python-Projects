def list2dict(list2d):
    converted = {}
    for i in range(len(list2d)):
        converted[list2d[i][0]] = list2d[i][1:len(list2d[i])]
    return converted