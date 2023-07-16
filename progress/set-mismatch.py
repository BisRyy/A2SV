class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s = len(nums)*(len(nums)+1) // 2
        a = sum(nums)
        u = sum(set(nums))
        return [a-u,s-u]