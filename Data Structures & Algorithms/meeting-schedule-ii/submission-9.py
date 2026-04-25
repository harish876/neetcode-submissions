"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        """ 
            Find minimum days to schedule meets
            [(25, 579), (218, 918), (1281, 1307), (623, 1320), (685, 1353), (1308, 1358)]
            [                                                       |
                (623, 1320)
                (218,918)
                (1281, 1307)
            ]

            (5,8)
        """

        intervals = sorted(intervals, key= lambda a: (a.start,a.end))
        if len(intervals) == 0:
            return 0

        groups = [intervals[0].end]

        for i in range(1, len(intervals)):            
            if groups[0] <= intervals[i].start:
                heapq.heappop(groups)
            
            heapq.heappush(groups,intervals[i].end)

        return len(groups)
