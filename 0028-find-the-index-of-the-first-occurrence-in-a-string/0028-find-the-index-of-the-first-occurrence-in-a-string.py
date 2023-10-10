class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        lps = [0] * n
        
        i = 0
        j = 1
        while j < n:
            if needle[i] == needle[j]:
                lps[j] = i+1
                i+=1
                j+=1
            else:
                if i < 1:
                    j+=1
                else:
                    i = lps[i-1]
                    
        i = 0
        j = 0
        while j < n and i < len(haystack):
            if haystack[i] == needle[j]:
                i+=1
                j+=1
            else:
                if j == 0:
                    i+=1
                else:
                    j = lps[j-1] 
        
        if j == n:
            return i-j
        return -1
    
    
    
    
    
    
    
    