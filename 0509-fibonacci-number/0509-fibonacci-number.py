class Solution:
    def fib(self, n: int) -> int:
        
        x = 1
        y = 0
        c = 0
        nth = 0
        while c < n-1:
            nth = x + y
            y = x
            x = nth
            c+=1
        return nth if n!= 1 else 1