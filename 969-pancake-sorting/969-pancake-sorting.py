class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        '''
        [3,2,4,1]
        [1,2,3,4]
        
        [4,2,4,3]
        
        '''
        
        answer = []
        index=len(arr)
       
        while index>0:
            
            fliped = max(arr[:index])
            fliped = arr.index(fliped)
            
            if fliped !=0:
                answer.append(fliped + 1)
               
            arr[:fliped +1]= reversed(arr[:fliped +1])
            arr[:index] = reversed(arr[:index])
            
            answer.append(index)
            index-=1
            
        return answer