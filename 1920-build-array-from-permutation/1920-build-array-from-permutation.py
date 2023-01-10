class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        array = []
        i = 0
        
        for num in nums:
            array.append(nums[nums[i]])
            i+=1

        return array