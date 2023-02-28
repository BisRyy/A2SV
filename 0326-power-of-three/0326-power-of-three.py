class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return 1 if  n == 1 else 0 if n < 1 else self.isPowerOfThree(n/3)