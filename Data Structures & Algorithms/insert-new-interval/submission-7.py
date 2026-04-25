class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
            doing sweep line

            python doesnt have sorted maps remember
        """

        mp = defaultdict(int)
        for start,end in intervals:
            mp[start] += 1
            mp[end] -= 1
        
        mp[newInterval[0]] += 1
        mp[newInterval[1]] -= 1

        result = []
        start, count = 0, 0

        for k in sorted(mp):
            if count == 0:
                start = k
            
            count += mp[k]

            if count == 0:
                result.append([start, k])

        return result


