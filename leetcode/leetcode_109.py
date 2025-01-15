# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        slow = head
        fast = head
        mid = slow

        while fast and fast.next:
            mid = slow
            fast = fast.next.next
            slow = slow.next

            node = TreeNode(slow.val)

            mid.next = None
            node.left = self.sortedListToBST(head)
            node.right = self.sortedListToBST(slow.next)

            return node

