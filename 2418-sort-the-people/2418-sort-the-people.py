class Solution:
    def sortPeople(self, names: List[str], height: List[int]) -> List[str]:
        
        for name in names:
            for index in range(len(height)-1):
                if height[index] < height[index+1]:
                    height[index],  height[index+1] = height[index+1], height[index]
                    names[index],  names[index+1] = names[index+1], names[index]
            
        return names