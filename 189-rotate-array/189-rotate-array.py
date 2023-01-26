class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        j = 0
        k = k % n

        for i in nums[n-k:] + nums[:n-k]:
            nums[j] = i
            j+=1
    
