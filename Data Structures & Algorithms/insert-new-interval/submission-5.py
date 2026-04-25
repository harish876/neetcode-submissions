class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        result = []

        """
            [1,5] [2,6] 
            [0,0]
        """

        for interval in intervals:
            if interval[1] < newInterval[0]:
                # new interval after the existing interval
                result.append(interval)

            elif interval[0] > newInterval[1]:
                # new interval before the existing interval
                result.append(newInterval)
                newInterval = interval
            
            else:
                newInterval = [
                    min(newInterval[0],interval[0]),
                    max(newInterval[1],interval[1])
                ]
        
        result.append(newInterval)
        return result