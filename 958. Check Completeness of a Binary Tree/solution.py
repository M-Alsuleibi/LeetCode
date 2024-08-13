# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        # Tc = O(n) , Sc = O(n)
        level ,col = 0 , 0
        q = deque([[root, level , col]])
        if root :
            pos = 1
            while q : 
                node , level , col  = q.popleft()
                # print(g)
                # node, level, col= g
                mark = 2 ** level + col
                if pos != mark :
                    return False
                if node.left:
                    q.append([node.left, level + 1, col * 2])
                if node.right:
                    q.append([node.right, level + 1, col * 2 + 1])
                pos += 1
            return True     
