class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        answer = defaultdict(int)
        count = 0
        
        for stone in stones:
            answer[stone] += 1
        
        for jewel in jewels:
            count += answer[jewel]
        
        return count
            