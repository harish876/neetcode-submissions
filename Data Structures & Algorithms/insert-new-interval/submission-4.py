class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
            Insert Intervals

            [[1,3], [4,6]] interval = [2,5]


            [1,2], [3,7], [4,8], [6,7], [8,10], [12,16]
            [1,2], [3,7], [6,7], [4,8], [8,10], [12,16]

            [1,2], [3,10]
        """
        # First lets insert and then sort
        intervals.append(newInterval)
        intervals = sorted(intervals, key = lambda a: (a[0],a[1]))
        print(intervals)


        # Second lets merge
        result = [intervals[0]]

        for i in range(1,len(intervals)):
            if result[-1][1] >= intervals[i][0]:
                result[-1][1] = max(result[-1][1], intervals[i][1])
            else:
                result.append(intervals[i])
        
        return result