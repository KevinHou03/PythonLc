def merge_lists(a, b):
    i, j = 0, 0
    result = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(a[j])
            j += 1
    if i < len(a):
        result.extend(a[i:])
    if j < len(b):
        result.extend(b[j:])
    return result



a = [1,2,3,4,5]
b = [1,2,3,4]
print(merge_lists(a,b))

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    dummy = ListNode()
    current = dummy
    while list1 is not None and list2 is not None:
        if list1.val <= list2.val:
            current.next = list1.val
            list1 = list1.next
        else:
            current.next = list2.val
            list2 = list2.next
        current = current.next

    if list1:
        current.next = list1
    if list2:
        current.next = list2
    return dummy.next
