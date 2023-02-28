class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return 1 if  n == 1 else 0 if n < 1 else self.isPowerOfFour(n/4)