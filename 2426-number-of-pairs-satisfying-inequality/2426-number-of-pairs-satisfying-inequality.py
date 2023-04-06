from sortedcontainers import SortedList 
class Solution:
    def numberOfPairs(self, A: List[int], B: List[int], diff: int) -> int:
        l = SortedList()
        res = 0
        for a,b in zip(A, B):
            res += l.bisect_right(a - b + diff)
            l.add(a - b)
        return res