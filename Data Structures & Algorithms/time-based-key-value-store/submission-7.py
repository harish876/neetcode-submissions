class SortedList:

    def __init__(self):
        self._nums = []
        self.length = 0

    def insert(self, val: str, timestamp: int):
        left, right = 0, self.length

        while left < right:
            mid = left + (right - left) // 2

            if self._nums[mid][1] >= timestamp:
                right = mid
            
            else:
                left = mid + 1

        self._nums.insert(left, (val,timestamp))
        self.length += 1

    def find(self, timestamp: int):
        left, right = 0, self.length - 1
        result = -1

        while left <= right:
            mid = left + (right - left) // 2

            if self._nums[mid][1] <= timestamp:
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        if result == -1:
            return "", -1

        return self._nums[result]
    
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
        
