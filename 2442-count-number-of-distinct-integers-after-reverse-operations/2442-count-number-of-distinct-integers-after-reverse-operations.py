class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        for i in range(n):
            s = list(str(nums[i]))
            s.reverse()
            nums.append(int("".join(s)))
            
        return len(set(nums))