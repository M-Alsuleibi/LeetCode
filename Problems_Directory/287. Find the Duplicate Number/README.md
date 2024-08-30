# [287. Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/description/) `MEDIUM`
## Intuition

The problem involves finding a duplicate value in an array where each value is guaranteed to repeat. A common approach is to use a hash map to keep track of the occurrences or frequencies of values, and return the value that repeats. However, this approach results in a space complexity of O(n), which the problem constraints prohibit.

Another approach is to sort the input array and then iterate over it, returning the first value that occurs twice. But this method modifies the input array, which is also not allowed by the problem.

## Approach

This is not an intuitive problem, unfortunately. It can be broken down into two key aspects:

1. The **Linked List Cycle** problem.
2. **Floyd's Algorithm**, which is used to detect the beginning of a cycle in a linked list.

The core of the problem lies in understanding that the values within the input array are bounded within the range [1, n]. This range also applies to the indices of the array, creating a block of length `n` that is guaranteed to contain a cycle. The trick is to follow the inline comments in the code with an example input `[1, 3, 4, 2, 2]` and understand the node representation (where each node represents an index, not the value inside the array).
![alt text](<Screenshot from 2024-08-10 17-50-58.png>)

## Complexity

### Time Complexity (Tc):

- **Brute Force Approach**: Using a hash table or sorting the array results in Tc = O(n) and Sc = O(n), which is not allowed by the problem constraints.
- **Optimized Solution**: Using Floyd's Algorithm with slow/fast pointers results in Tc = O(n) and Sc = O(1).

### Space Complexity (Sc):

- **Brute Force Approach**: Using a hash table or sorting the array results in Sc = O(n).
- **Optimized Solution**: Using Floyd's Algorithm with slow/fast pointers results in Sc = O(1).

## Code

```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0  # pointers represent indices, not array values

        # Phase 1: Find intersection
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Phase 2: Find entrance
        slow2 = 0  # start at the beginning of the array until it intersects with slow
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                break
        return slow
```
