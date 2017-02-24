class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


def insert(intervals, newInterval):
    """
    :type intervals: List[Interval]
    :type newInterval: Interval
    :rtype: List[Interval]
    """
    # binary search
    length = len(intervals)
    start = 0
    end = length
    interval = Interval()
    if length == 0:
        intervals.append(newInterval)
        return intervals
    while start < end:
        mid = (start + end)//2
        if newInterval.start < intervals[mid].start:
            end = mid
        else:
            start = mid + 1
    left = 0
    right = length - 1
    if start == 0:
        left = start
        interval.start = newInterval.start
    else:
        if newInterval.start <= intervals[start - 1].end:
            left = start - 1
            interval.start = intervals[start - 1].start
        else:
            left = start
            interval.start = newInterval.start
    for i in range(left,length):
        if newInterval.end < intervals[i].start:
            right = i - 1
            break
    if right != -1:
        if newInterval.end > intervals[right].end:
            interval.end = newInterval.end
        else:
            interval.end = intervals[right].end
    else:
        interval.end = newInterval.end
    intervals[left:right+1] = []
    intervals.insert(left,interval)
    return intervals

a = Interval(2,5)
b = Interval(6,7)
c = Interval(8,9)
d = Interval(0,1)
intervals = [a,b,c]

insert(intervals,d)

print(intervals)
