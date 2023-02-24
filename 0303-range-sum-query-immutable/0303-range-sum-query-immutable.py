class NumArray:

    def __init__(self, nums: List[int]):
        self.a = [0] + nums 
        for i in range(1, len(nums)+1):
            self.a[i] += self.a[i-1]

    def sumRange(self, left: int, right: int) -> int:
        return self.a[right+1] - self.a[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)