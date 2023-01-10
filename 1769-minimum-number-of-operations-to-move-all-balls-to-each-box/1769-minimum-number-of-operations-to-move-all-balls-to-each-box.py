class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = []
        n = range(len(boxes))
        for i in n:
            t = 0
            for j in n:
                if i != j and boxes[j] == '1':
                    t += abs(i-j)
            ans.append(t)
        return ans
        