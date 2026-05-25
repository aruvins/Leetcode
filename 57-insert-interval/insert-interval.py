class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]: # Append to the beginning (new Interval's end value is less than the current intervals start value)
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]: # Append to the end (new Interval's start value is greater than the current intervals end value)
                res.append(intervals[i])
            else: # Overlapping interval (Grab the minimum start value and max end value)
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                ]


        res.append(newInterval)
        return res