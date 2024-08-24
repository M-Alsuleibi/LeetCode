# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        left    right
         2        2  
       3   4    4   3
     5   6        6   5 

        """
        # Tc = O(n), 
        # Sc = O(h), h:height of tree
        def dfs(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False    
            return  (
                left.val == right.val and 
                dfs(left.left, right.right) and
                dfs(left.right, right.left)
                    )

        return dfs(root.left, root.right)    
