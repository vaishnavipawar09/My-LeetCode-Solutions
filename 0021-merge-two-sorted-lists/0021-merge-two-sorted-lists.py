# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Iterative method - optimal 
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()          #create a dummy list for output
        tail = dummy                #tail will be dummy
        l1, l2 = list1, list2

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
        else:
            tail.next = l2    
        
        return dummy.next           #return the dummy list

#Time Complexity: O(n + m)
#Space Complexity: O(1)



    
        