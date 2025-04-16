class GridPos:
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._ship = None
        self._guessed = False
    
    def __str__(self):
        pass

class Board:
    def __init__(self, ships):
        grid = []
        for i in range(9,-1,-1):
            row = []
            for j in range(10):
                row.append(GridPos(i,j))
            grid.append(row)
        self._grid = grid
        self._ships = ships
    
    def __str__(self):
        pass

    def guess(gridpos):
        pass

class Ship:
    def __init__(self,type, positions):
        self._type = type
        self._size = 0
        if type == "A":
            self._size = 5
        elif type == "B":
            self._size = 4
        elif type == "S":
            self._size = 3
        elif type == "D":
            self._size = 3
        elif type == "P":
            self._size = 2
        self._positions = positions
        self._not_hit = self._size
    def __str__(self):
    
