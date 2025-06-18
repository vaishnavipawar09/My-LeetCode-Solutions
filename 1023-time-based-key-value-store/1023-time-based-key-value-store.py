class TimeMap:
    def __init__(self):
        self.store = {}  # key -> list of (timestamp, value)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:       #chcek if key exist in the store
            self.store[key] = []  # initialize with an empty list
        self.store[key].append((value, timestamp))  # append the new (timestamp, value) pair
     
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:       #if key did not exist return ""
            return ""

        res = ""
        values = self.store.get(key, [])  #if find the match returns the list if not return empty []
        l = 0                               #left ptr
        r = len(values) - 1                 #right ptr at the end of list
        

        while (l <= r):                     #if l hasn't crossed right run the loop
            mid = (l + r ) // 2             #cal mid value

     #compare mid is valyes, 0 is the timestamp, so check if it <= timestamp, to check if it exist
            if values[mid][1] <= timestamp: 
                res = values[mid][0]
                l = mid + 1                 #search right portion
            else:
                r = mid - 1                 #search left portion of the list, 
                                            #cant assign result here as it invalid value
           
        return res                          #return the result

        
#Time Complexity ; SET : O(1), GET : O(log n)
#Space Complexity: O(m * n),  n = total no of values, m = total no. of keys

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)