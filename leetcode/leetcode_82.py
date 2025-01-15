class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return None

        dummy = ListNode(-1)
        prev = dummy
        dummy.next = head
        current = head

        while current is not None and current.next is not None:
            if current.val == current.next.val:
                while current.val == current.next.val:
                    current = current.next
                prev.next = current.next
            else:
                prev = current
            current = current.next


        return prev.next


l1 = ListNode(1)
l1.next = ListNode(1)
l1.next.next = ListNode(2)
# l1.next.next.next = ListNode(1)
# l1.next.next.next.next = ListNode(1)
# l1.next.next.next.next.next = ListNode(1)
# l1.next.next.next.next.next.next = ListNode(2)

solution = Solution()

# while l1 is not None:
#     print(l1.val)
#     l1 = l1.next

l1 = solution.deleteDuplicates(l1)
while l1 is not None:
    print(l1.val)
    l1 = l1.next