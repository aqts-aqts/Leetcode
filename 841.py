class Solution(object):
    def canVisitAllRooms(self, rooms):
        n = len(rooms)
        queue = [0]
        visited = [0] * n
        visited[0] = 1
        while queue:
            cur = queue.pop()
            for room in rooms[cur]:
                if not visited[room]: 
                    queue.append(room)
                    visited[room] = 1
        return all(visited)