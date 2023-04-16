class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        wl, tl = len(words[0]), len(target)
        modulo = 10 ** 9 + 7
        counters = [[0] * 26 for _ in range(wl)]
        for word in words:
            for i, c in enumerate(word):
                counters[i][ord(c) - ord('a')] += 1
        
        dp = [1] * (wl + 1)
        dp[0] = 0
        for ti in range(1, tl + 1):
            prev = 1 if ti == 1 else 0
            for wi in range(1, wl + 1):
                dp[wi], prev = (dp[wi - 1] + prev * counters[wi - 1][ord(target[ti - 1]) - ord('a')]) % modulo, dp[wi]
        
        return dp[wl]