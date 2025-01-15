
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def reverse_linkedlist(self, head):
        current = head
        pre = None
        while current != None:
            next_node = current.next
            current.next = pre
            pre = current
            current = next_node
        return pre

    def reverse_linkedlist_restricted(self, head, length):
        current = head
        pre = None
        for i in range(length):
            next_node = current.next
            current.next = pre
            pre = current
            current = next_node
        return pre


    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        current = dummy
        for i in range(left - 1):
            current = current.next
        temp_head = current.next
        tail_tracker = current.next
        for j in range(right - left + 1):
            tail_tracker = tail_tracker.next
        current.next = self.reverse_linkedlist_restricted(current.next, right - left + 1 )
        temp_head.next = tail_tracker
        return dummy.next

    def reverseBetween2(self, head, left, right):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Move prev to the node before the left position
        for _ in range(left - 1):
            prev = prev.next

        # Reverse the sublist from left to right
        current = prev.next
        for _ in range(right - left):
            next_node = current.next
            current.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node

        return dummy.next


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next = ListNode(7)
head.next.next.next.next.next.next.next = ListNode(8)


head = ListNode().reverseBetween(head,1,3)
while head!= None:
    print(head.val)
    head = head.next






