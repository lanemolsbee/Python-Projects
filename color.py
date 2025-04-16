class Color:
    def __init__(self, r, g, b):
        if r < 0:
            self._r = 0
        if g < 0:
            self._g = 0
        if b < 0:
            self._b = 0
        if r > 255:
            self._r = 225
        if g > 225:
            self._g = 225
        if b > 225:
            self._b = 225
        self._r = r
        self._g = g
        self._b = b
    
    def get_rgb(self):
        return (self._r, self._g, self._b)
    
    def remove_red(self):
        self._r = 0
    
    def __str__(self):
        return "Color(" + str(self._r) + ","\
         + str(self._g) + "," + str(self._b) + ")"

    def same_color(self, other):
        if self._r != other._r:
            return False
        if self._g != other._g:
            return False
        if self._b != other._b:
            return False
        return True