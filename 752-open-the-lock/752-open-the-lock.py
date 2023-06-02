class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def neighbors(code):
            neighbour = []
            for i in range(4):
                x = int(code[i])
                for diff in (-1, 1):
                    y = (x + diff + 10) % 10
                    neighbour.append(code[:i] + str(y) + code[i + 1:])
            return neighbour

        deadSet = set(deadends)
        if "0000" in deadSet:
            return -1
        q = deque(["0000"])
        steps = 0
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if curr == target:
                    return steps
                for nei in neighbors(curr):
                    if nei in deadSet: 
                        continue
                    deadSet.add(nei)
                    q.append(nei)
            steps += 1

        return -1