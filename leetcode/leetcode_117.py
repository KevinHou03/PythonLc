
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        head = root

        while head:
            dummy = Node(0)
            temp = dummy
            '''
            At the beginning of each level, temp is assigned to dummy, so temp and dummy point to the same object.
            Any change to temp.next will also update dummy.next because they both refer to the same object.
            
            After the first connection, temp moves away from dummy:

            When temp is updated with temp = temp.next, temp no longer points to dummy.
            Any subsequent updates to temp.next do not affect dummy.next because temp now points to a new object (the last connected node).

            '''
            while head:
                if head.left:
                    temp.next = head.left
                    temp = temp.next
                if head.right:
                    temp.next = head.right
                    temp = temp.next
                head = head.next # Move to the next node in the current level

            head = dummy.next
        return root

