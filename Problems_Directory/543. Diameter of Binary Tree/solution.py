# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def findHeight(node):
            if not node:
                return -1
            left = findHeight(node.left)
            right = findHeight(node.right)
            
            # Update the diameter at this node
            self.res = max(self.res, left + right + 2)
            
            # Return height of the tree rooted at this node
            return max(left, right) + 1

        # Use of self.res: This eliminates the need for a list to hold the result, making the code cleaner.
        self.res = 0
        findHeight(root)
        return self.res
