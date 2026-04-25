class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
            [1,3], [1,5], [6,7]

            [1]
        """

        intervals = sorted(intervals, key =  lambda a: (a[0],a[1]))
        result = [intervals[0]]

        for i in range(1, len(intervals)):
            if result[-1][1] >= intervals[i][0]:
                result[-1][1] = max(result[-1][1], intervals[i][1])
            
            else:
                result.append(intervals[i])
        
        return result

