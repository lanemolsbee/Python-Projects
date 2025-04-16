class Word:
    def __init__(self, word):
        self._word = word
    
    def  __str__(self):
        return self._word.lower()
    
    def __eq__(self, other):
        if len(self._word) != len(other):
            return False
        lowercase_other = other.lower()
        lower_self = self._word.lower()
        other_dict = {}
        self_dict = {}

        for i in range(len(lowercase_other)):
            if lower_self[i] not in self_dict:
                self_dict[lower_self[i]] = 0
            if lowercase_other[i] not in other_dict:
                other_dict[lowercase_other[i]] = 0
            self_dict[lower_self[i]] += 1
            other_dict[lowercase_other[i]] += 1
        
        for key in self_dict:
            if key not in other_dict:
                return False
            if other_dict[key] != self_dict[key]:
                return False
            
        return True

            


