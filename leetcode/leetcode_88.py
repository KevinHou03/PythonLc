def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    index1, index2 = m - 1, n - 1
    # 从nums1的实际末尾开始填充
    merge_index = m + n - 1

    # 当两个数组都还有元素时
    while index1 >= 0 and index2 >= 0:
        # 取两者中较大的值放到nums1的末尾
        if nums1[index1] > nums2[index2]:
            nums1[merge_index] = nums1[index1]
            index1 -= 1
        else:
            nums1[merge_index] = nums2[index2]
            index2 -= 1
        merge_index -= 1

    # 如果nums2中还有元素未合并（nums1中的元素已经在正确位置），直接复制到nums1的前面
    while index2 >= 0:
        nums1[merge_index] = nums2[index2]
        index2 -= 1
        merge_index -= 1


nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]

merge(nums1,3,nums2,3)
print(nums1)



