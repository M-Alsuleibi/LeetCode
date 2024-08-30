# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # Tc = O(n) , Sc= O(n)
        if not root : 
            return 0
        sumOfLeaves = 0
        # Check if the left child exists (if root.left)
        #  and it's a leaf node (not root.left.left and not root.left.right)
        if  root.left and not root.left.left and not root.left.right :
            sumOfLeaves += root.left.val

        sumOfLeaves += self.sumOfLeftLeaves(root.left)
        sumOfLeaves += self.sumOfLeftLeaves(root.right)

        return sumOfLeaves

