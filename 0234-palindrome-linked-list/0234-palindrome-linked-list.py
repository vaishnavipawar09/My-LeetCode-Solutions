# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Step 1: Find the middle of the linked list (slow/fast pointers)
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Step 3: Compare first half and reversed second half
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True

    



"""
Approach
Find the Middle: Use slow and fast pointers to reach the midpoint.
Reverse the Second Half: Reverse the list from the middle to the end.
Compare Halves: Walk pointers from the start and from the new reversed second half, comparing values.
(Optional) Restore the List: If required, reverse again to restore the original list.

Edge Cases
Odd-length list: The middle element doesn’t matter for palindrome check.
Single node: Always a palindrome.
All nodes equal: Should return True.
List not palindrome: Any mismatch found returns False.

Time and Space Complexity
Time: O(n) — Each step (find middle, reverse, compare) is linear.
Space: O(1) — Only pointers used; no extra storage.

Dry Run
Example: [1, 2, 2, 1]
Step 1: slow at 2 (middle), fast at end
Step 2: Reverse from 2 onwards: [1] -> [2] (now the reversed second half is [1, 2])
Step 3: Compare: 1 == 1, 2 == 2 → Success
Result: True

Statement to Remember
"Find the middle, reverse the second half, then compare both halves in place."
"""