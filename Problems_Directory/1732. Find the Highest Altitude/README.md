![Screenshot from 2024-11-01 05-29-02.png](https://assets.leetcode.com/users/images/7c9f2a41-b79f-4b21-aafc-928f3e07ea24_1730431947.383335.png)

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Construct an altitudes array and retrun the hieghest value from it.  
# Approach
<!-- Describe your approach to solving the problem. -->
- The first value of the altitude array is always **zero**
- The altitudes array is a `prefixSum` data structure.
- Return max from prefixSum. 
# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
$$O(1)$$
- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
$$O(n)$$
# Code
```python3 []
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefixSum = [0]
        total = 0

        for g in gain:
            total += g
            prefixSum.append(total)
        return max(prefixSum)    
```
