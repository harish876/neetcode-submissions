"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        """
        (0,30), (30,40), (40,60)
        """

        intervals = sorted(intervals, key= lambda a: (a.start,a.end))
        
        if len(intervals) == 0:
            return True

        last_interval = intervals[0]
        for i in range(1,len(intervals)):
            if last_interval.end > intervals[i].start:
                return False
            
            else:
                last_interval = intervals[i]

        return True