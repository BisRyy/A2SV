class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        
        val = inf
        ans = -1
        for index in range(len(points)):
            if points[index][0] == x or points[index][1] == y:
                temp = abs(points[index][0] - x) + abs(points[index][1] - y)
                if temp < val:
                    val = temp
                    ans = index
        return ans