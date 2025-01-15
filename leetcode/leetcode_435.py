def eraseOverlapIntervals(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: int
    """

    intervals.sort()
    res = 0
    cur_end = intervals[0][1]

    for start, end in intervals[1:]:
        if start >= cur_end:
            cur_end = end
        else:
            res += 1
            cur_end = min(cur_end, end)
    return res

