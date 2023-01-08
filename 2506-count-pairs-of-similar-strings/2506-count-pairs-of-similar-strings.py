class Solution:
    def similarPairs(self, words: List[str]) -> int:
        
        count = 0
        
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                same = 0
                for k in words[i]:
                    if k not in words[j]:
                        same += 1
                        break
                    
                for k in words[j]:
                    if k not in words[i]:
                        same +=1
                        break
                        
                if same == 0:
                    count += 1
                    
        return count
    
    
    # add comments to describe important operations 
    # add space between assignment and the for loop 
    # same = same + 1
