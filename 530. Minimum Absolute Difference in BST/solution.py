# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        arr=[]
        # We can do preOrder but have to handle negative diff in line #25 by using abs()
        def inorder(node):
            arr
            if not node:
                return

            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)
            

        inorder(root)
        diff = float('inf')
        for i in range(1,len(arr)):
            diff = min(diff, abs(arr[i] - arr[i-1]))

        return diff
