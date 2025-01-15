from collections import deque


def wallsAndGates(rooms):
    """
    :type rooms: List[List[int]]
    :rtype: None Do not return anything, modify rooms in-place instead.
    """

    # use queue for bfs
    rows, cols = len(rooms), len(rooms[0])
    visited= set()
    q = deque()

    def addRoom(row, col):
        if row < 0 or row == rows or col < 0 or col == cols or (row, col) in visited or rooms[row][col] == -1:
            return
        visited.add((r, c))
        q.append([row, col])


    for r in range(rows):
        for c in range(cols):
            if rooms[r][c] == 0:
                q.append([r, c])
                visited.add((r, c))

    distance = 0
    # 这个while 套 for 才能保证一层一层来
    while q:
        for i in range(len(q)):
             gate_r, gate_c =  q.popleft()
             # gate直接距离为0
             rooms[gate_r][gate_c] = distance

             addRoom(gate_r, gate_c + 1)
             addRoom(gate_r, gate_c - 1)
             addRoom(gate_r + 1, gate_c)
             addRoom(gate_r - 1, gate_c)

        distance += 1

