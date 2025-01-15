class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        # dfs用stack， bfs用queue, dfs寻找有没有路，bfs寻找最短路径
        stack = [start]
        visited = set()
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        while stack:
            pos = stack.pop()
            # r, c = pos[0], pos[1]
            if pos[0] == destination[0] and pos[1] == destination[1]:
                return True

            for dir in directions:
                r, c = pos[0], pos[1]
                dr, dc = dir[0], dir[1]
                while 0 <= r + dr <= len(maze) - 1 and 0 <= c + dc <= len(maze[0]) - 1 and maze[r + dr][c + dc] == 0:
                    r += dr
                    c += dc
                if (r, c) in visited:
                    continue
                else:
                    visited.add((r, c))
                    stack.append([r, c])

        return False
