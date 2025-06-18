# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode()
        tail = temp
        l1, l2 = list1, list2

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1      # attach l1’s node to tail
                l1 = l1.next        # move l1 forward
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next        # move tail forward

        tail.next = l1 if l1 else l2
        
        return temp.next



    
        