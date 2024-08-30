# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:



        # DFS; Recursive Approach: Tc = O(n) ,
        #  Sc = O(n), When reach leaf node in left sub-tree, stack call pop the last call,
        # and push a new call for right sub-tree if exists. So at most the call stack will have n length 
     
        treeVals = []
        
        def postOrder(node : TreeNode | None) -> None:

            if not node :
                return  []   

            postOrder(node.left)
            postOrder(node.right)
            treeVals.append(node.val)    

        postOrder(root)

        return treeVals

        # Iterative approach:
            # Base case...
        if not root: return []
        # Create an array list to store the solution result...
        sol = []
        # Create an empty stack and push the root node...
        bag = [root]
        # Loop till stack is empty...
        while bag:
            # Pop a node from the stack...
            node = bag.pop()
            sol.append(node.val)
            # Push the left child of the popped node into the stack...
            if node.left:
                bag.append(node.left)
            # Append the right child of the popped node into the stack...
            if node.right:
                bag.append(node.right)
        # Return the REVERSED solution list...
        return sol[::-1]       
