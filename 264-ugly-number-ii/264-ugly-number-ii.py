class Solution(object):
    def nthUglyNumber(self, n):
        
        two, three, five, nums = 0, 0, 0, [1]
        
        for i in range(n - 1):
            nums.append(min(nums[two] * 2, nums[three] * 3, nums[five] * 5))
        
            if nums[-1] == nums[two] * 2:
                two += 1
            
            if nums[-1] == nums[three] * 3:
                three += 1
            
            if nums[-1] == nums[five] * 5:
                five += 1
        
        return nums[-1]
