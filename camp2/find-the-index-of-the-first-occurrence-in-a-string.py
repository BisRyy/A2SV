class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1
        if haystack == needle:
            return 0
        
        def hash(word):
            n = 0
            for i, letter in enumerate(word):
                n += (ord(letter)- ord("a")) * 26**(len(word)-1-i)
            return n % (10**9 + 7)
        x = hash(needle)
        y = hash(haystack[:len(needle)])
        
        for i in range(len(haystack) - len(needle)):
            if x == y:
                return i
            
            y -=  (ord(haystack[i]) - ord("a")) * 26**(len(needle)-1)
            y *= 26
            y += (ord(haystack[i+len(needle)]) - ord("a"))
            y %= (10**9 + 7)
            
            if x == y:
                return i+1
        return -1
            