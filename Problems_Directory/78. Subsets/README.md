# [78. Subsets](https://leetcode.com/problems/subsets/description/) `MEDIUM`
![Screenshot from 2024-11-07 22-14-51.png](https://assets.leetcode.com/users/images/a974b82d-17e8-4c25-962f-49b0f0a02e2a_1731010509.6367767.png)


# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Iterate over the `nums` array and using a **Decision Tree**, with two branches in each iteration. In each branch (iteration) either include the element or NOT include it .
# Approach
<!-- Describe your approach to solving the problem. -->
- Initiate `res` which is a list of lists to return as a result.
- Define `helper()` to proceed the backtracking. The function accepts these arguments:
  - `i` : the index of `nums`.
  - `res` : reference of result array.
  - `curSet` : reference of the current set we build in each branch, either include `nums[i]` or not include it.
note: since `curSet` is a reference so in every recursive call we update the same array, this is why we use `.copy()` in the base case when we add it to the result, since we wil use it again in other recursive calls.
  - `num` : refernce to the input array.

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
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Backtracking: T O(n * 2^n), M O(n)
        res = []
        self.helper(0, res, [], nums)
        return res
    def helper(self, i, res, curSet, nums):
        # Base case
        if i == len(nums):
            res.append(curSet.copy())
            return
        # include nums[i]
        curSet.append(nums[i])
        self.helper(i + 1, res, curSet, nums) 
        curSet.pop()

        # Not include nums[i]
        self.helper(i + 1, res, curSet, nums)
```

