from collections import defaultdict


def canFinish(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """
    '''
    py中一般用dict来代表图
    
    visited-0:还没有访问
    visited-1：正在访问，意思是正在访问他的neighbors
    visited-2：访问完成
    
    有环：证明不行 因为全部互相dependent
    '''

    graph = defaultdict(list)
    #每一个节点代表一节课, 对应的value list里面是他相关的prerequisite
    visited = [0] * numCourses

    for a, b in prerequisites:
        '''
        ab 不能调换顺序 b是先修，有b才能a，所以b是指向这一群a的
        '''
        graph[b].append(a)

    def dfs(course):
        # 访问一个node的邻居的过程中碰见了该node，说明有个环，无法满足课程需求
        if visited[course] == 1:
            return False
        if visited[course] == 2:
            return True

        #以上都没问题，标记为正在访问该node
        visited[course] = 1

        for neighbor in graph[course]:
            if not dfs(neighbor): #如果在递归中检测到任意一个环则直接返回false
                return False

        #以上都没问题 标记为该node访问完成
        visited[course] = 2

        return True

    #每一次调用dfs（i）是对一个节点进行清扫，要对全部的node都用一遍，以防有的课单独出来和其他的课毫不相干，如果不是这样的话就扫不到他了
    for i in range(numCourses):
        if not dfs(i):
            return False

    return True


