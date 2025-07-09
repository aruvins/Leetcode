class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        count = 1
        prevEnd = intervals[0][1]

        for i in intervals[1:]:
            if i[0] >= prevEnd:
                count += 1
                prevEnd = i[1]

        return len(intervals) - count

        