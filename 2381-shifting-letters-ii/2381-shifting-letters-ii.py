class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        p = [ord(i)-ord('a') for i in s]
        s = [0]*(len(p)+1)
        
        for shift in shifts:
            if shift[2] == 0:
                s[shift[0]]-=1
                s[shift[1]+1]+=1
            else:
                s[shift[0]]+=1
                s[shift[1]+1]-=1
                
        for i in range(1,len(s)):
            s[i]+=s[i-1]
            
        for i in range(len(p)):
            p[i] += s[i]
            p[i] %= (ord('z') - ord('a') +1)
            p[i] = chr(p[i]+ord('a'))
            
        return (''.join(p))    