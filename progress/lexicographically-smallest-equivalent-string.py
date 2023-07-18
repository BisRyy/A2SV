class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        equiv = defaultdict(set)
        smallest = defaultdict(str)

        for c1, c2 in zip(s1, s2):
            if c1 == c2: 
                continue
            equiv[c1].add(c2)
            equiv[c2].add(c1)
        
        def setMinChar(curr, minCh):
            if curr in smallest: 
                return
            
            smallest[curr] = minCh
            for eq in equiv[curr]:
                setMinChar(eq, minCh)

        for c in [chr(ord('a') + i) for i in range(26)]:
            if c in equiv:
                if c in smallest: 
                    continue
                setMinChar(c, c)
                
        return ''.join([smallest[c] if c in smallest else c for c in baseStr])
