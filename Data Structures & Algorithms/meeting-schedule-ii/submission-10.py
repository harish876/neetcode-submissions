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
            (0,40) (5,10)(15,20)

            (0,1),(40,-1),(5,1),(10,-1),(15,1),(20,-1)

            (0,1),(5,1),(10,-1),(15,1),(20,-1),(40,-1)
                                                    2  
        """

        events = []
        for interval in intervals:
            events.append((interval.start,1))
            events.append((interval.end,-1))
        
        events = sorted(events)

        curr = 0
        result = 0

        for ts,marker in events:
            curr += marker
            result = max(result,curr)

        return result 