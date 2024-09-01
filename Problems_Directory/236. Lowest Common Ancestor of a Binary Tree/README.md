# [236. Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/) `MEDIUM`
# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Traversing the tree in **Depth Fisrt Search** manner. If **p** and **q** found in separete sub-trees, then the _root_ is the **LCA**.
# Approach
<!-- Describe your approach to solving the problem. -->
This Problem is about 3 cases :
1. If p or q is root, return root
2. In left-subtree , if we find **p**  , go to right-subtree,
		-  if we find **q** then return _root_
		-  if we dont find q the return **p**
3. same as point 2 but change **p** to **q**  
# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
_$$O(n)$$_
- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
_$$O(1)$$_,
Unless counting the recursive calls in the stack memory _$$O(n)$$_ .
# Code
```python3 []
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
```
