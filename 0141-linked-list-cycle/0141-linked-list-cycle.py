# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head                 #use two ptrs, one slow and one fast assign both to head
        fast = head

        if head is None or head.next is None:#handle edge case where 1 or 0 node cant have a cycle
            return False            #return false immediately , means no cycle

        while fast and fast.next:   #We must make sure fast and fast.next are not none, if one is none, loop exits
            slow = slow.next        #move slow by 1 space 
            fast = fast.next.next   #move fast by 2 space
        
            if slow == fast:        #if both are equal we get a cyclic linked list
                return True         #return true if yes

        return False                #no cyclic linked list found
        
#Time Complexity: O(n)
#Space Complexity: O(1)