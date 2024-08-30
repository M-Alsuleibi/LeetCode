# [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/description/) `MEDIUM`

## Three approaches to solve the problem:
1. `Brute-force`: nested for loops , and collect currentSum for each subarray and compare it with maxSum , then return maxSum with a `Tc = O(n^2)`, `Sc = O(1)`
2.  `Optimized approach`:
- `Kadane's Algorithm` : `Tc = O(n)` , `Sc = O(1)`
_code_ : 
```python3
        maxSum = float('-inf')
        curSum = 0

        for num in nums:
            curSum = max(curSum,0) + num
            maxSum = max(maxSum, curSum)
            
        return maxSum    

```
 
- `Sliding Window Technique`: `Tc = O(n)` , `Sc = O(1)`
_code in `solution.py`_

