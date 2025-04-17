# [198. House Robber](https://leetcode.com/problems/house-robber/description/?envType=study-plan-v2&envId=dynamic-programming) `MEDIUM`

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
The intuition in to maximize the sum of non adjacent elements.
# Approach
<!-- Describe your approach to solving the problem. -->
1. Create a recursive function that represents the decision at each house:

- If we rob the current house, we add its value and move to the house two steps away
- If we skip the current house, we move to the adjacent house
- Take the maximum of these two options
```python3[]
 def rob(self, nums: List[int]) -> int:

        def bruteForce(ind):
            if ind == 0:
                return nums[0]
            if ind < 0:
                return 0
            rob = nums[ind] + bruteForce(ind-2)
            notRob = 0 + bruteForce(ind-1)
            return max(rob, notRob)

        return bruteForce(len(nums)-1)
```
2. To avoid redundant calculations, I used memoization to store already computed results:

- Initialize a memo array with -1 values to indicate uncalculated states
- Before calculating a result, check if it's already in the memo array
- After calculating, store the result in the memo array

3. Base cases:

- If we reach the first house (index 0), we return its value
- If we go beyond the first house (negative index), we return 0


4. Start the recursion from the last house (index n-1)
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
    def rob(self, nums: List[int]) -> int:
        memo = [-1]*len(nums)
        def bruteForce(ind):
            # memoization : O ()
            if memo[ind] != -1:
                return memo[ind]
            if ind == 0:
                return nums[0]
            if ind < 0:
                return 0

            rob = nums[ind] + bruteForce(ind-2)
            notRob = 0 + bruteForce(ind-1)

            memo[ind] = max(rob, notRob)
            return memo[ind]

        return bruteForce(len(nums)-1)            
```
