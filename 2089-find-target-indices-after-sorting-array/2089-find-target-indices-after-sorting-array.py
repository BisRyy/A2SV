class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i, v in enumerate(sorted(nums)):
            if v == target:
                ans.append(i)
                
        return ans
        