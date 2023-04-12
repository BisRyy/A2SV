class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        def t(n: int) -> list[int]:
           nonlocal pro
           d = 2

           while d * d <= n:
               while n % d == 0:
                   pro.add(d)
                   n //= d
               d += 1
           if n > 1:
               pro.add(n)

           return pro
        pro = set()
        for i in nums:
            t(i)
            
        return len(pro)
