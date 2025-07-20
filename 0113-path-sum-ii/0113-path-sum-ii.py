# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def dfs(node, path, curr_sum):
            if not node:
                return
            
            path.append(node.val)    # Add current node to the path
            curr_sum += node.val
       
            # If it's a leaf and the sum matches, add a copy of the path
            if not node.left and not node.right and curr_sum == targetSum:
                res.append(list(path))
            else:
                dfs(node.left, path, curr_sum)
                dfs(node.right, path, curr_sum)

            # Backtrack: remove current node before going up
            path.pop()

        dfs(root, [], 0)
        return res


#DFS/backtrack from root to leaf, building up path and sum; on leaf, if sum matches, save the path.” 

#Dry Run:
#targetSum = 22
#How the paths are built: Path: 5 → 4 → 11 → 7 (sum = 27)
#Path: 5 → 4 → 11 → 2 (sum = 22) ✅
#Path: 5 → 8 → 13 (stops: not leaf, incomplete path)
#Path: 5 → 8 → 4 → 5 (sum = 22) ✅
#Path: 5 → 8 → 4 → 1 (sum = 18)
#So, output: [[5,4,11,2], [5,8,4,5]]

#Time: O(N)
#We visit every node once (worst-case, all nodes on all root-to-leaf paths are checked).
#Space: O(H) for recursion stack (H = height), plus O(K*L) for output
#K = number of valid paths
#L = average length of each path (up to H).

#Clarifying questions:
# Valid binary tree
#Do we care about all paths or just root-to-leaf? (Only root-to-leaf)
#Are negative numbers possible in node values or targetSum? (Yes, as per constraints)
#Should we return False if the tree is empty? (Yes)
#Are duplicate values allowed in the tree? (Yes)
#Can there be multiple valid paths from the root? Yes
#Can i assume a Treenode, or should i code it down too? 

# root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22 [[5,4,11,2],[5,8,4,5]]

#Approcach:
#This is a classic backtracking/DFS problem.
#At each node: Add current node’s value to the current path.
#Subtract node’s value from the remaining target sum.
#If you’re at a leaf and the sum matches, append the path to the result.
#Otherwise, recurse left/right.
#After recursion, backtrack (remove last node).
#Edge cases: Empty tree returns [].

