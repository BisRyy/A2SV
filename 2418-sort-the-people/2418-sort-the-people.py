class Solution:
    def sortPeople(self, names: List[str], height: List[int]) -> List[str]:
        
        for i in range(len(names)-1):
            unsorted  = height[i+1]
            unsortedName = names[i+1]
            place = 0
            
            for j in range(i, -1 , -1):
                if height[j] < unsorted:
                    height[j],  height[j+1] = height[j+1], height[j]
                    names[j],  names[j+1] = names[j+1], names[j]
                else:
                    place = j+1
                    break
            height[place] = unsorted
            names[place] = unsortedName
            
        return names