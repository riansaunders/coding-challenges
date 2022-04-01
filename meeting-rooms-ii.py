def mr2(intervals):
    intervals.sort(key=lambda i: i[0])
    starts = [ intervals[i][0] for i in range(len(intervals)) ]
    ends = [ intervals[i][1] for i in range(len(intervals)) ]

    res, count = 0, 0

    s, e = 0, 0

    while s < len(intervals):

        if starts[s] < ends[e]:
            s += 1
            count += 1
        else:
            e += 1
            count -= 1

        res = max(res, count)
    
    return res
