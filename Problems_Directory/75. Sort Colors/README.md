# [75. Sort Colors](https://leetcode.com/problems/sort-colors/description/) `MEDIUM`
# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
- Since sorting the array is going to solve the problem in _O(nlogn)_ time complexity BUT its a constrain that we can not use it. We need Implement our own sorting algorithm, and choose one that takes less than _O(nlogn)_.
- Since the problem statemnet states that all values in the array in in range [0 - 2]. So we can use _Bucket Sort_ to achive our goal in sorting this array.
# Approach
<!-- Describe your approach to solving the problem. -->
- Create buckets for each three values(0,1,2) of the input array. Then apply the _Bucket Sort_ algorithm.
- _Bucket Sort_ is an **in-place**, **non-stable** algorithm.  
# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
_O(n)_
- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
_O(n)_
# Code
```python3 []
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Brute Force -> Tc : O(nlogn)
        # Optimized:  Bucket Sort -> Tc : O(n), Sc : O(n)
        # array/bucket for count each value (0,1,2)
        count = [0, 0, 0]
        # Phase 1 : build the buckets
        for num in nums:
            count[num] += 1
        
        #Phase 2: rewrite the original array nums
        i = 0
        for k in range(len(count)):
            for _ in range(count[k]):
                nums[i] = k
                i += 1

        print(nums)        
           
```
