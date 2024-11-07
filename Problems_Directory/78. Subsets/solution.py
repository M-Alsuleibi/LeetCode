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
