from collections import defaultdict, deque


def sequenceReconstruction(nums, sequences):
    """
    :type nums: List[int]
    :type sequences: List[List[int]]
    :rtype: bool
    """

    # 入度表
    in_degree = {i : 0 for i in range(1, len(nums) + 1)}

    # graph
    graph = defaultdict(list)
    for seq in sequences:
        for i in range(len(seq) - 1):
            graph[seq[i]].append(seq[i + 1])
            in_degree[seq[i + 1]] += 1

    # topological sorting
    q = deque(node for node in range(1, len(nums) + 1) if in_degree[node] == 0)
    idx = 0

    while q:
        if len(q) > 1:
            return False
        node = q.popleft()
        if nums[idx] != node:
            return False
        idx += 1
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                q.append(neighbor)

    return idx == len(nums)

