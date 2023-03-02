class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        stack = []
        ans = [-1] * len(nums)
        
        for i in range(2):
            for idx, num in enumerate(nums):

                while stack and num > stack[-1][1]:
                    poped = stack.pop()
                    ans[poped[0]] = num

                stack.append((idx,num))
            
        
        return ans