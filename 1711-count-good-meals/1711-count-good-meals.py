class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        
        count = defaultdict(int)
        answer = 0
        
        for values in deliciousness:
            # since there are only 21 powers of 2 based on the constraints
            for power in range(22):
                # check if the other number is present  
                difference = 2**power - values
                
                if difference in count:
                    
                    answer += count[difference]
                    
            count[values] += 1
                
        return answer % (10**9 + 7) 
                    
                