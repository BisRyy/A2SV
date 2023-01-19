class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
        answer = []
        
        for i, v in enumerate(sorted(nums)):
            
            if v == target:
                answer.append(i)
                
        return answer
        