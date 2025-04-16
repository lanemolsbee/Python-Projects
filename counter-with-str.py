class Counter:
    def __init__(self, name):
        self._name = name
        self._count = 0

    def click(self):
        self._count += 1

    def count(self):
        return self._count

    def __str__(self):
        return "Counter: " + self._name + "->" + str(self._count)

def main():
    c = Counter("Count")
    c2 = Counter("Count2")
    for x in range(1, 6):
        c.click()
    for x in range(1, 10):
        c2.click()
    print(c.count())
    print(c2.count())
    print(c.__str__())
    print(c2.__str__())

main()