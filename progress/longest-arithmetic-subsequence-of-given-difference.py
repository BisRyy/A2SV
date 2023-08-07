class Solution:
    def longestSubsequence(self, arr: List[int], d: int) -> int:
        subseqs = defaultdict(int)
        for n in arr:
            prev = subseqs[n]
            next = subseqs[n+d]
            subseqs[n+d] = max(prev + 1, next)
        
        return max(subseqs.values())