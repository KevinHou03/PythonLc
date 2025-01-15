class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode()
        dummy.next = head
        current = dummy

        while current.next and current.next.next:
            one = current.next
            two = one.next
            three = two.next

            current.next = two
            one.next = three
            two.next = one

            current = current.next.next.next

        return dummy.next
