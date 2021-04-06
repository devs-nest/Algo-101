class Solution:  # ByCyFun
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        index = 0
        ret = []
        while index < len(intervals) and intervals[index][1] < newInterval[0]:
            ret += [intervals[index]]
            index += 1

        while index < len(intervals) and newInterval[1] >= intervals[index][0]:
            newInterval[0] = min(newInterval[0], intervals[index][0])
            newInterval[1] = max(newInterval[1], intervals[index][1])
            index += 1

        ret += [newInterval]
        return ret + intervals[index:]
