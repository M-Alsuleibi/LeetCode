# [143. Reorder List](https://leetcode.com/problems/reorder-list/description/) `EASY`
## This problem follows three stages: 
1. Slow and fast pointers approach to reach the middle of the linked list
2. Breaking the original list into two halves(equal halves if number of nodes in the original list are EVEN and viseverca).Then reverse the second half.
3. Merging the two halves and use thse second half in the loop condition(`slow2` in my solution), because it maybe shorter than the first half(in the case that nuber of nodes in the original list is ODD) 
