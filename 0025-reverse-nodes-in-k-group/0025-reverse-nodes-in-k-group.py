# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)   #create a dummy node
        grpprev = dummy             #track the end of the previous reversed group
        
        while True:
            kth = self.getK(grpprev, k) #find the kth node from grpprev
            if not kth:                 #if fewer than k nodes remaining break
                break
            grpnext = kth.next          #start of the next gr after the reversal
              
            #Reverse the k nodes
            prev = kth.next          #assign the prev ptr after the kth node
            curr = grpprev.next      #curr node starts at the first node in the grp
            while curr != grpnext:   #if curr is not equal to the start of the node
                temp = curr.next     # Save next node, create a temp variable and store the head.next
                curr.next = prev     # Reverse the link
                prev = curr          # Move prev to current, move it forward
                curr = temp          # Move to next node, move it forward
            

            temp = grpprev.next      # store old start, it will become tail after reverse
            grpprev.next = kth       # point previous group to new head
            grpprev = temp           # move grpprev to the new tail for the next group

        return dummy.next            #do not return the dummy node, but the next node from it i.e. new head

    def getK(self, curr, k):
        while curr and  k > 0:       # Move forward k steps or return None if not enough nodes
            curr = curr.next
            k -= 1
        return curr

        #Time Complexity: O(n)
        #Space Complexity: O(1)