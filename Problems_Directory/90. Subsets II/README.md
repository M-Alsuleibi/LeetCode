# [90. Subsets II](https://leetcode.com/problems/subsets-ii/description/) `MEDIUM`
![Screenshot from 2024-11-08 17-17-14.png](https://assets.leetcode.com/users/images/5edf182e-8aa7-4a05-93ac-7fed412dabc3_1731079062.9682987.png)

)
# Intuition

<!-- Describe your first thoughts on how to solve this problem. -->

- Iterate over the `nums` array and using a **Decision Tree**, with two branches in each iteration. In each branch (iteration) either include the element or NOT include it .
- To validate the branch of NOT include the element, we need to sort($$O(nlogn)$$). So we can skip all duplicates when we want to decide of NOT include the elemenen while building the subsets.
# Approach

<!-- Describe your approach to solving the problem. -->

- Initiate `res` which is a list of lists to return as a result.
- Sort the input array. Sorting costs $$O(nlogn)$$ which doesn't affect the overall time complexity in brute force backtracking problems $$O(2^n)$$

- Define `helper()` to proceed the backtracking. The function accepts these arguments:

  - `i` : the index of `nums`.

  - `curSet` : reference of the current set we build in each branch, either include `nums[i]` or not include it.

  note: since `curSet` is a reference so in every recursive call we update the same array, this is why we use `[:]` notation in the base case when we add it to the result, It creates a copy of `curSet` every time the recursive call proceed  same as using copy function(`curSet.copy()`) .

  

# Complexity

- Time complexity:

<!-- Add your time complexity here, e.g. $$O(n)$$ -->

$$O(n * 2^n)$$

- Space complexity:

<!-- Add your space complexity here, e.g. $$O(n)$$ -->

$$O(n)$$

# Code
```python3 []
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Backtracking: T O(n * 2^n), M O(n)
        res = []
        nums.sort()

        def helper(i, curSet):
            if i == len(nums):
                res.append(curSet[:]) # same as: curSet.copy()
                return
            # Decision of All subsets that include nums[i]    
            curSet.append(nums[i])
            helper(i + 1, curSet)
            curSet.pop()
            # Decision of All subsets that don't include nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            helper(i + 1, curSet)     
            
        helper(0, [])
        return res

           
```
