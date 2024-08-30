# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        """
        inorder -> [1,2,3,4,6]
        diff -> min(diff, r-l)
        """
        arr = []

        def inorder(node):
            if not node:
                return
            if node:
                inorder(node.left)
                arr.append(node.val)
                inorder(node.right)
        inorder(root)
        diff = float('inf')
        for i in range(1,len(arr)):
            diff = min(diff,arr[i] - arr[i-1] )               
        return diff    
