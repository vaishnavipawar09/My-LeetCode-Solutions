# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy =  ListNode()                 #Create a dummy list
        carry = 0                           #Intialize the carry to 0

        curr = dummy                        #Start the curr with the dummy node
        while l1 or l2 or carry:            #loop through l1 or l2, or carry until it exists
            val1 = l1.val if l1 else 0      #Get value from l1 and l2 until they exist, else use 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry     #cal the total of the number
            digit = total % 10              #cal the digit of the number and store it 
            carry = total // 10             #check and cal the carry ie. update the carry 

            curr.next = ListNode(digit)     #create a new node to add to the result list for digit 
           
            curr = curr.next                #move all the pointers forward 
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummy.next                   #return the line starting at dummy.next

#Time Complexity : O(n + m) n = l1, m = l2
#Space Complexity : O(1) extra space
                # or O(max(n, m)) for output list
