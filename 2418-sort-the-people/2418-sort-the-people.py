class Solution:
    def sortPeople(self, names: List[str], height: List[int]) -> List[str]:
        
        for i in range(len(names)-1):
            maximum  = i
            for index in range(i+1,len(height)):
                if height[index] > height[maximum]:
                    maximum = index
            
            height[i],  height[maximum] = height[maximum], height[i]
            names[i],  names[maximum] = names[maximum], names[i]
            
        return names