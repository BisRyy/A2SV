class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        m = len(word1)
        n = len(word2)
        ans = ""
        
        s1 = 0
        s2 = 0
        
        i = 0
        j = 0
        while i < m and j < n:
            if word1[i] == word2[j]:
                if word1[s1:] > word2[s2:]:
                    ans += word1[s1]
                    s1+=1
                    i += 1 
                else:
                    ans += word2[s2]
                    s2+=1
                    j +=1
            
            
            elif word1[i] > word2[j]:
                ans += word1[s1]
                s1+=1
                i=s1
                j=s2
                
            elif word1[i] < word2[j]:
                ans += word2[s2]
                s2+=1
                j=s2
                i=s1
        print(ans)
        print(ans + word2[s2:] + word1[s1:],ans + word1[s1:] + word2[s2:])
        return max(ans + word2[s2:] + word1[s1:] , ans + word1[s1:] + word2[s2:]) 
