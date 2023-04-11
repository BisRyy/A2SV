class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        d = defaultdict(list)
        for edge in roads:
            d[edge[0]].append(edge[1])
            d[edge[1]].append(edge[0])
        a = list(d.keys())
        m = 0
        for i in range(len(a)):
            for j in range(i+1, len(a)):
                x = len((d[a[i]]+d[a[j]]))
                if m < x:
                    m = x
                    m -= 1 if a[j] in d[a[i]] else 0
                
        return m