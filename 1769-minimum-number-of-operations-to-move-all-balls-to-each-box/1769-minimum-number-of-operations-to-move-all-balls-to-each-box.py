class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        answer = []
        n = range(len(boxes))
        
        for i in n:
            t = 0
            
            for j in n:
                
                if i != j and boxes[j] == '1':
                    t += abs(i-j)
            
            answer.append(t)
            
        return answer
        