class TimeMap:
    def __init__(self):
        self.store = {}  # key -> list of (timestamp, value)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []  # initialize with an empty list
        self.store[key].append((timestamp, value))  # append the new (timestamp, value) pair
     
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        values = self.store[key]
        l = 0
        r = len(values) - 1
        res = ""

        while (l <= r):
            mid = (l + r ) // 2

            if values[mid][0] <= timestamp:
                res = values[mid][1]
                l = mid + 1
            else:
                r = mid - 1
           
        return res

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)