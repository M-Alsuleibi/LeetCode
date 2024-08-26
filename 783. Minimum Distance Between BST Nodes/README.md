# [783. Minimum Distance Between BST Nodes](https://leetcode.com/problems/minimum-distance-between-bst-nodes/description/) `EASY`
# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Traverse all nodes in the tree and compare the difference between each two nodes values. At the end return the minimum diiference.
# Approach
<!-- Describe your approach to solving the problem. -->
- Since its a BST, we can create a sorted array using _DFS_ _Inorder_ traversal.
- Iterate and collect the minimum difference.
# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
_O(n)_
- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
_O(n)_
# Code
```python3 []
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

