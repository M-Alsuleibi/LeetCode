# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:

        # Time complexity = O(1), Space Complexity = O(1)
        return True if root.left.val + root.right.val == root.val else False
