# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        grpprev = dummy
        
        while True:
            kth = self.getK(grpprev, k)
            if not kth:
                break
            grpnext = kth.next
              
            prev = kth.next
            curr = grpprev.next
            while curr != grpnext:
                temp = curr.next 
                curr.next = prev
                prev = curr
                curr = temp

            temp = grpprev.next         # store old start — it will become tail after reverse
            grpprev.next = kth          # point previous group to new head
            grpprev = temp              # move grpprev to the new tail for the next group

        return dummy.next 

    def getK(self, curr, k):
        while curr and  k > 0:
            curr = curr.next
            k -= 1
        return curr