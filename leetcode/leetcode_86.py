# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        if not head:
            return None
        # if head.val < x and head.next is None:
        #     return head

        # while prev.val < x and prev.next.val < x:
        while prev.next.val < x:
            prev = prev.next
            if prev.next is None:
                return head
            # 现在prev。next就是我们要插入的位置
        current = prev
        while current and current.next:
            if current.next.val < x:
                temp = prev.next
                # delete the node that's found smaller than x
                insert_value = current.next
                current.next = current.next.next
                # insert current.next to prev.next and then update pre to prev.next
                insert_value.next = temp
                prev.next = insert_value
                prev = prev.next
            else:
                current = current.next

        return dummy.next


l1 = ListNode(1)
# l1.next = ListNode(1)
# l1.next.next = ListNode(3)
# l1.next.next.next = ListNode(4)
# l1.next.next.next.next = ListNode(1)
# l1.next.next.next.next.next = ListNode(5)
# l1.next.next.next.next.next.next = ListNode(2)

solution = Solution()

new_head = solution.partition(l1, 3)
while new_head is not None:
    print(new_head.val)
    new_head = new_head.next
