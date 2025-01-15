# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def addTwoNumbers(l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 传进去的是head
        result_linked_list = l1
        list1 = []
        list2 = []
        current1 = l1
        current2 = l2
        while current1:
            list1.append(current1.val)
            current1 = current1.next
        while current2:
            list2.append(current2.val)
            current2 = current2.next
        list1.reverse()
        list2.reverse()
        result1_str = ''
        result2_str = ''
        for digit in list1:
            result1_str += str(digit)
        for digit in list2:
            result2_str += str(digit)
        result1_str = int(result1_str)
        result2_str = int(result2_str)
        result = result2_str + result1_str
        digits = [int(digit) for digit in str(result)]
        print(digits)
        Nodefirst = ListNode(digits[0])
        NodeFirstrecord = Nodefirst
        for digit in digits[1:]:
            currentNode = ListNode(digit)
            Nodefirst.next = currentNode
            Nodefirst = Nodefirst.next

        return NodeFirstrecord



def main():
# 创建链表节点
    node1 = ListNode(2)
    node2 = ListNode(4)
    node3 = ListNode(3)

    node4 = ListNode(5)
    node5 = ListNode(6)
    node6 = ListNode(4)

    # 构建链表 l1: 2 -> 4 -> 3
    node1.next = node2
    node2.next = node3
    l1 = node1

    # 构建链表 l2: 5 -> 6 -> 4
    node4.next = node5
    node5.next = node6
    l2 = node4


    def print_linked_list(head):
        current = head
        while current:
            print(current.val)
            current = current.next


    # 假设 l2 是链表的头部
    print_linked_list(l2)
    print_linked_list(l1)
    ListNode1 = ListNode
    print(ListNode1.addTwoNumbers(l1,l2))

if __name__ == "__main__":
    main()