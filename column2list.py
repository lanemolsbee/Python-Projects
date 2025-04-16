def column2list(grid, n):
    position_list = []
    for i in range(len(grid)):
        if n < len(grid[i]):
            position_list.append(grid[i][n])
    return position_list
