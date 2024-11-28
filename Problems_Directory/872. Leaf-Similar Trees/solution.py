# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # Time O(n), Memory O(n)
        tree1 = []
        tree2 = []

        def dfs(node, arr):
            if node:
                if not node.left and not node.right:
                    arr.append(node.val)
                dfs(node.left, arr)
                dfs(node.right, arr)

        dfs(root1, tree1)    
        dfs(root2, tree2) 
        return tree1 == tree2   
