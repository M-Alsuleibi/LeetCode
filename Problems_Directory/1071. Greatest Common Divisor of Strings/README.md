# [1071. Greatest Common Divisor of Strings](https://leetcode.com/problems/greatest-common-divisor-of-strings/description/?envType=study-plan-v2&envId=leetcode-75) `MEDIUM`
![image.png](https://assets.leetcode.com/users/images/8b495c24-7ccf-4005-897c-bf1b5ec405af_1731939360.6320302.png)

# Approach
<!-- Describe your approach to solving the problem. -->
- For two strings `str1` and `str2` to have a GCD:
Concatenating them in either order `(str1 + str2 or str2 + str1)` must yield the same result. This ensures that the strings are built using the same repeating pattern.
- Calculate GCD of Lengths:

  Use the `math.gcd` function to calculate the GCD of the lengths of str1 and str2. Let this value be `k`.
- Extract GCD Substring:

  If the condition `str1 + str2 == str2 + str1` is true, extract the substring `str1[0:k]`. This substring represents the GCD string pattern shared by both str1 and str2.


If the condition is false, return an empty string `""`, indicating that no GCD exists.
# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
$$O(n + m)$$
- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
$$O(n + m)$$
# Code
```python3 []
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        return str1[0: math.gcd(len(str1), len(str2))] if str1 + str2 == str2 + str1 else ""  


```
