val = 0
class newSet:
    def __init__(self):
        self.items = dict()

    def add(self, item):
        self.items[item] = 1
        return self

    def remove(self, item):
        self.items.pop(item)
        return self

    def pop(self):
        return self.items.popitem()

    def printall(self):
        print(self.items)



newSet = newSet()

newSet.add(1)
newSet.add(2)
newSet.add(3)
newSet.printall()
newSet.pop()

newSet.printall()
