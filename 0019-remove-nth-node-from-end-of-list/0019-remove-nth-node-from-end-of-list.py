# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)   #next ptr must be head
        left = dummy                #left to dummy
        right = head                #we actually need it to be head + 2 or (n)

        while n > 0 and right:      #while n is greater than 0 and right is not null
            right = right.next      #shift right by one step
            n -= 1                  #shift till you have the ptr you needed (before the deletion)

        while right:                #while right is not null
            left = left.next
            right = right.next      #shift bot ptrs by one step
        
        #delete the node
        left.next = left.next.next  #assign the ptrs to next node of the deletion node
        return dummy.next           #cause we want to not include the dummy node           

#Time Complexity: O(n)
#Space Complexity: O(1)