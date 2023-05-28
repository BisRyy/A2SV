class Solution:
   def longestPath(self, parent: List[int], s: str) -> int:
       children = [[] for _ in range(len(parent))]
       for child in range(1, len(parent)):
           children[parent[child]].append(child)
       max_path = 0
       def dfs(node: int) -> int:
           nonlocal max_path 
           max_chain, second_max_chain = 0, 0
           for child in children[node]:
               chain_len = dfs(child)
               if s[node] != s[child]:
                   if chain_len > max_chain:
                       second_max_chain = max_chain
                       max_chain = chain_len
                   elif chain_len > second_max_chain:
                       second_max_chain = chain_len
           max_path = max(max_path, max_chain + second_max_chain + 1)
           return max_chain + 1
       dfs(0)
       return max_path