from bisect import bisect_left
class SortedList:

    def __init__(self):
        self._nums = []
        self.length = 0

    def insert(self, val: str, timestamp: int):
        """
            target = 3
            1   2   2   3   4
            |               |
                    |
        """
        left, right = 0, self.length

        while left < right:
            mid = left + (right - left) // 2

            if self._nums[mid][1] < timestamp:
                left = mid + 1
            
            else:
                right = mid

        self._nums.insert(left, (val,timestamp))
        self.length += 1

    def find(self, timestamp: int):
        left, right = 0, self.length

        while left < right:
            mid = left + (right - left) // 2

            if self._nums[mid][1] <= timestamp:
                left = mid + 1
            else:
                right = mid
        
        if left-1 < 0:
            return "", -1

        return self._nums[left-1]
    
    @property
    def nums(self):
        return list(self._nums)


class TimeMap:

    def __init__(self):
        self.mp = defaultdict(SortedList)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # lowerbound, upperbound exercise right
        self.mp[key].insert(value,timestamp)

    def get(self, key: str, timestamp: int) -> str:
        value, _ = self.mp[key].find(timestamp)
        # print(self.mp[key].nums)
        return value
        
