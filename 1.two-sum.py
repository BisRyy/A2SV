#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num = sorted(nums)
        i = 0
        j = len(nums) - 1
        while i < j:
            if num[i] + num[j] == target:
                x = nums.index(num[i])
                nums[x] = 'x'
                y = nums.index(num[j])
                return [x,y]
            elif num[i] + num[j] < target:
                i += 1
            else:
                j -= 1
        
# @lc code=end

