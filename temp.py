class Temp:
    def __init__(self, temp, unit):
        self._temp = temp
        self._unit = unit
    
    def __str__(self):
        return str(self._temp) + str(self._unit)
    
    def convert_to_celsius(self):
        if self._unit == "F":
            self._temp = (self._temp - 32) * (5/9)
        return self._temp
    
    def __eq__(self, temp2):
        if self._unit == "F":
            self._temp = (self._temp - 32) * (5/9)
        if self._temp == temp2.convert_to_celsius():
            return True
        return False
    
    def __lt__(self,temp2):
        if self._unit == "F":
            self._temp = (self._temp - 32) * (5/9)
        if self._temp < temp2.convert_to_celsius():
            return True
        return False
    
    def __gt__(self, temp2):
        if self._unit == "F":
            self._temp = (self._temp - 32) * (5/9)
        if self._temp > temp2.convert_to_celsius():
            return True
        return False
    def __neq__(self, temp2):
        if self._unit == "F":
            self._temp = (self._temp - 32.0) * (5.0/9.0)
        if self._temp == temp2.convert_to_celsius():
            print(self._temp, temp2.convert_to_celsius())
            return False
        return True

t1 = Temp(100, "C")
t2 = Temp(212, "F")
print(t1 != t2)





