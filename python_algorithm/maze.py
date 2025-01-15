# 用二维列表表示迷宫，0是通道，1是围墙，给算法要求求出路径
from collections import deque

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# 封装所有可走的方向
directions = [
    lambda x, y: (x + 1, y),
    lambda x, y: (x - 1, y),
    lambda x, y: (x, y - 1),
    lambda x, y: (x, y + 1)
]


# 使用stack -- 深度优先搜索
def maze_path(x1, y1, x2, y2):  # 分别代表起点终点位置
    global nextNode
    stack = [(x1, y1)]  # 存放走过的点： 路径
    # 找到一个能走的点，压入栈
    # 如果没有通路，则一直退退退直到起点也退出去，栈为空，所以如果栈最后为空，这代表没有路径
    while len(stack) > 0:
        # 往四个方向找可走的点，从起点开始
        curNode = stack[-1]
        # 拿到当前节点了，如果这就是终点
        if curNode[0] == x2 and curNode[1] == y2:  # 要求出路径，遍历栈
            for position in stack:
                print(position)
            return True
        # 上下左右四个点 对于(x,y)来说，上（x-1，y） 下（x+1,y) 左（x，y-1）右（x，y+1）
        for dirs in directions:  # 遍历整个lambda函数集，将依次执行每一个函数
            nextNode = dirs(curNode[0], curNode[1])
            if maze[nextNode[0]][nextNode[1]] == 0:  # 能走
                stack.append(nextNode)
                maze[nextNode[0]][nextNode[1]] = 2  # 2表示已经走过了
                break  # 找到一个可走的点，跳出if循环
        else:  # 没有一个地方可以走了，先把current这个标记为走过
            maze[nextNode[0]][nextNode[1]] = 2
            stack.pop()  # 开始回退，此时while下面的curNode = stack【-1】就是上一个新节点了，因为这个节点被pop出去了
    else:
        print('No path')
        return False


maze_path(1, 1, 8, 8)


# 使用queue -- 广度优先搜索；从一个节点开始，寻找所有接下来可以走的点，直到找到出口 并且使用队列储存当前正在考虑的节点
# 队列存放的是广度优先搜索中探索队的头的位置，每当一个点出队，他以下可走的所有点都同时入队
# 队里存的永远不是路径，是现在考虑的路的可能的方向
# 同时需要辅助列表，存放出队的元素，和他们的上一节

def print_r(path):
    curNode = path(-1)
    realPath = []
    while curNode[2] != -1:
        realPath.append((curNode[0], curNode[1]))
        curNode = path[curNode[2]]  # 则是直接跳到 到curNode的那个Node的位置下标！
    realPath.append(curNode[0:2])  # 加第一个起点进去
    realPath.reverse()
    for node in realPath:
        print(node)


def maze_path_queue(x1, y1, x2, y2):
    queue = deque()
    # 起点进队列
    queue.append((x1, y1, -1))  # 记录第一个点，并记录他是从哪里来的，在这种情况下，起点没有源头，记-1
    path = []  # 把出队的节点都放入进去
    while len(queue) > 0:  # 空了就是没有进队了，就是全死路，没路
        curNode = queue.popleft()  # 完成了出队，也把起点或者当前点存到了curNode里，注意，当前点此时已经出去了，只要把他可走的进队即可
        path.append(curNode)
        if curNode[0] == x2 and curNode[1] == y2:
            print_r(path)
            return True
        for dirs in directions:
            nextNode = dirs(curNode[0], curNode[1])
            if maze[nextNode[0]][nextNode[1]] == 0:  # 可走
                queue.append((nextNode[0], nextNode[1], len(path) - 1))  # 入队,那么他的source的位置，因为
                # 我们已经把curNode放入path了，curNode此时一定是path的最后一个节点。
                maze[nextNode[0]][nextNode[1]] = 2  # 标记已经走过
    else:
        print('No Path')
        return False


maze_path_queue(1, 1, 8, 8)
