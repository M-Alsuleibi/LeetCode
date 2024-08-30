# Definition for a binary tree node.
from typing import List ,Optional #import it to resolve `NameError` when run removeDuplicates() in Driver code
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

# Helper function to print the binary tree in a structured way
def printTree(node: Optional[TreeNode], level=0, prefix="Root: "):
    if not node:
        print(" " * (level * 4) + prefix + "None")
        return
    print(" " * (level * 4) + prefix + str(node.val))
    if node.left or node.right:
        if node.left:
            printTree(node.left, level + 1, "L--- ")
        else:
            print(" " * ((level + 1) * 4) + "L--- None")
        if node.right:
            printTree(node.right, level + 1, "R--- ")
        else:
            print(" " * ((level + 1) * 4) + "R--- None")



class Solution:
    # Note: Only the code inside this class should be submitted to Leetcode.
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:       
        # base condition
        if(len(nums) == 1) : return TreeNode(nums[0])
        if(len(nums) == 0) : return None

        centerIndx = len(nums) // 2 #integer division
        root = TreeNode(nums[centerIndx])

        leftSubTree = nums[0 : centerIndx] # centerInxd is exluded
        root.left =  self.sortedArrayToBST(leftSubTree)

        rightSubTree = nums[centerIndx + 1 :]
        root.right = self.sortedArrayToBST(rightSubTree)

        return root

        # Driver code 
def main():
    nums = [-10,-3,0,5,9]
    solution=Solution()
    output=solution.sortedArrayToBST(nums)
    printTree(output)

if __name__ == "__main__":
    main()    
