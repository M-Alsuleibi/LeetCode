# [162. Find Peak Element](https://leetcode.com/problems/find-peak-element/description/?envType=study-plan-v2&envId=leetcode-75) `MEDIUM`
![Screenshot from 2024-11-15 00-41-32.png](https://assets.leetcode.com/users/images/82f9debc-3bb7-4dd5-a06b-9778493cba83_1731624108.631068.png)

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
**A peak** is defined as an element that is not smaller than its neighbors.
We can apply a _binary search_, reducing the problem size by half at each step.

# Approach
<!-- Describe your approach to solving the problem. -->
Perform a binary search.
# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
$$O(logn)$$
- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
$$O(1)$$
# Code
```python3 []
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # T O(logn), M O(1)
        L, R = 0, len(nums) - 1

        while L < R :
            mid = (L + R) // 2
            if nums[mid] < nums[mid + 1]:
                L = mid + 1
            else:
                R = mid   

        return L # same as: return R       
```
