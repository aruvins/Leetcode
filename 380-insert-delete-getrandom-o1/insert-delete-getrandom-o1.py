class RandomizedSet:

    def __init__(self):
        self.list = []
        self.indexMap = {}

    def search(self, val):
        return val in self.indexMap

    def insert(self, val: int) -> bool:
        if self.search(val):
            return False

        self.list.append(val)
        self.indexMap[val] = len(self.list) - 1
        return True

    def remove(self, val: int) -> bool:
        if not self.search(val):
            return False
        
        i = self.indexMap[val]
        self.list[i] = self.list[-1]
        self.indexMap[self.list[-1]] = i
        self.list.pop()
        del self.indexMap[val]
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()