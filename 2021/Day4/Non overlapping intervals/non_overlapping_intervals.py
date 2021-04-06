class Solution:# By CyFun
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 1:
            return 0
        intervals.sort()
        overleap = 0

        end = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                overleap += 1
                end = min(intervals[i][1], end)
            else:
                end = intervals[i][1]

        return overleap
