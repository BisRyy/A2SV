class SmallestInfiniteSet:

    def __init__(self):
        self.excluded = set()
        self.min_val = 1

    def popSmallest(self) -> int:
        next_min_val = self.min_val + 1
        while next_min_val in self.excluded:
            next_min_val += 1
        ans = self.min_val
        self.min_val = next_min_val
        self.excluded.add(ans)
        return ans

    def addBack(self, num: int) -> None:
        if num not in self.excluded:
            return
        self.excluded.remove(num)
        self.min_val = min(self.min_val, num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)