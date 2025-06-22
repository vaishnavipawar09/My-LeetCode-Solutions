# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:    #If list is empty or if its len is 0 return empty linked list
            return None

        while len(lists) > 1:           #take pairs of linked list and merge them every time until you get only one list
            mergedLists = []              #make a new list 

            for i in range(0, len(lists), 2):   #iterate through each list, pair of linked list so 2 is the incrementer
                l1 = lists[i]                   #first at index i 
                l2 = lists[i+1] if (i + 1) < len(lists) else None   #list 2 can be null, so check for inbound, check if it is small then the other
                mergedLists.append(self.mergeList(l1, l2))  #Take both the list and merge  them together
            lists = mergedLists                 #temp var to update it there
            
        return lists[0]                         #retuurn that list 


    def mergeList(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:     #if list 1 value is less than list 2 value 
                tail.next = l1      # attach l1’s node to tail
                l1 = l1.next        # move l1 forward
            else:                   #if lit 2 is less than or equal than list 1
                tail.next = l2
                l2 = l2.next
            tail = tail.next        # move tail forward (update regardless of which node we insert into the list)

        if l1:                      #if one is empty, then find the non empty lit and add it at the end of the list
            tail.next = l1
        if l2:
            tail.next = l2    
            
        return dummy.next           #return the dummy list