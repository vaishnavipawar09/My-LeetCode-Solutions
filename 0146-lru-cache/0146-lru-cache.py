class Node:                                 #Create a node funt class                                 
    def __init__(self, key, val):
        self.key, self.val = key, val       #it will have a key value pair and two ptrs, prev and next node      
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity                 #store the capacity cause we have to know it it goes over 
        self.cache = {}                     # map key to node -  A hashmap key value pair

        #leftt = Least recently used,  Right = Most recently used
        self.left, self.right = Node(0, 0), Node(0, 0)  #Dummy nodes, which tells us the most recent nd the least recent 
        self.left.next, self.right.prev = self.right, self.left #Connect the nodes to each other (doubly linked list)

    def remove(self, node):                 #Node to remove from the doubly linked list 
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev     #update the next and prev nodes

    def insert(self, node):                 #Insert the node from the right to the cache
        prev, nxt = self.right.prev, self.right #Get by using the rightmost ptrs
        prev.next = nxt.prev = node         #insert in between the rihght and prev, pt to the node
        node.next, node.prev = nxt, prev    #assign to the next and prev from the node

    def get(self, key: int) -> int:
        if key in self.cache:               #If key exists 
            self.remove(self.cache[key])    #first remove the key and insert it to the right most position
            self.insert(self.cache[key])
            return self.cache[key].val      #If key is in our cache, return the value
        return -1                           #doesnt exist return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:               #If key exists, that means the node exists      
            self.remove(self.cache[key])    #so remove the node 
        self.cache[key] = Node(key, value)  #put that in our hashmap
        self.insert(self.cache[key])        #insert it into the list too (DLL)

        if len(self.cache) > self.cap:      #check if the len of cache exceeds the capacity
            lru = self.left.next            #remove from the list and delete the lru from the hashmap 
            self.remove(lru)                #(this is the least recently used)
            del self.cache[lru.key]         #delete from hashmap

#Time Complexity : O(1) for both get and put
#Space Complexity : O(n)




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)