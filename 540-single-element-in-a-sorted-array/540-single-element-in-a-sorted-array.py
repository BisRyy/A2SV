class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        a = Counter(nums)
        for num in nums:
            if a[num] == 1:
                return num
            
        return 0