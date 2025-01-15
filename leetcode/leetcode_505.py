from collections import deque


def shortestDistance(maze, start, destination):
    """
    :type maze: List[List[int]]
    :type start: List[int]
    :type destination: List[int]
    :rtype: int
    """
    from heapq import heappop, heappush

    class Solution:
        def shortestDistance(self, maze, start, destination):
            """
            :type maze: List[List[int]]
            :type start: List[int]
            :type destination: List[int]
            :rtype: int
            """
            m, n = len(maze), len(maze[0])
            directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            dist = [[float('inf')] * n for _ in range(m)]
            dist[start[0]][start[1]] = 0
            pq = [(0, start[0], start[1])]

            while pq:
                d, row, col = heappop(pq)
                if [row, col] == destination:
                    return d

                if d > dist[row][col]:
                    continue

                for dr, dc in directions:
                    nr, nc = row, col
                    steps = 0

                    while 0 <= nr + dr < m and 0 <= nc + dc < n and maze[nr + dr][nc + dc] == 0:
                        nr += dr
                        nc += dc
                        steps += 1

                    if dist[row][col] + steps < dist[nr][nc]:
                        dist[nr][nc] = dist[row][col] + steps
                        heappush(pq, (dist[nr][nc], nr, nc))

            return -1
