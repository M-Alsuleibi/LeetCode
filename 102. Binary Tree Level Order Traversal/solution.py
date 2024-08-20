# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Tc = O(n), Sc = O(n)
        res = []
        queue = deque()
        if root : 
            queue.append(root)
        else :
            return []
        while queue:
            # each level is a subarray in res
            level = []
            # inner loop for each level    
            for i in range(len(queue)):
                # popleft: delete from LEFT ,
                # pop(): delete an argument from the right end of the deque.

                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                level.append(curr.val)
                
            res.append(level)
            
        return res        
