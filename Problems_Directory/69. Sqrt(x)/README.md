# [69. Sqrt(x)](https://leetcode.com/problems/sqrtx/description/) `EASY`
# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
The problem asks for the square root of a number \( x \) rounded down to the nearest integer. A naive approach is to check every number starting from 0 to \( x \) and find the largest integer whose square is less than or equal to \( x \). However, this approach is inefficient, especially for large values of \( x \). Instead, we can use binary search to efficiently narrow down the range of possible square root values.

# Approach
<!-- Describe your approach to solving the problem. -->
1. **Edge Cases**: First, handle simple cases where \( x \) is 0 or 1. For these values, the square root is equal to \( x \) itself.

2. **Binary Search**:
   - Start with the range from 0 to \( x \) (inclusive).
   - Calculate the midpoint of the current range.
   - Check if the square of this midpoint is equal to \( x \). If it is, return the midpoint as the square root.
   - If the square of the midpoint is less than \( x \), move the search range to the right half (i.e., increase the lower bound). Store the current midpoint as it is the closest valid square root found so far.
   - If the square of the midpoint is greater than \( x \), move the search range to the left half (i.e., decrease the upper bound).
   - Continue the process until the search space is exhausted.
   - Return the stored value as the result, which represents the largest integer whose square is less than or equal to \( x \).

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
  - The time complexity is \( O(\log x) \) because binary search repeatedly halves the search space.

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
  - The space complexity is \( O(1) \) because the algorithm uses a constant amount of extra space.

# Code _Brute Force_
```python3 []
class Solution:
    def mySqrt(self, x: int) -> int:
        # Brute Force: Tc = O(sqrt(x)), Sc = O(1)

        # Start checking from 0
        for i in range(x + 1):
            # If i squared is greater than x, return the previous i
            if i * i > x:
                return i - 1
        # If no number squared is greater, return x (which is 0 or 1)
        return x      
```
# Code _Optimized_
```python3 []
class Solution:
    def mySqrt(self, x: int) -> int:
        # Optimized: Binary Search. 
        # Since the search space is from 0 to i, take mid point M: if M^2 > x then reduce the search space to i to M .Iterrate
        # Tc = O(logn), Sc = O(1)
        L, R = 0, x 
        res = 0

        while L <= R:
            M = L + (R-L) // 2
            
            if (M * M) > x:
                R = M - 1
            elif (M * M) < x:
                L = M + 1
                res = M
            # not always execute    
            else:
                return M
 
        return res        
```
