# Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), determine if a person could add all meetings to their schedule without any conflicts.

# Example 1:

# Input: intervals = [(0,30),(5,10),(15,20)]

# Output: false
# Explanation:

# (0,30) and (5,10) will conflict
# (0,30) and (15,20) will conflict
# Example 2:

# Input: intervals = [(5,8),(9,15)]

# Output: true
# Note:

# (0,8),(8,10) is not considered a conflict at 8
# Constraints:

# 0 <= intervals.length <= 500
# 0 <= intervals[i].start < intervals[i].end <= 1,000,000


# Solution:

from typing import List

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda i: i.start)
        for i in range(len(intervals) - 1):
            if intervals[i].end > intervals[i+1].start:
                return False
        return True