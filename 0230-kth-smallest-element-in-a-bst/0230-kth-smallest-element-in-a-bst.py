# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []              #intialize a stack 
        curr = root             #set curr to root
        n= 0                    #intialized a counter
        while stack or curr:    #while the stack and curr nodes are not empty
            while curr:         #while curr is not empty 
                stack.append(curr)  #add the curr val to the satck
                curr = curr.left    #shift frm the root node to the left subtree
            curr = stack.pop()      #pop from the stack 
            n += 1                  #update the counter
            if n == k:              #if cnt is equal to the k value
                return curr.val     #we return the node, value, found it 
            curr = curr.right       #then we can start going to the right subtree


#Time Complexity: O(n), worst case , : O(h + k) in best case (balanced tree, early exit after k), O(n) in worst case (unbalanced, or k = n).
#Space Complexity: O(n), in worst case, unbalanced tree, O(h) for recursion stack (h = height of tree), O(1) extra (not storing all values).

"""
1. Clarifying Questions
Are all node values unique? Not necessarily, but it's a BST, so duplicates (if any) are on a specific side.
Is the input always a valid BST? Yes.
Is k always valid (1 ≤ k ≤ n)? Yes.
What should I return if the tree is empty? Constraints guarantee at least 1 node.
Is the BST static or will it be modified? The follow-up asks about frequent modifications, but the main problem is a one-off query.

2. Test Cases / Edge Cases
root = [1], k = 1 → 1
root = [2,1,3], k = 2 → 2
root = [5,3,6,2,4,null,null,1], k = 3 → 3
BST with only right children: [1, null, 2, null, 3], k = 3 → 3

3. Approach
Key insight:
Inorder traversal of BST gives values in sorted order (left, root, right).
Plan:
Traverse the tree inorder.
Collect nodes until we've reached the kth node.
Return the value of the kth node.

6. Dry Run Example
root = [3,1,4,null,2], k = 1
Inorder: 1 → 2 → 3 → 4
Visit 1 (k=1): k–1=0, res=1
"""