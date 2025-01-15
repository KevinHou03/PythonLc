def merge(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """

    def helper(sub_intervals, start):
        intervals.sort(key=lambda x: x[0])
        swapped = False
        i = start
        while i < len(sub_intervals):
            if sub_intervals[i][0] <= sub_intervals[i - 1][1]:
                sub_intervals[i - 1][1] = max(sub_intervals[i][1], sub_intervals[i - 1][1])
                del sub_intervals[i]
                swapped = True
            else:
                i += 1
        if swapped:
            return helper(sub_intervals, i)
        else:
            return sub_intervals

    return helper(intervals, 1)


print(merge([[1, 4], [4, 5]]))
