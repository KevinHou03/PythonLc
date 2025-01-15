def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """
    i = 1
    while i < len(intervals):
        if intervals[i][0] <= intervals[i - 1][1]:
            intervals[i - 1][1] = max(intervals[i][1], intervals[i - 1][1])
            del intervals[i]
        else:
            i += 1

    return intervals


print(merge([[1, 4], [4, 5]]))


def insert(intervals, newInterval):
    """
    :type intervals: List[List[int]]
    :type newInterval: List[int]
    :rtype: List[List[int]]
    """
    for i in range(0, len(intervals) - 1):
        if intervals[i][0] <= newInterval[0] <= intervals[i + 1][0]:
            intervals.insert(i + 1, newInterval)

    else:
        intervals.append(newInterval)

    return merge(intervals)


intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
new_interval = [4, 8]
print(insert(intervals, new_interval))
