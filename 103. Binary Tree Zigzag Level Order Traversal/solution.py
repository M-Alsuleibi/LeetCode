# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # This proble is all about REVERSING the ODD level while traversing using BFS
        # Time complexity = O(n)
        # Memory complexity = O(n)

        res = []
        # These 4 lines equal line 19 :)
        # if not root:
        #     return []
        # if root : 
        #     queue.append(root)
        queue = deque([root] if root else [])
  
        while queue:
            level = []
            
            for i in range(len(queue)):
                node = queue.popleft()  
                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)  
                if node.right:
                    queue.append(node.right)  
            # can sustitute this line by lines 36-38        
            level = reversed(level) if len(res) % 2 else level        
            res.append(level)

      #  for i in range(len(res)):
      #      if i % 2 :
      #          res[i].reverse()    

        return res
