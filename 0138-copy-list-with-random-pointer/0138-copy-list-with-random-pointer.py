"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
#Method 1 : Two pass Hash map technique
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        hashmap = {} #key, value
        
        #First pass, creation the hashmap and start storing the values in it
        curr = head
        while curr:                         #run until the list end
            hashmap[curr] = Node(curr.val)  #create hashmap and store the value of the node
            curr = curr.next                #update the curr ptr until it reaches null

        #Second pass, start connecting the ptrs of the list, like original list
        curr = head                         #start with the node
        while curr:                         #run unti the list end
            copy = hashmap[curr]            #create a copy and set the hashmap
            if curr.next:                   #check if it empty or not
                copy.next = hashmap[curr.next]  #map the original node to the copy next node
            if curr.random:                 #check if it is empty or not
                copy.random = hashmap[curr.random] #map the original node to the copy random node
            curr = curr.next                #update the curr ptr until it reaches null

        return hashmap[head]                #return the head of the copy list 

#Time Complexity: O(n)
#Space Complexity : O(n)


        