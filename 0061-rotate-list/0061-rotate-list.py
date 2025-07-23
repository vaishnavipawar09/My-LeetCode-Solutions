# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head     #if empty return head

        length, tail = 1, head      
        while tail.next:        # loop to cal length and get the tail node
            tail = tail.next
            length += 1
        
        k =k % length       #cal this so that k never crossess length 
        if k == 0:
            return head

        #find the break and then rotate it 
        curr = head #       find the new tail node
        for i in range(length - k - 1): 
            curr = curr.next   # curr = 3
        newHead = curr.next    # new head = 4     
        curr.next = None        # as 3 is the end now, set its ptr to null so list is 1 -> 2-> 3 and list2 : 4 _> 4
        tail.next = head        # list 2 tail pt 5 to head
        return newHead      # 4 -> 5 -> 1-> 2 -> 3



"""
 \U0001f50e Clarifying Questions (Ask Your Interviewer):
Is k always non-negative? (Yes, constraint says so.)
Can k be larger than the list’s length? (Yes. In this case, rotation should be mod length.)
Is the list singly or doubly linked? (Usually singly.)
Should we rotate in-place, or can we create a new list? (Usually in-place preferred.)
What to do if the list is empty or has one node? (Return as is.)
Can node values be negative/zero/duplicates? (Yes.)

\U0001f4dd Approach (How to Explain):
Step 1: Compute the length of the list.
Step 2: Make the list circular.
Step 3: Find the new tail and new head by moving (length - k % length - 1) and (length - k % length) steps from the current head.
Step 4: Break the circle.

Why this works:
Rotating right by k is the same as moving the last k nodes to the front. If k >= length, it’s equivalent to k % length rotations.

\U0001f50d Dry Run Example
Input: head = [1,2,3,4,5], k = 2
Step-by-step:
Length = 5.
Make circle: tail 5 → head 1.
k % length = 2. Steps to new tail: 5 - 2 - 1 = 2 (new tail is node 3, new head is node 4).
Break at node 3.
Result: [4,5,1,2,3]

\U0001f9e0 Edge Cases
Empty list (head = None): Return None.
Single node: Return head.
k = 0: Return head.
k is a multiple of length: List remains the same.

\U0001f4e2 How to Explain to Interviewer:
"I’ll first get the list’s length, connect the tail to head to form a circle, then find the new tail and new head using modular arithmetic. Finally, I’ll break the cycle to return the rotated list. This approach works in O(n) time and O(1) space, and handles all edge cases cleanly."
"""
        