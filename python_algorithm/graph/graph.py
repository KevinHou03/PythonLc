import queue


class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.color = 'white'  # New property to track node color
        self.distance = 0  # New property to track node distance from start
        self.pred = None  # New property to track predecessor node

    def add_neighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + 'connectedTo: ' \
            + str([x.id for x in self.connectedTo])

    def get_connection(self):
        return self.connectedTo.keys()

    def get_id(self):
        return self.id

    def get_weight(self, nbr):
        return self.connectedTo[nbr]

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_distance(self, distance):
        self.distance = distance

    def get_distance(self):
        return self.distance

    def set_pred(self, pred):
        self.pred = pred

    def get_pred(self):
        return self.pred


class Graph:
    def __init__(self):
        self.verti_list = {}
        self.num_vertices = 0

    def add_vertex(self, key):
        self.num_vertices += 1
        new_vertex = Vertex(key)
        self.verti_list[key] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.verti_list:
            return self.verti_list[n]
        else:
            return None

    def __contains__(self, item):
        return item in self.verti_list

    def add_edge(self, f, t, cost=0):
        if f not in self.verti_list:
            new_vertex = self.add_vertex(f)
        if t not in self.verti_list:
            new_vertex = self.add_vertex(t)
        self.verti_list[f].add_neigbor(self.verti_list[t], cost)

    def get_vertices(self):
        return self.verti_list.keys()

    def __iter__(self):
        return iter(self.verti_list.values())


def bfs(g, start):
    start.set_distance(0)
    start.set_pred(None)
    vert_queue = queue.Queue()
    vert_queue.put(start)
    while not vert_queue.empty():
        current_vert = vert_queue.get()
        for nbr in current_vert.get_connection():
            if nbr.get_color() == 'white':
                nbr.set_color('gray')
                nbr.set_distance(current_vert.get_distance() + 1)
                nbr.set_pred(current_vert)
                vert_queue.put(nbr)
        current_vert.set_color('black')


def knights_tour(n, path, u, limit):  # 骑士周游，能否走遍整个棋盘？确保每个格子都被访问一次且不重复
    # n 当前已经走了多少步了， path是路径， u当前current vert， limit总深度，比如8x8就是limit = 63
    # 因为我们要返回上一层，所以我们用stack
    u.set_color('gray')
    path.append(u)
    if n < limit:
        nbr_list = list(u.get_connection())
        i = 0
        done = False
        while i < len(nbr_list) and not done:
            if nbr_list[i].get_color() == 'white':
                done = knights_tour(n + 1, path, nbr_list[i + 1], limit)
            i += 1
        if not done:  # 这条路线走不通，回溯
            path.pop()
            u.set_color('white')
    else:
        done = True
    return done
