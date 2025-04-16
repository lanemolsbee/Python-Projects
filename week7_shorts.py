def list2string(arglist):
    if len(arglist) == 0:
        return ""
    else:
        return arglist[0] + list2string(arglist[1:])

def palindrome_list(arglist):
    if len(arglist) == 0:
        return True
    else:
        if arglist[0] == arglist[len(arglist) - 1]:
            return palindrome_list(arglist[1:len(arglist) - 1])
        else:
            return False


def column2list_rec(grid, n):
    if len(grid) == 0:
        return []
    else:
        return [grid[0][n]] + column2list_rec(grid[1:],n)

def diag2list_rec(grid):
    return help_diaglist(grid, 0)


def help_diaglist(grid, x):
    if len(grid) == 0:
        return []
    else:
        return [grid[0][x]] + help_diaglist(grid[1:],x + 1)
    