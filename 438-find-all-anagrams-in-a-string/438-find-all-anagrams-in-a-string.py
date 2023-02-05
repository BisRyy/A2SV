class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        

        n = len(p)
        m = len(s) 
        counter = n
        left = 0
        right = 0
        
        pvalue = defaultdict(int)
        v = []
        
        if n > m:
            return v;
        
        for i in range(n):
            pvalue[p[i]] += 1
        
        while right < m:
            
            if pvalue[s[right]] >=  1:
                counter -= 1
                
            pvalue[s[right]]-=1

            if counter == 0:
                v.append(left);
        
            if (right - left) + 1 == n :
                
                if pvalue[s[left]] >= 0:
                    counter += 1
                    
                pvalue[s[left]]+=1
                
                left+=1
            right+=1
            
        return v
