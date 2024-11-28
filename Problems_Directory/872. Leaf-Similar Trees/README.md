# [872. Leaf-Similar Trees](https://leetcode.com/problems/leaf-similar-trees/description/?envType=study-plan-v2&envId=leetcode-75) `EASY`
![Screenshot from 2024-11-29 00-06-50.png](https://assets.leetcode.com/users/images/118fd49e-7d60-4cba-a26a-b081babdee75_1732831637.8086562.png)

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Collect `leaf` nodes for each tree in a separete `array`. Then compare the two arrays if they equal or not.
# Approach
<!-- Describe your approach to solving the problem. -->
- Declare two arrays `tree1`, `tree2` to collect nodes values for each corresponding tree.We declare them outside the helper function `dfs()` so we can pass them as refernces later.
- Implement the DFS logic inside the helper function `dfs()`. This function has two parameters:
  - root of the tree `node` and 
  - the related array that will collects the nodes values `arr`. 

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
$$O(n)$$
- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
$$O(n)$$
# Code
```python3 []
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

```
