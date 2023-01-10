class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        a = []
        for i in range(len(grid)):
            t = []
            for j in range(len(grid)):
                t.append(grid[j][i])
            a.append(t)
        c = 0

        for i in range(len(a)):
            for j in range(len(grid)):
                t = False
                for k in range(len(grid)):
                    if grid[i][k] == a[j][k]:
                        t = True
                    else:
                        t = False
                        break
                if t: c += 1
        return c