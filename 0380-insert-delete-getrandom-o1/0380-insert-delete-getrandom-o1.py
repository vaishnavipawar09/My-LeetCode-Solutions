import random

class RandomizedSet:
    def __init__(self):
        self.nums = []          # List for O(1) random access
        self.pos = {}           # Hashmap , Dict for O(1) insert/remove: val -> index

    def insert(self, val: int) -> bool:
        if val in self.pos:     #if val in the hashmap, return false
            return False
        self.nums.append(val)   #if val is not in the list, add it to the list
        self.pos[val] = len(self.nums) - 1  #Record the index of the added value in the hashset 
        return True             #return True if inserted

    def remove(self, val: int) -> bool:
        if val not in self.pos: #check if val not present in the map, nothing to find so return False
            return False
        idx = self.pos[val]     #else, get the index from the map and the last val from the list
        last_val = self.nums[-1]
        # Swap with last and update
        self.nums[idx] = last_val
        self.pos[last_val] = idx
        # Remove last
        self.nums.pop()
        del self.pos[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums) #use random built in function to get the random

#Time Complexity : for each function is O(1)
#Space Complexity: O(n)
