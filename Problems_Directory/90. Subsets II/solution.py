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

           
