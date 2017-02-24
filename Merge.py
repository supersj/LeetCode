class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


def merge( intervals):
    """
    :type intervals: List[Interval]
    :rtype: List[Interval]
    """
    result = []
    if len(intervals) == 0:
        return []
    if len(intervals) == 1:
        return intervals
    intervals.sort(key=lambda x: x.end)
    intervals.sort(key=lambda x: x.start, reverse=True)
    tmp = intervals.pop()
    while len(intervals) != 0:
        cur = intervals.pop()
        if cur.start > tmp.end:
            result.append(tmp)
            tmp = cur
        else:
            if cur.end < tmp.end:
                continue
            else:
                tmp.end = cur.end
    result.append(tmp)
    return result


a = Interval(1,4)
b = Interval(5,6)
intervals = [a,b]
print(merge(intervals)[0].start)
