#[977. Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/description/) `EASY`
# Approach:
- Since sorting is not allowed. We compare each absolute element in the input array via Two Pointers.
If the element in Left is greater than the elemnt in Right, Then suqare it an push it to Axullary array.
- Iterate for the Right element.
- Finally Reverse the Auxillary array. 
