class RandomizedSet:

    def __init__(self):
        self.dict = set()

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.dict.add(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False
        self.dict.remove(val)
        return True
        

    def getRandom(self) -> int:
        return int(random.choice(list(self.dict)))
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()