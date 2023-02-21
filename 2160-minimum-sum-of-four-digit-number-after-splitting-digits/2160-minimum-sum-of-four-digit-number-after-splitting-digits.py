class Solution:
    def minimumSum(self, num: int) -> int:
        m = list(str(num))
        m.sort()
        
        return int(m[0]+m[2]) + int(m[1]+m[3])