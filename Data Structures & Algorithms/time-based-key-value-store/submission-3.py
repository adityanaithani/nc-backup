class TimeMap:

    def __init__(self):
        # key: string -> value: list of (timestamp, value) tuples
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # o(1)
        # check if the key exists in self.store, create empty list if not
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # o(logn) time o(m*n) space
        if key not in self.store:
            return ""
        res = ""
        values = self.store[key]
        lo = 0 
        hi = len(values) -1 

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            time = values[mid][0]
            if time == timestamp:
                return values[mid][1]
            elif time < timestamp: 
                res = values[mid][1]
                lo = mid + 1
            else:
                hi = mid - 1

        return res

            
        # if mid_timestamp > target: hi = mid - 1
        # if mid_timestamp <= target: lo = mid + 1
        # while lo <= hi:
        #     mid = lo + (hi - lo) // 2
        #     if target == nums[mid]:
        #         return mid
        #     elif target > nums[mid]:
        #         lo = mid + 1
        #     else:
        #         hi = mid - 1
