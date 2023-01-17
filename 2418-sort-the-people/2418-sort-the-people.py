class Solution:
    def sortPeople(self, names: List[str], height: List[int]) -> List[str]:
        
        for j in range(len(names)):
            flag  = True
            for index in range(len(height)-1-j):
                if height[index] < height[index+1]:
                    height[index],  height[index+1] = height[index+1], height[index]
                    names[index],  names[index+1] = names[index+1], names[index]
                    flag = False
            if flag:
                break
            
        return names