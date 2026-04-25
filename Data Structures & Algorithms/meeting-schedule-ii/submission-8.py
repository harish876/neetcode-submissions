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
        # print([(i.start,i.end) for i in intervals])
        if len(intervals) == 0:
            return 0

        groups = [intervals[0]]

        for i in range(1, len(intervals)):
            count, group_idx = 0, len(groups)
            for idx,last_interval in enumerate(groups):
                if last_interval.end > intervals[i].start:
                    count += 1
                
                else:
                    group_idx = min(group_idx, idx)

            if count == len(groups):
                groups.append(intervals[i])
            
            else:
                groups[group_idx] = intervals[i]

        # print([(i.start,i.end) for i in groups])
        return len(groups)
