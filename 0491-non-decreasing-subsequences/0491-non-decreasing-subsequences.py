class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def helper(i,l):
            nonlocal ans

            if len(l) > 1 and l not in ans:
                ans.append(l.copy())
            if i >= len(nums):
                return l
                        
            for j in range(i+1, len(nums)):
                if i == -1 or nums[i] <= nums[j]:
                    helper(j,l+[nums[j]])

        helper(-1,[])
        
        return ans