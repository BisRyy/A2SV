class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        d = ["" for i in range(len(s) + len(spaces))]

        for i,j in enumerate(spaces):
            d[i+j] = " "

        j = 0
        for i in s:
            while d[j] == " ":
                j+=1
            d[j] = i
            j+=1
                
        return "".join(d)
    
    
    
    
    