from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
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
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        # Convert linked list to array
        nums = []
        curr = head
        while curr:
            nums.append(curr.val)
            curr = curr.next
        # Use helper function to convert sorted array to BST
        return self.sortedArrayToBST(nums)

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # base condition
        if not nums:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])

        centerIndx = len(nums) // 2  # integer division
        root = TreeNode(nums[centerIndx])

        leftSubTree = nums[0:centerIndx]  # centerIndx is excluded
        root.left = self.sortedArrayToBST(leftSubTree)

        rightSubTree = nums[centerIndx + 1:]
        root.right = self.sortedArrayToBST(rightSubTree)

        return root

# Helper function to create a linked list from a list
def createLinkedList(nums: List[int]) -> Optional[ListNode]:
    if not nums:
        return None
    head = ListNode(nums[0])
    current = head
    for num in nums[1:]:
        current.next = ListNode(num)
        current = current.next
    return head

# Driver code
def main():
    nums = [-10, -3, 0, 5, 9]
    head = createLinkedList(nums)
    solution = Solution()
    output = solution.sortedListToBST(head)
    printTree(output)

if __name__ == "__main__":
    main()
