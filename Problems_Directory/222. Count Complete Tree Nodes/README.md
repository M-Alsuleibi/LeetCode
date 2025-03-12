![Screenshot from 2025-03-13 00-43-06.png](https://assets.leetcode.com/users/images/11e9fe68-1ebc-4410-9388-9e03ef864cc5_1741819412.5918267.png)

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
- Brute Force: Do a **BFS** traversal, collecting the nodes inside auxialary list and return the length -> Time O(n), Space O(n)

# Approach
<!-- Describe your approach to solving the problem. -->
- Optimized: DFS by Utilizing the concept of **Perfect Binary Tree**, which the **#nodes = 2<sup>depth</sup> - 1**.
# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
$$O(logm + logn)$$
- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
$$O(logm + logn)$$
# Code
```python3 []
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # DFS , T O(logn + logm), M O(logn)
        leftDepth = self.leftDepth(root)
        rightDepth = self.rightDepth(root)

        #If the tree is perfect binary tree
        if leftDepth == rightDepth:
            return (2 ** leftDepth) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)    


    def rightDepth(self, root):
        depth = 0
        while root:
            root = root.right
            depth += 1
        return depth 

    def leftDepth(self, root):
        depth = 0
        while root:
            root = root.left
            depth += 1
        return depth
```
