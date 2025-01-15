def canAttendMeetings(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: bool
    """
    if len(intervals) == 1:
        return True
    intervals.sort()
    for i in range(1,len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False
    return True



intervals = [[7,10],[2,4]]
print(sorted(intervals))

print(canAttendMeetings(intervals))