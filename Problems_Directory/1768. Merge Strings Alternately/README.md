# [1768. Merge Strings Alternately](https://leetcode.com/problems/merge-strings-alternately/description/?envType=study-plan-v2&envId=leetcode-75) `EASY`
# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Take one character from `word1`, then one from `word2`, and so on, until the shorter string runs out. After that, you append the remaining characters from the longer string.


# Approach
<!-- Describe your approach to solving the problem. -->
1. Initialize Pointers: Initialize two pointers `l` and `r`, both starting at `0`. 

2. Alternate Merging: In the while loop, keep appending one character from `word1` (using `l`) and one from `word2` (using `r`) to the result string `s`, as long as both pointers are **within the bounds**.

3. Handle Remaining Characters: Once one of the strings is fully traversed, append the remaining characters of the longer string to the result s. This is handled by the `elif` statements.

4. Stop the Loop: When both `word1` and `word2` are completely traversed, the loop breaks, return `s`.


# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
$$O(n)$$
- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
$$O(n)$$
# Code
```python3 []
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        abc
         l
            -> adbecfr
        defr
         r
        """
        s = ""
        l, r = 0, 0
        while True:
            if l < len(word1) and r < len(word2):
                s += word1[l] + word2[r]
                l += 1
                r += 1
            elif len(word1) > len(word2) and l < len(word1):
                s += word1[l]
                l += 1
            elif len(word1) < len(word2) and r < len(word2):
                s += word2[r]
                r += 1
            else:

                break    
        return s      
```
