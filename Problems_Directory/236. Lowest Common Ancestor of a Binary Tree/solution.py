# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Tc = O(n) 
        # Sc = O(1), Unless counting the recursive stack frames
        if not root or root == p or root == q :
            return root 

        L = self.lowestCommonAncestor(root.left, p, q)    
        R = self.lowestCommonAncestor(root.right, p, q)    

        if L and R :
            return root
        else:
            return L or R     
