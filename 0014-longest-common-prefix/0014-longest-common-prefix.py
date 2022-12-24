class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        x = 0
        ans = ""
        if len(strs) == 1 or strs[0] == "":
            return strs[0]
            
        while x < len(strs[0]) + 1:
            if strs[0][:x] != strs[len(strs) - 1][:x]:
                return strs[0][:x-1]
            x += 1
        return strs[0][:x]
