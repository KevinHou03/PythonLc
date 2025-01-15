# Definition for singly-linked list.
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
        dummy.next = head
        prev = dummy
        current = head

        while current and current.next:
            if current.val == current.next.val:
                prev.next = current.next
                current = current.next
                continue
            else:
                prev = current
            current = current.next

        return dummy.next

l1 = ListNode(1)
l1.next = ListNode(1)
l1.next.next = ListNode(2)
l1.next.next.next = ListNode(3)
l1.next.next.next.next = ListNode(3)
# l1.next.next.next.next.next = ListNode(1)
# l1.next.next.next.next.next.next = ListNode(2)

solution = Solution()

l1 = solution.deleteDuplicates(l1)
while l1 is not None:
    print(l1.val)
    l1 = l1.next
