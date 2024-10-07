# [1913. Maximum Product Difference Between Two Pairs](https://leetcode.com/problems/maximum-product-difference-between-two-pairs/description/) `EASY`
# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Having the maximum production difference between two pairs means to have the product of **smallest two numbers**  subtracted from the product of **largest two numbers**

# Approach
<!-- Describe your approach to solving the problem. -->
#### Brute Force Approach: 
Ascendingly sorting the array and extract the smallest two numbres from the beggining of the array and extract the largest two numbers from the end of the array and do the operation as follows:

```python3 []
    nums.sort()
    w, x, y, z = nums[0], nums[1], nums[-2], nums[-1]
    return (y * z) - (w * x)
    
```
#### Optimized Approach:
- Since we need the maximum and minimum numbers, we can use heaps that provide a $$O(1)$$ time complexity for popping a max or a min number .
- We construct **Two Heaps**, one a maxHeap and another a minHeap.
- from the **maxHeap** we retrive the largest two numbers. From the **minHeap** we retrive the smallest two numbers.
- Constucting a heap from array nums (**heapify**) costs O(n).

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
    def maxProductDifference(self, nums: List[int]) -> int:
        # Brute Force: T O(nlogn), M O(1)
        # Optomized: constructing min/max heaps with a cost of O(2 * n) to heapify it twice
        # T O(n), M O(n)
        minHeap = [ num for num in nums]
        maxHeap = [-num for num in nums]
        heapq.heapify(minHeap)
        heapq.heapify(maxHeap)
        w = x = y = z = 0
        w = heapq.heappop(minHeap)
        x = heapq.heappop(minHeap)
        y = - heapq.heappop(maxHeap)
        z = - heapq.heappop(maxHeap)
        return (y * z) - (w * x)
    
```
![Screenshot from 2024-10-07 00-23-48.png](https://assets.leetcode.com/users/images/693e1862-67fe-42ad-a01c-161fa96ced50_1728337468.6400497.png)
