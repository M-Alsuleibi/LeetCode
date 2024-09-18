# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Return the minimum value node of the BST.
    def minValueNode(self, root):
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # Remove a node and return the root of the BST.
        # T O(logN), M O(log N)
            if not root:
                return None

            if key > root.val:
                root.right = self.deleteNode(root.right, key)
            elif key < root.val:
                root.left = self.deleteNode(root.left, key)
            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                else:
                    minNode = self.minValueNode(root.right)
                    root.val = minNode.val
                    root.right = self.deleteNode(root.right, minNode.val)
            return root
