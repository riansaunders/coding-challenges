from typing import List


def mergeIntervals(intervals: List[List[int]]):
    out = []
    intervals.sort(key = lambda i : i[0])
    for start, stop in intervals:
        if out:
            last_start, last_stop = out[-1]

            if last_stop >= start:
                
                out[len(out) - 1] = [min(last_start, start), max(last_stop, stop)]
                continue
        out.append([start, stop])
    return out

print(mergeIntervals([[1,4], [4,5]]))
print(mergeIntervals([[1,4],[0,0]]))
print(mergeIntervals([[1,0], [2,6], [8, 10], [15,18]]))