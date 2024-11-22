# [485. Max Consecutive Ones](https://leetcode.com/problems/max-consecutive-ones/description/) `EASY`
# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Find the length of a window of ones`1`, compare each window length and retrun the maximum.
# Approach
<!-- Describe your approach to solving the problem. -->
- Using `sliding window with variable size`, each window expand and shrinks accourding to the number of consecutive ones`1s`.
- Check the inline comments :) 
# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
$$O(n)$$
- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
$$O(1)$$
# Code
```python3 []
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Result length 
        length = float('-inf')
        # Current window length
        windowLength = 0
        L = 0

        for R in range(len(nums)):
            if nums[R] != 1:
                L = R + 1
                windowLength = 0 # If find 0, then reset the window 
            if nums[R] == 1:
                windowLength += 1
                L += 1
            length = max(windowLength, length) 
        return length           
```

