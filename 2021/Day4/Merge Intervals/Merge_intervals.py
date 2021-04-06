from collections import defaultdict
#By CyFun

class Solution(object):
    def __init__(self):
        self.startToEnds = defaultdict(list)

    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        for (start, end) in intervals:
            self.startToEnds[start].append(end)

        intervals = [[start, max(endList)]
                     for start, endList in self.startToEnds.items()]
        intervals.sort(key=lambda x: x[0])

        mergedIntervals = []
        for interval in intervals:
            if not mergedIntervals or interval[0] > mergedIntervals[-1][1]:
                mergedIntervals.append(interval)
            else:
                mergedIntervals[-1][1] = max(mergedIntervals[-1]
                                             [1], interval[1])

        return mergedIntervals
