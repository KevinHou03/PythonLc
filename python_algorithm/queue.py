# 环形结构
class Queue:
    def __init__(self, size=100):
        self.size = size
        self.queue = [0 for _ in range(size)]
        self.rear = 0  # 队尾指针
        self.front = 0  # 队首指针
        # 一开始首尾都指向相同的位置

    # 用取余来获得每加入/删除一个元素后rear和front的下标，front不会指向元素，front+1才会
    def push(self, element):
        if not self.is_full():
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = element
        else:
            raise IndexError("Queue is full")
            # 下面两行是另一种方式，即满了之后挤一个出去
            # self.pop()
            # self.push(element)

    def pop(self):  # 你pop一个元素出去了，front要往后面挪一个
        if not self.is_empty():
            self.front = (self.front + 1) % self.size
            return self.queue[self.front]  # -1?
        else:
            raise IndexError("Queue is empty!")

    def is_empty(self):
        return self.rear == self.front

    def is_full(self):
        return (self.rear + 1) % self.size == self.front


q = Queue(5)  # 长度是5的队列只能存4个数
for i in range(5):
    q.push(i)

print(q.is_full())
print(q.pop())  # 0
print(q.pop())  # 1
print(q.pop())
print(q.pop())
