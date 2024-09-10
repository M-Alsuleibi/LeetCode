# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
- To find the minimum in circularly sorted array we iterate over the array and collect the minimum number but this is brute force $$O(n)$$ solution.
- We want to take advantage of sorting proprety of the array  by using a variation of _Binary Search_ algorithm and solve it in $$O(log)$$ time.
# Approach
<!-- Describe your approach to solving the problem. -->
- using a variation of _Binary Search_ to finding the minimum elemnet in circularly sorted array with NO duplicates. This minimum number act as **Pivot** to the sorted array.
- **Pivot** proprety -> **next** and **previous** numbers are both **greater**.
- There are 4 cases to cover as it appear in code comments.
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
   def findMin(self, nums: List[int]) -> int:
       # Brute Force: Tc = O(n), Sc = O(1)
       # minElemnt = nums[0]
       # for num in nums:
       #     if num < minElemnt:
       #         minElemnt = num
       # return minElemnt
       # ------------------------------------
       # Optimized: using a variation of Binary Search to find the minimum(Pivot) in
       # circularly sorted array with condition :All the integers of the array are unique.
       # Tc = O(nlogn), Sc = O(1)
       L, R = 0, len(nums) - 1
       while L <= R:
           mid = (L+R) // 2
           #case 1
           # adding = with < to cover a single elemnt array case
           if nums[L] <= nums[R]:
               return nums[L]
           prev, next = (mid -1), (mid + 1) % len(nums)
           #case 2
           if nums[mid] <= nums[prev] and nums[mid] <= nums[next]:
               return nums[mid]
           #case 3
           elif nums[mid] >= nums[L]:
               L = mid + 1
            #case 4
           elif nums[mid] <= nums[R]:
               R = mid - 1          




```

