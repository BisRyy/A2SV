class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = Counter(words)
        d = [(-c[key], key) for key in c]
        ans = []
        heapify(d)
        # for i in range(len(d)-k):
        #     heappop(d)
        for i in range(k):
            ans.append(heappop(d))
        ans.sort()
        ans = [i[1] for i in ans]
        return ans