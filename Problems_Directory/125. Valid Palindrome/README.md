# [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/description/) `EASY`

## Solution Approach:
### Explanation of the steps:

1. **str.isalnum()**: Used within the `filter` function to remove non-alphanumeric characters.
2. **filter(fn, iterable)**: Filters the input string `s` to retain only alphanumeric characters.
3. **str.lower()**: Converts the filtered string to lowercase.
4. **delimiter.join(iterable)**: Joins the filtered characters into a single string.

The `while` loop with left and right pointers (`l` and `r`) checks if the string is a palindrome by comparing characters from both ends moving towards the center. If all characters match, it returns `True`, otherwise `False`.

