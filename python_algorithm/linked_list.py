class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c

print(a.next.next.item)  # 3

current = a
while current:
    print(current.item)
    current = current.next


# 创建linkedList addFirst 和 addLast
def create_linked_list_addFirst(li):  # 把list转换为linkedList,用addFirst
    head = Node(li[0])
    for element in li[1:]:
        node = Node(element)
        node.next = head
        head = node
    return head


def traverse_linked_list(head):
    currentHead = head
    while currentHead:
        print(currentHead.item)
        currentHead = currentHead.next


create_linked_list_addFirst([1, 2, 3, 4, 5,6,7,8,9,0])
traverse_linked_list(create_linked_list_addFirst([1, 2, 3, 4, 5]))

print('addLast 测试')


def create_linked_list_addLast(li):
    head = Node(li[0])
    tail = head
    for element in li[1:]:
        node = Node(element)
        tail.next = node
        tail = node
    return head


example1 = create_linked_list_addLast([1, 2, 3, 4, 5])
traverse_linked_list(create_linked_list_addLast([1, 2, 3, 4, 5]))


def insert(head, value, pos):
    current_node = head
    next_node = head
    new_node = Node(value)
    for i in range(0, pos - 1):
        current_node = current_node.next
        next_node = current_node.next
    current_node.next = new_node
    new_node.next = next_node

    return head


print('test for insert')
traverse_linked_list(insert(example1, 9, 4))


def delete(head, pos):
    previous_node = head
    current_node = head
    next_node = head
    for i in range(0, pos):
        previous_node = current_node
        current_node = current_node.next
        next_node = current_node.next
    previous_node.next = next_node
    return head


print('test for delete')
traverse_linked_list(delete(example1, 2))

print("")


def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    cur1 = head
    cur2 = head
    count = 0
    while cur1.next is not None:
        cur1 = cur1.next
        count += 1
    count += 1
    count2 = count - n
    for i in range(0, count2 - 1):
        cur2 = cur2.next
    cur2.next = cur2.next.next
    return count


print(removeNthFromEnd(example1, 5))

print("")
traverse_linked_list(removeNthFromEnd(example1, 2))
