class Solution:
    def tribonacci(self, n: int) -> int:
        
        a = [0, 1, 1]
        
        def f(i):
            return a[i-1] + a[i-2] + a[i-3]
        
        for i in range(3, n):
            a.append(f(i))
            
        return f(n) if n not in [0, 1, 2] else a[n]
        