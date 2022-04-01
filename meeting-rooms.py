def mr(intervals):
    intervals.sort(key=lambda i: i[0])

    for i in range(1, len(intervals)):
        prev = intervals[i - 1]
        if intervals[i][0] < prev[1]:
            return False

    return True

print(mr([(0,30), (5,10), (15,20)]))