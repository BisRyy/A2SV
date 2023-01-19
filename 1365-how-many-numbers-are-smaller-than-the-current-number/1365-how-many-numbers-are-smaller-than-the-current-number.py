
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = [0]*len(nums)
        k = 0
        for i in nums:
            for j in nums:
                if j < i:
                    count[k]+=1
            k+=1
        return count