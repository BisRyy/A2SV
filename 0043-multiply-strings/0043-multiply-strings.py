class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        prod = num1 + "*" + num2
        return str(eval(prod))