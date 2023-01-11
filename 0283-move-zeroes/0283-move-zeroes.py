class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = nums.count(0)
        
        for _ in range(zeros):
            nums.remove(0)
            nums.append(0)