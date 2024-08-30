# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Keeping the scope of values array global
        values = [] 

        # Iterative approach:
        stack = []
        curr = root
        # if there is a node or stack not empty 
        while curr or stack:
            while curr:
                # first add to stack then go left as far as possible
                stack.append(curr)
                curr = curr.left
            # reaching the far left of a tree
            # First is pop from stack THEN go right
            curr = stack.pop()
            values.append(curr.val)
            curr = curr.right
        return values

        # Recursive Approach:
        def inorder(root):
            if not root :
                return []
            inorder(root.left)
            values.append(root.val)
            inorder(root.right)

        inorder(root)
        return values
