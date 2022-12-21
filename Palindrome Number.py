class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)

        ans = True
        for i in range(int(len(y) / 2)):
            if y[i] != y[len(y)-i-1]:
                ans = False

        return ans
