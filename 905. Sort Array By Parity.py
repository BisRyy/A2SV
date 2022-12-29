class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        ans = deque()
        for num in nums:
            if num % 2 == 0:
                ans.appendleft(num)
            else:
                ans.append(num)
                
        return ans
