class Queue:
    def __init__(self):
        self._items = []
    def enqueue(self, item):
        self._items.append(item)
    def dequeue(self):
        return self._items.pop(0)
    def reverse(self):
        self._items = self._items[::-1]
    def __str__(self):
        return str(self._items)

def  main():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(q)
    q.reverse()
    print(q)

main()