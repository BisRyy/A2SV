class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        
        houses.sort()
        heaters.sort()
        res = 0
        i = 0
        for house in houses:
            while i < (len(heaters)-1) and abs(heaters[i] - house) >= abs(heaters[i+1] - house):
                i+=1
            res = max(abs(heaters[i] - house), res)
        return res