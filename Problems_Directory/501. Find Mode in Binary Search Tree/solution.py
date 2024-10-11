# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        # T O(n), M O(n)
        modes = []
        map = defaultdict(int)
        maxCount = float('-inf')
       
        def dfs(node):
            if not node:
                return
       
            dfs(node.left)
            nonlocal maxCount, modes
            map[node.val] += 1
            if map[node.val] > maxCount:
                maxCount = map[node.val]
                modes = [node.val]
            elif map[node.val] == maxCount:
                modes.append(node.val)

            dfs(node.right)

        dfs(root)
        return(modes)
