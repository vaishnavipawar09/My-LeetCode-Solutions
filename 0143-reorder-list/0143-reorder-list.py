# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head                     #create two ptrs, one fast and other second
        while fast and fast.next:                   #run till you get one empty
            slow = slow.next                        #move by 1 step
            fast = fast.next.next                   #move by 2 step

        #find the mid value, and divide the list(find second half of list) and reverse it
        second = slow.next                      #begin the second half of the list
        slow.next = None                        #split the second list
        prev = None                             #set pre to null
        while second:                           #Reverse the second half of the list
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        #merge the two lists
        first, second = head, prev              #where the first and second half starts
        while second:                           #keep going until one ptr is null
            tmp1, tmp2 = first.next, second.next    #store next nodes in the temp node
            first.next = second                 #reassign that is insert in between the nodes
            second.next = tmp1
            first, second = tmp1, tmp2          #shift our ptrs, of the both the list

#Time Complexity: O(n)
#Space Complexity: O(1)