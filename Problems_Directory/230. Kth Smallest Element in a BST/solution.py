# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # BST can generate sorted array by inorder DFS
        #Tc = O(n) 
        #Sc = O(n)
        arr = []

        def inorder(node):
            if not root : 
                return None
            if node:
                inorder(node.left)
                arr.append(node.val)
                inorder(node.right)      

        inorder(root)    
        return arr[k - 1]
