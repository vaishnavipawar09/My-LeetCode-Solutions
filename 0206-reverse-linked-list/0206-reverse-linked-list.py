# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#by Iteration - Optimal
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None             #iniialize the prev ptr to none
        curr = head             #make a current ptr pointing at head
        
        while curr:
            temp = curr.next     # Save next node, create a temp ariable and store the head.next
            curr.next = prev     # Reverse the link
            prev = curr          # Move prev to current
            curr = temp          # Move to next node
        
        return prev              # New head of reversed list

    #Time Complexity: O(n)
    #Space Complexity: O(1)    
        
"""
#By Recursion
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:            # Base case: if the list is empty, return None
            return None

        newHead = head          # Start by assuming the new head is the current node

        if head.next:           # If there is a next node, recursively reverse from that point
            newHead = self.reverseList(head.next) #Recursively call reverseList for rest of the list
            head.next.next = head   # When recursion unwinds, reverse the current node's pointer

        head.next = None         # Set the current node's next to None to avoid cycle

        return newHead           # Return the new head of the reversed list

#Time Complexity:O(n)
#Space Complexity: O(n)

"""