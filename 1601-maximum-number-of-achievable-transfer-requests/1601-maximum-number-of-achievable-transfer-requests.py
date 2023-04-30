class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        result =  0   
        buildings = [0] * n
        def backtrack(start, curr, buildings):
            nonlocal result
            
            if start >= len(requests):
                return
            
            for idx in range(start, len(requests)):
                curr.append(requests[idx])
                from_, to_ = requests[idx]
                buildings[from_] -= 1
                buildings[to_] += 1
                
                if all(net == 0 for net in buildings):
                    result = max(result, len(curr))
                
                backtrack(idx + 1, curr, buildings)
                
                request = curr.pop()
                from_, to_ = request
                buildings[from_] += 1
                buildings[to_] -= 1
            
            return
        
        backtrack(0, [], buildings)
        
        return result