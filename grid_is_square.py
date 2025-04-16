def grid_is_square(arglist):
    status = True
    for i in range(len(arglist)):
        if len(arglist[i]) != len(arglist):
            status = False
    return status
