class SmallestInfiniteSet:

    def __init__(self):
        self.x = 1
        self.s = set()

    def popSmallest(self) -> int:
        if self.s:
            small = min(self.s)
            self.s.remove(small)
            return small
        else:
            self.x += 1
            return self.x - 1

    def addBack(self, num: int) -> None:
        if self.x > num:
            self.s.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)