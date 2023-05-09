class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        ans = []
        for row in matrix:
            ans.extend(row)
        return sorted(ans)[k-1]