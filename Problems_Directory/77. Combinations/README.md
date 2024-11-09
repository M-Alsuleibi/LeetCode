# [77. Combinations](https://leetcode.com/problems/combinations/description/) `MEDIUM`
# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Use **decision tree** like the approach of generating all subsets. BUT here instead of generate only subsets that have length `k`. And since the range is `[1 - n]` so there is no duplicates in the range to handle.
# Approach
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
$$O(K∗2 ^N)$$
- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
$$O(N)$$
# Code
```python3 []
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # The result combinations list of lists
        combs = []
        
        # i is the individual number
        def helper(i, curComb):
            # 1st base case: curCumb > k
            if len(curComb) == k:
                combs.append(curComb[::]) # if we don't pass the copy the result(combs) will be [[],[],[],[],[],[]]
                return
            # 2nd base case: i > n
            if i >= n + 1:
                return
            # decision to include i
            curComb.append(i)
            helper(i + 1, curComb)
            # decision to NOT include i
            curComb.pop()        
            helper(i + 1, curComb)        

        helper(1, [])
        return combs    
```
