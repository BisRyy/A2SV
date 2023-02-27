class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        def cmp(x, y):
            for i in x:
                if y[i] < x[i]:
                    return False
            return True
        
        if len(t) > len(s):
            return ""
        if s == t:
            return t
        
        left = 0
        c = Counter(t)
        d = Counter(t)
        
        ans = s+s+s
        
        for i in d:
            d[i] = 0
            
        for right in range(len(s)):
            
            if s[right] in d:
                d[s[right]]+=1
                
            while cmp(c, d):
                if len(ans) > right - left + 1:
                    ans = s[left:right+1]
                    
                d[s[left]]-=1
                left+=1
                
        return ans if ans != s+s+s else ""