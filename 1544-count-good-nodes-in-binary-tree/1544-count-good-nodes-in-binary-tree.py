# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q = collections.deque()
        q.append([root, root.val])
        good = 0
        maxsofor = 0
        while q:
            node, maxsofar= q.popleft()
            if node.val >= maxsofar:
                good += 1
            if node.left:
                q.append([node.left, max(node.left.val, maxsofar, node.val)])
            if node.right:
                q.append([node.right, max(node.right.val, maxsofar, node.val)])
        return good
        