class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque([0])
        visited = set([0])
        while queue:
            current = queue.popleft()
            for key in rooms[current]:
                if key not in visited:
                    queue.append(key)
            visited.add(current)
        
        return len(visited) == len(rooms)
                