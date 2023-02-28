class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        mid = -float("inf")
        
        for i in range(len(nums)-1, -1, -1):
            if mid > nums[i]:
                return True
            
            while stack and stack[-1] < nums[i]:
                mid = stack.pop()
            
            stack.append(nums[i])
            
        return False
        
        '''
        
        1 2 3 4
        
        
        
        3 1 4 2
        
        3 4
        
        -1 3 2 0
        
        -1 3 
        
        '''
        