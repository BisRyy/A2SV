class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            a = list(str(num))
            num = sum(map(int, a))
        return num