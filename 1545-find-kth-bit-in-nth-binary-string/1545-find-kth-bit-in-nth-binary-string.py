class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        def revinv(s, c, n):
            if c == n:
                return s
            t = []
            for i in s:
                if i == "1":
                    t.append("0")
                else:
                    t.append("1")  
            return revinv(s + "1" + "".join(t[::-1]), c+1, n)
        S1 = "0"
        
        return(revinv(S1, 0, n)[k-1])