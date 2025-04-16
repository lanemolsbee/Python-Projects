class Stack():
    def __init__(self):
        self._items = []
    
    def push(self, item):
        self._items.append(item)
    
    def pop(self):
        return self._items.pop()
    
    def alt_push(self, item):
        if len(self._items) == 0:
            self._items.append(item)
        else:
            self._items.insert(0, item)
    
    def alt_pop(self):
        return self._items.pop(0)

class Queue:
    def __init__(self):
        self._items = []
    
    def enqueue(self, item):
        self._items.append(item)
    
    def dequeue(self):
        return self._items.pop(0)
    
    def alt_enqueue(self, item):
        if len(self._items) == 0:
            self._items.append(item)
        else:
            self._items.insert(0, item)
    
    def alt_dequeue(self):
        return self._items.pop()