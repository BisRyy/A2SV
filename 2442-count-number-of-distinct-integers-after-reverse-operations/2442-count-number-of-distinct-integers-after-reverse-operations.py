class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        
        arr = nums[:]
        
        for num in nums:
            s = list(str(num))
            s.reverse()
            arr.append(int("".join(s)))
            
        return len(set(arr))