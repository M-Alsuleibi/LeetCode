# [2215. Find the Difference of Two Arrays](https://leetcode.com/problems/find-the-difference-of-two-arrays/description/?envType=study-plan-v2&envId=leetcode-75) `EASY`
# Approach
<!-- Describe your approach to solving the problem. -->
- Initialize the answer array `res` as a `list of lists` of size `2`.
-  Iterate over each array using two separete loops. In each loop check if the number is NOT found in the other array.And if the same number not found in the corresponding array in the `res` array. 
**NOTE** : Duplicates not allowed.
- Add the numbers that belongs to `nums1` and don't belongs to `nums2` into index `0` of the answer array.
 
- Add the numbers that belongs to `nums2`and don't belongs to `nums1`  into index `1` of the answer array. 

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
$$O(n)$$
- Space complexity:
<!-- Add$$O(n)$$ your space complexity here, e.g. $$O(n)$$ -->
$$O(n)$$
# Code
```python3 []
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res = [[], []] # initialize answer list of lists of size 2.
        for num in nums1:
            if num not in nums2 and num not in res[0]:
                res[0].append(num) 
        for num in nums2:
            if num not in nums1 and num not in res[1]:
                res[1].append(num)
        return res    
```

