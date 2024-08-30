# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
""" 
    Pseudocode   |
-----------------|
BFS Traversal -left to right-
    -------->
        1     -- L1 = 0            [1]
      2    3   -- L2 = 1           [2,3]            res = [1,3,6]    
    4    7   6  -- L3 = 2          [4,7,6]            queue = [4,7,6 ]
    
    1. BFS from right to left
    2. using queue DS , queue always holds elements in each level . 
    3.pop the first element and add to res.
    4. iterate until queue is empty  
        """
# Time complexity = O(n), Space Complexity = O(n)        
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:        
        if not root :
            return []

        res = []
        queue = collections.deque()    
        queue.append(root)

        while queue:
            # Track th last node in each level. after Inner loop finish(level pop up), we append to res
            last = None
            # Inner loop to track each level 
            for i in range(len(queue)):

                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                last = node    
            if last :
                res.append(last.val)

        return res    
