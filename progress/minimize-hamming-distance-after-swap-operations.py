class UnionFind:
    def __init__(self, n): 
        self.root = list(range(n))
    
    def union(self, x, y): 
        self.root[self.find(x)] = self.find(y)
    
    def find(self, x):
        if x != self.root[x]: 
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    
class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        uf = UnionFind(len(source))
        for x, y in allowedSwaps: 
            uf.union(x, y)
        m = defaultdict(set)  # key is the component, value is the set of indices in same component
        for i in range(len(source)):
            m[uf.find(i)].add(i)
        ans = 0
        for indices in m.values():
            A = [source[i] for i in indices]
            B = [target[i] for i in indices]
            ans += sum((Counter(A) - Counter(B)).values())
        return ans
            
