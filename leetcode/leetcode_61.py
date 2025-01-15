# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def rotateRight(head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    if not head:
        return head
    if head.next is None:
        return head
    if head.next.next is None:
        if k % 2 == 0:
            return head
        else:
            new_head = head.next
            head.next.next = head
            head.next = None
            return new_head
    tail = head
    count = 1
    while tail.next is not None:
        tail = tail.next
        count += 1

    if k == count:
        return head
    # if k > count:
    #     k = k - count
    while k > count:
        k = k - count
    # tail 在尾部
    current = head
    for i in range(count - k - 1):
        current = current.next
    next_node = current.next
    tail.next = head
    current.next = None
    return next_node




def rotate(head):
    if not head or not head.next:
        return head

    temp = head
    current = head
    next_node = current.next
    while next_node.next is not None:
        current = current.next
        next_node = next_node.next
        # now current is the last element
    next_node.next = temp
    head = next_node
    current.next = None

    return head


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)

head = rotateRight(head,10)
current = head

while current is not None:
    print(current.val)
    current = current.next



def rotate_list(head):
    prev = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    head = prev
    return head