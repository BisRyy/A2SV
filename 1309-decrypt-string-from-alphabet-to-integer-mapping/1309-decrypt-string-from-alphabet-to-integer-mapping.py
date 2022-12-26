class Solution:
    def freqAlphabets(self, s: str) -> str:
        max_length = len(s) - 1
        ans = ""
        while max_length > -1:
            if s[max_length] == "#":
                ans = chr(int(s[max_length-2:max_length]) +  96) + ans 
                max_length -= 3
            else:
                ans = chr(int(s[max_length]) + 96) + ans
                max_length -= 1
        return ans
