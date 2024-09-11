# [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/description/) `MEDIUM`
# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Since input array is circularly sorted, we can benifit from  a variation of a **Binary Search** to find the target rather than using **Linear Search** through the array.
# Approach
<!-- Describe your approach to solving the problem. -->
Input array is circularly sorted with **NO Duplicates**. We can benifit from sorting segments in the array which are those segments that don't have the _Break Point_.
- _Break Point_ is the point that contains th minimum element in sorted sequence.
For example: In [12, 14, **18**, **3**, 6, 8, 9] array , **[18,3]** is the _Break Point_. And any segment/subarray doesn't contain it will be sorted : **[12, 14]** and  **[6, 8, 9]**.
- Understanding the _Break/Boundary Point_ lead us to three cases to cover to find the target in cicularly sorted array after Initialize _Low/High_ indices and declare _mid_ index in each iteration until Low exceeds High:
1. Case 1: mid elemnt equal to target -> return mid index.
2. Case 2: mid elemnt <= High elemnt -> This means the right half is sorted.
3. Case 3: mid elemnt >= Low elemnt -> This means the left half is sorted.
# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
$$O(logn)$$
- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
$$O(1)$$
# Code
```python3 []
class Solution:
   def search(self, nums: List[int], target: int) -> int:
       # Brute Forcce: Tc O(n), Sc O(1)
       #for i in range(len(nums)):
       #    if nums[i] == target :
       #        return i   
       #return -1   
       #-----------------------------------------------------


       #Optimized: Binary Search for circularly sorted array
       # Tc = O(logn) , Sc = O(1)
       L, R = 0, len(nums) - 1
       while L <= R:
           mid = (L+R) // 2
           #case 1
           if nums[mid] == target:
               return mid
           #case 2   
           if nums[mid] <= nums[R]:
               if target >= nums[mid] and target <= nums[R]:
                   L = mid + 1
               else:
                   R = mid - 1
           #case 3
           if nums[mid] >= nums[L]:
               if target <= nums[mid] and target >= nums[L]:
                   R = mid - 1
               else:
                   L = mid + 1
       return -1                
```




