# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []                    #Empty string

        def dfs(node):              #Helper function
            if not node:            #if node is null
                res.append("N")     #Append a N char 
                return
            res.append(str(node.val)) #Append the vale to the res
            dfs(node.left)              #traverse on left subtree
            dfs(node.right)             #traverse on right subtree

        dfs(root)                       #pass the root val
        return ",".join(res)            #Join by the , delimeter
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(",")          #split by the , (comma) delimeter
        self.i = 0                      #a ptr global

        def dfs():                      #helper funt for recursion 
            if vals[self.i] == "N":     #if N return the Null node
                self.i += 1             #icrement i so next val will be there
                return None
            node = TreeNode(int(vals[self.i]))  #conert to int and then pass the value
            self.i += 1                 #increment i to move to next
            node.left = dfs()           #left subtree
            node.right = dfs()          #right subtree

            return node                 #return the root node of the tree

        return dfs()                    #call dfs and return the tree
        
#Serialize: O(n), each node visited once.
#Deserialize: O(n), each token processed once.
#Space: O(n), result string and recursion stack.

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


#Clarifying Questions:
#Are node values unique or can they repeat?  They can repeat—need to preserve tree structure, not just values!
#Is it a regular binary tree (not necessarily a BST)? Yes.
#Do I need to handle empty trees? Yes, root = [] should be supported.
#Can I use any traversal for serialization? Yes! Preorder (with null markers) is common.

"""
pproach (Preorder with Nulls – Most Common and LeetCode-Friendly)
Serialize: Use preorder traversal. For every node:
Record the value as a string.
For null nodes, record a special marker (e.g., "N").
Join all values with commas (or another delimiter).
Deserialize: Read the list in order, recursively reconstruct the tree:
If value is "N", return None.
Otherwise, create a node with that value and recurse for left/right.

DRY Run:
Serialized: "1,2,N,N,3,4,N,N,5,N,N"
1 (root)
2 (left)
N (left null)
N (right null)
3 (right)
4 (left)
N (left null)
N (right null)
5 (right)
N (left null)
N (right null)

Deserialized: Rebuilds the exact same tree in preorder!

“I serialize the tree in preorder, using a special symbol for null children. This way, when I deserialize, I reconstruct the tree recursively in the same order, always knowing when to place None vs. an actual node. This works for all binary trees, even with duplicates or negative values.”
"""