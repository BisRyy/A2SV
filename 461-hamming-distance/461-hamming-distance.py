class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = 0
        for i in range( max(x,y).bit_length()):
             ans += x&(1<<i) != y&(1<<i)
            
        return ans