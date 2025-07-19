# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(left, right):
            if left > right:
                return None

            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root
        return helper(0, len(nums) - 1)

#Dry Run:
##nums = [-10, -3, 0, 5, 9] _> [0, -3, 9, -10, null, 5]
# l = 0, r = 4, mid = 4/2 = 2 root =0 
#Nuild left [-10, -3] l = 0, r = 1,  mid = 0, node -10  (left child), right: -3 (right child of -10)
#Build right: [5,9], mid=3, node=5 (right child), right: 9 (right child of 5)
# [0, -10, 5, null, -3, null, 9]

#ime: O(n) — Each element is processed once.
#Space: O(log n) for recursion stack (height of the balanced tree).
        

#Are all numbers unique? Yes, since the array is strictly increasing.
#Should the tree be as balanced as possible (minimizing the height)?Yes.
#Can the output be any one valid height-balanced BST?  yes
# Is the input always sorted ascending and non-empty? Yes, by constraints.
# Do I need to implement the TreeNode class, or is it given?

#nums = [1] -> [1]
#nums = [-10, -3, 0, 5, 9] _> [0, -3, 9, -10, null, 5]
#nums = [1, 3] -> [1, 3] or [3, 1]

#Approach,
#Recursively, for any subarray [left, right],
#Choose middle as root.
#Left subtree: nums[left:mid-1]
#Right subtree: nums[mid+1:right]

#“Always pick the middle of the sorted array as the root, recursively, to keep the BST as balanced as possible.”