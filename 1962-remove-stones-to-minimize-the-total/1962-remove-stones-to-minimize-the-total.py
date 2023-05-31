class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-num for num in piles]
        heapify(heap)
        for _ in range(k):
            curr = -heappop(heap)
            remove = curr // 2
            heappush(heap, -(curr - remove))
        return -sum(heap)