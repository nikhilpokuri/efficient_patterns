intervals = [[1,3],[6,7],[8,10],[10,18],[2,5]]
def merge(intervals):
    intervals.sort()
    res = [intervals[0]]
    for start, end in intervals[1:]:
        last_end = res[-1][1]
        if start <= last_end:
            res[-1][1] = max(end, last_end)
        else:
            res.append([start,end])
    del intervals #to save the memory[optional]
    return res

print(merge(intervals))