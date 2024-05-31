# [109. Convert Sorted List to Binary Search Tree](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/?envType=problem-list-v2&envId=p29oug1s)`MEDIUM`

## Note for Leetcode Submission
**Important:** Only the code inside the `Solution` class should be submitted to Leetcode.

## NOTES:
- I started with the easier version of this problem [problem #108](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/)
- Explanation:
    - Creating a Linked List:The createLinkedList function converts a Python list to a linked list of ListNode objects.**THIS IS FOR TESTING PURPOSES ONLY**
    - Conversion Function: The sortedListToBST method converts the linked list to an array (nums) and then calls sortedArrayToBST to create the BST.
    - BST from Sorted Array: The sortedArrayToBST method recursively creates a balanced BST from the sorted array.
    - Printing the Tree: The printTree function prints the tree structure in a readable format.
    - Driver Code:In main, the input list is converted to a linked list, the sortedListToBST method is called to convert it to a BST, and the resulting BST is printed using printTree.