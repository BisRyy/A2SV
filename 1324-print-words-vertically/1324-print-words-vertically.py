class Solution:
    def printVertically(self, s: str) -> List[str]:
        p = s.split(" ")
        _max = 0
        for l in p:
            _max = max(_max, len(l)) 
        ans=  []
        for _ in range(_max):
            w = ""
            for l in p:
                if len(l) > _:
                    w += l[_]
                else:
                    w+=" "
            ans.append(w.rstrip())
        return ans