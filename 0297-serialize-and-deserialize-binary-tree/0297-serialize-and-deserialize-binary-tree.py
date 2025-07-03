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
        
#Time Complexity: O(n)
#Space Complexity: O(n)
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))