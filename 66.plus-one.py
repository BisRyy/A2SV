#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        r = [str(i) for i in digits]
        s = int(''.join(r))
        t = list(str(s+1))
        u = [int(i) for i in t]
        return u

        
# @lc code=end

