class Solution:
    def countSubTrees(self, n: int, edges: list[list[int]], labels: str) -> list[int]:
        graph = [[] for i in range(n)]
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        ans = [0] * n

        def dfs(vertex, parent, cnt):
            before = cnt[labels[vertex]]

            for adjacent in graph[vertex]:
                if adjacent != parent:
                    dfs(adjacent, vertex, cnt)

            cnt[labels[vertex]] += 1
            ans[vertex] = cnt[labels[vertex]] - before

        dfs(0, 0, Counter())
        return ans