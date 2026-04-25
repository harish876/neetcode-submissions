class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """

            minimum intervals needed to be removed

            [0,1], [1,3], [3,5], [4,6]

        """

        intervals = sorted(intervals, key = lambda a: (a[1],a[0]))
        last_interval, result = intervals[0], 0
        print(intervals)

        for i in range(1, len(intervals)):
            if last_interval[1] > intervals[i][0]:
                result += 1
            
            else:
                last_interval = intervals[i]
            
        return result