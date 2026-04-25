class TimeMap:
    def __init__(self):
        self.store = {}

    def _insert(self, key: str, value: str, timestamp: int):
        store_val = self.store.get(key, [])
        left, right = 0, len(store_val) - 1

        while left <= right:
            mid = left + (right - left) // 2
            comp_ts = store_val[mid][0]

            if timestamp > comp_ts:
                left = mid + 1
            else:
                right = mid - 1

        new_store_val = store_val[:left] + [[timestamp, value]] + store_val[left:]
        self.store[key] = new_store_val

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [[timestamp, value]]
        else:
            self._insert(key, value, timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        store_val = self.store[key]
        left, right = 0, len(store_val) - 1

        while left <= right:
            mid = left + (right - left) // 2
            comp_ts = store_val[mid][0]

            if comp_ts > timestamp:
                right = mid - 1
            else:
                left = mid + 1

        return store_val[right][1] if right >= 0 else ""
