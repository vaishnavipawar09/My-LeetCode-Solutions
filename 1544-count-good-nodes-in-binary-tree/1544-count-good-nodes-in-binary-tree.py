# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q= collections.deque()
        q.append([root, root.val])
        maxval= 0
        good = 0
        while q:
            node, maxval = q.popleft()
            if node.val >= maxval:
                good += 1
            if node.left:
                q.append([node.left, max(maxval, node.val)])

            if node.right:
                q.append([node.right, max(maxval, node.val)])

        return good

