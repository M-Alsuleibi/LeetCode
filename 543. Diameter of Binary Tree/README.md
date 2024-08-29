# [543. Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/description/) `EASY`

# Approach
<!-- Describe your approach to solving the problem. -->
1. The height of a binary tree is the maximum of the heights of the left and right subtrees plus 1.
2. The diameter of a binary tree is the sum of the heights of the left and right subtrees plus 2.
3. The height of an empty tree (NULL node) is -1.
4. The height of a single-node tree is 0.
        
This approach calculates the height while updating the diameter during the tree traversal.       
# Complexity
- Time complexity:$$O(n)$$

<!-- Add your time complexity here, e.g. $$O(n)$$ -->
 - We traverse each node exactly once, performing constant-time operations at each node.
- Therefore, the time complexity is O(n), where n is the number of nodes in the tree.
- --
- Space complexity:$$O(n)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
- The space complexity is dominated by the recursive call stack, which can go as deep as the height of the tree.
- In the worst case (unbalanced tree), the height can be O(n), making the space complexity O(n).
- For a balanced tree, the height and thus space complexity would be $$O(log n)$$.
# Code
```python3 []
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

        
```
