# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # DFS , T O(logn + logm), M O(logn)
        leftDepth = self.leftDepth(root)
        rightDepth = self.rightDepth(root)

        #If the tree is perfect binary tree
        if leftDepth == rightDepth:
            return (2 ** leftDepth) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)    


    def rightDepth(self, root):
        depth = 0
        while root:
            root = root.right
            depth += 1
        return depth 

    def leftDepth(self, root):
        depth = 0
        while root:
            root = root.left
            depth += 1
        return depth

