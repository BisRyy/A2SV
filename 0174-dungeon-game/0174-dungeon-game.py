class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        r = len(dungeon)
        c = len(dungeon[0])
        val = [[float("-inf") for i in range(c+1)] for i in range(r+1)]

        for i in range(r-1, -1, -1):
            for j in range(c-1, -1, -1):
                if i == r-1 and j == c-1:
                    val[i][j] = min(0, dungeon[i][j])
                else:
                    temp = dungeon[i][j] + max(val[i+1][j], val[i][j+1])
                    val[i][j] = min(0, temp)
        return abs(val[0][0]) + 1 if val[0][0] < 0 else 1
   