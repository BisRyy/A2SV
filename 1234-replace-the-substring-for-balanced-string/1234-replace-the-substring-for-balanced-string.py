class Solution:
    def balancedString(self, s: str) -> int:
        def check(d):
            for i in d:
                if d[i] > 0:
                    return 0
            return 1
        
        c = Counter(s)
        n = len(s)
        
        ans = ""
        for i in "QWER":
            if c[i] > n//4:
                ans += (c[i] - n//4) * i
        
        if ans == "":
            return 0

        d = Counter(ans)
        l = 0
        r = 0
        m = n + 1
        
        while r < n:
            if s[r] in d:
                d[s[r]]-=1
                
            while check(d) and l < n:
                m = min(m, r-l+1)
                if s[l] in d:
                    d[s[l]]+=1
                l+=1
            r+=1
            
        return m
        