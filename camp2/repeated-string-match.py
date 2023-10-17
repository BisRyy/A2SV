class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if a.find(b) != -1:
            return 1
        else:
            if (a+a).find(b) != -1:
                return 2
        
        ans = 1
        tmp = a
        while len(a) <= 2*len(b):
            a += tmp
            ans += 1
            if a.find(b) != -1:
                break
            print(ans)
        
        # print(a, b)
        if a.find(b) == -1:
            return -1
        return ans