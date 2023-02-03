class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        last_idx = {}
        for index,letter in enumerate(s):
            last_idx[letter] = index
            
        left = 0 
        end = 0
        answer =[]
        
        for i,letter in enumerate(s):
            end = max(end ,last_idx[letter])
            
            if i == end:
                answer.append(i-left+1)
                left = i+1
                
        return answer
            
            
            
            
            