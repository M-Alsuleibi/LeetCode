# [1456. Maximum Number of Vowels in a Substring of Given Length](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/?envType=study-plan-v2&envId=leetcode-75) `MEDIUM`
# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Using `fixed size sliding window` to check against list of vowels.
# Approach
<!-- Describe your approach to solving the problem. -->
Check the inline comments :) 
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
    def maxVowels(self, s: str, k: int) -> int:
        # Time : O(n), Memory: O(1)
        v = ('a', 'e', 'i', 'o', 'u')
        L = 0
        curCount = 0
        maxCount = 0
        for R in range(len(s)) :
            # Check if the window size exceeds `k`
            if R - L + 1 > k:
            # Remove the leftmost character from the current window
                if s[L] in v:
                    curCount -= 1
                L += 1  # Shrink the window from the left
            # Add the right character to the current window
            if s[R] in v :
                curCount += 1

            # Update the maximum vowel count
            maxCount = max(maxCount, curCount)        

        return maxCount

```
