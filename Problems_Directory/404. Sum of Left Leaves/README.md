# [404. Sum of Left Leaves](https://leetcode.com/problems/sum-of-left-leaves/description/) `EASY`
## Approach:
- Check if the left child exists:  `if root.left`
- and it's a leaf node: `not root.left.left and not root.left.right`
