class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prior = None


a = Node(1)
b = Node(2)
c = Node(3)


def traverse_list(head):
    current = head
    while current:
        print(current.item)
        current = current.next


a.next = b
b.next = c

c.prior = b
b.prior = a

traverse_list(a)  # 123


def create_linked_list_addFirst(li):
    head = Node(li[0])
    for element in li[1:]:
        node = Node(element)
        node.next = head
        head.prior = node
        head = node
    return head


print('test for create addFirst list')
traverse_list(create_linked_list_addFirst([1, 2, 3, 4, 5, 6]))


def create_linked_list_addLast(li):
    head = Node(li[0])
    tail = head
    for element in li[1:]:
        node = Node(element)
        tail.next = node
        node.prior = head
        tail = node
    return head


print('test for create addLast list')
example1 = create_linked_list_addLast([1, 2, 3, 4, 5, 6])
traverse_list(create_linked_list_addLast([1, 2, 3, 4, 5, 6]))


def insert(head, val, pos):
    current_node = head
    next_node = head
    new_node = Node(val)
    for i in range(0, pos - 1):
        current_node = current_node.next
        next_node = current_node.next
    new_node.next = next_node
    next_node.prior = new_node
    current_node.next = new_node
    new_node.prior = current_node

    return head


print('test for insert')
traverse_list(insert(example1, 9, 3))


def delete(head, pos):
    previous_node = head
    current_node = head
    next_node = head
    for i in range(0, pos):
        previous_node = current_node
        current_node = current_node.next
        next_node = current_node.next
    previous_node.next = next_node
    next_node.prior = previous_node

    return head

print('test for delete')
traverse_list(delete(example1, 3))